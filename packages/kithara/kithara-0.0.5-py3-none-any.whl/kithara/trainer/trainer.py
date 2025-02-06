import os

os.environ["KERAS_BACKEND"] = "jax"
import keras
import time
import sys
import jax
from kithara.distributed.sharding.utils import (
    entire_tree_is_sharded,
    is_not_sharded_and_is_large,
    get_size_in_mb,
)
from kithara.model import Model
from kithara.dataset import Dataloader
from kithara.callbacks import Profiler, Checkpointer
from kithara.distributed.sharding._data_sharding import DataSharding
from keras.src.backend.common import global_state
from typing import Any, Union, List, Tuple
import jax.tree_util as jtu
import numpy as np


class Trainer:
    """
    A Trainer class for training and evaluating Kithara models. This base class is designed to be
    subclassed for implementing custom training objectives.

    Attributes:
        model (kithara.Model): The model to be trained or evaluated.
        optimizer (keras.Optimizer): The optimizer used for training.
        train_dataloader (kithara.Dataloader): A dataloader that provides training batches.
        eval_dataloader (kithara.Dataloader, optional): A dataloader that provides evaluation batches.
            Defaults to None.
        steps (int, optional): The total number of training steps to execute, where each step processes
            one batch of data. Defaults to 100.
        log_steps_interval (int, optional): The interval between logging steps. Each log includes the
            current loss value and performance metrics. Defaults to 1.
        eval_steps_interval (int, optional): The interval between evaluation steps. Evaluation is
            disabled if not provided.
        max_eval_samples (int, optional): The maximum number of samples to use during evaluation.
            Uses the entire evaluation dataset if not provided.
        tensorboard_dir (str, optional): The directory path for TensorBoard logs. Can be either a
            local directory or a Google Cloud Storage (GCS) path. Defaults to None.
        profiler (kithara.Profiler, optional): A profiler instance for monitoring performance metrics. Defaults to None.

    Methods:
        loss_fn: Returns a JAX-compatible callable that computes the loss value from logits and labels.
            Defaults to SparseCategoricalCrossentropy.
        train(): Executes the main training loop.
        evaluate(state=None): Performs evaluation using batches from eval_dataloader.
        generate(prompt, stop_token_ids="auto"): Generates text responses in inference mode.
        save_model(filepath): Saves model weights in HDF5 (.h5) format.
    """

    def __init__(
        self,
        model: Model,
        optimizer: keras.Optimizer,
        train_dataloader: Dataloader,
        eval_dataloader: Dataloader = None,
        steps=100,
        log_steps_interval=1,
        eval_steps_interval=sys.maxsize,
        max_eval_samples=sys.maxsize,  # entire batch
        tensorboard_dir=None,
        profiler: Profiler = None,
        checkpointer: Checkpointer = None,
    ):
        # Core components
        self.model = model
        self.optimizer = optimizer
        self.train_dataloader = train_dataloader
        self.eval_dataloader = eval_dataloader

        # Training parameters
        self.steps = steps
        self.tensorboard_dir = tensorboard_dir
        self.step_count = 0
        self.epoch_count = 0
        self.eval_steps_interval = eval_steps_interval
        self.max_eval_samples = max_eval_samples
        self.log_steps_interval = log_steps_interval
        self.global_batch_size = train_dataloader.global_batch_size
        self.profiler = profiler
        self.checkpointer = checkpointer

        # Initialize optimizer and callbacks
        self.optimizer.build(self.model.trainable_variables)
        self.callbacks = self._create_callbacks()

        # JIT compile training and evaluation steps for better performance
        self.train_step = self._make_train_step()
        self.eval_step = self._make_eval_step()

        # Configure data sharding strategy
        self.data_sharding = global_state.get_global_attribute(
            "DATA_SHARDING", DataSharding["fully_replicated"]
        )

        # Validate setup and print summary
        self._print_run_summary()
        self._validate_setup()
        self._validate_memory_usage()

    @property
    def loss_fn(self):
        """Define the loss function for training and evaluation. This property
        is intended to be overriden with custom loss functions.

        Returns:
            A JAX callable that takes y_true and logits as input and returns the loss value.
        """
        return keras.losses.SparseCategoricalCrossentropy(
            from_logits=True,
            ignore_class=self.train_dataloader.dataset.tokenizer.pad_token_id,
        )

    def compute_loss(self, trainable_variables, non_trainable_variables, x, y):
        """Compute model loss in a stateless manner. This function is intended
        to use together with jax.grad, i.e. grad_fn =
        jax.value_and_grad(compute_loss, has_aux=True)

        Args:
            trainable_variables: Model's trainable parameters, obtained with `model.trainable_variables`
            non_trainable_variables: Model's non-trainable parameters, obtained with `model.non_trainable_variables`
            x: Input data
            y: Target data

        Returns:
            tuple: (loss value, updated non-trainable variables)
        """
        logits, non_trainable_variables = self.model.stateless_call(
            trainable_variables, non_trainable_variables, x
        )
        loss = self.loss_fn(y, logits)

        return loss, non_trainable_variables

    @property
    def grad_fn(self):
        """Stateless function that returns the value and gradients from the
        `compute_loss` function."""

        return jax.value_and_grad(self.compute_loss, has_aux=True)

    def _train_step(self, state: Tuple[List[jax.Array]], data: dict):
        """Execute a single training step.

        Args:
            state: Current model state (trainable variables, non-trainable variables, optimizer variables)
            data: Batch of training data, a dictionary containing "x" (input) and "y" (target) entries.
            Input value is directly fed into the model, so it should be exact format expected by the model.
            Target value is used to compute the loss, and should be in the exact format expected by the loss function.

        Returns:
            tuple: (loss value, updated state)
        """
        (
            trainable_variables,
            non_trainable_variables,
            optimizer_variables,
        ) = state
        x, y = data["x"], data["y"]
        (loss, non_trainable_variables), grads = self.grad_fn(
            trainable_variables, non_trainable_variables, x, y
        )
        trainable_variables, optimizer_variables = self.optimizer.stateless_apply(
            optimizer_variables, grads, trainable_variables
        )
        return (
            loss,
            (
                trainable_variables,
                non_trainable_variables,
                optimizer_variables,
            ),
        )

    def train(self):
        """Execute the main training loop.

        This method handles:
        - Epoch iteration
        - Batch processing
        - Loss computation
        - Model updates
        - Progress logging
        - Periodic evaluation
        """

        print("-> Start training...")
        print("The first training step will be slow due to JAX compilation.")

        state = self._get_jax_state(
            trainable_variables=True,
            non_trainable_variables=True,
            optimizer_variables=True,
        )

        # Training loop
        self.callbacks.on_train_begin()
        while self.step_count < self.steps:
            self.epoch_count += 1
            self.callbacks.on_epoch_begin(self.epoch_count)

            epoch_loss = 0
            train_set_size = 0

            # Process each batch in the epoch
            for batch_input in self.train_dataloader:
                if self.step_count >= self.steps:
                    break
                self.step_count += 1

                start_time = time.time()
                self.callbacks.on_train_batch_begin(self.step_count)

                # Prepare and validate input
                batch_input = self._prepare_batch_input_for_training(batch_input)
                self._validate_sharding_correctness(batch_input, state)

                # Execute training step
                loss, state = self.train_step(state, batch_input)
                epoch_loss += loss
                train_set_size += self.global_batch_size

                # Log progress
                if self.step_count == 1 or self.step_count % self.log_steps_interval == 0:
                    # Wait for computation to complete for accurate step time
                    jax.block_until_ready(loss)

                    step_time = time.time() - start_time
                    tokens_per_second_per_device = (
                        self.global_batch_size
                        * self.train_dataloader.dataset.max_seq_len
                        / (step_time * jax.device_count())
                    )
                    print(f"Training loss at step {self.step_count}: {loss}")
                    print(f"Step {self.step_count} took {step_time:.3f}s")
                    print(f"Tokens/s/device: {tokens_per_second_per_device:.2f}")

                self._update_model_with_state(state)
                self.callbacks.on_train_batch_end(self.step_count, {"loss": loss})

                # Periodic evaluation
                if self.step_count % self.eval_steps_interval == 0:
                    self.evaluate(state)
            # Compute epoch statistics
            epoch_loss = epoch_loss / train_set_size
            self.callbacks.on_epoch_end(self.epoch_count, {"epoch_loss": epoch_loss})
            print(f"Train epoch {self.epoch_count} loss : {epoch_loss}")

        self.callbacks.on_train_end()

    def save_model(self, filepath):
        """Save model weights in .h5 format.

        Args:
            filepath (str): Path where model weights will be saved
        """
        self.model.save_weights(filepath)

    def _eval_step(self, state: Tuple[List[jax.Array]], data: dict):
        """Execute a single evaluation step.

        This method performs forward propagation without gradient computation
        to evaluate model performance on provided data.

        Args:
            state: Tuple containing (trainable_variables, non_trainable_variables, optimizer_state)
            data: Dictionary containing input data 'x' and target data 'y'.
            Data should be in the same format as expected by _train_step function.

        Returns:
            tuple: (logits, loss value)
        """
        (trainable_variables, non_trainable_variables, _) = state
        x, y = data["x"], data["y"]
        logits, non_trainable_variables = self.model.stateless_call(
            trainable_variables, non_trainable_variables, x, training=False
        )
        loss = self.loss_fn(y, logits)
        return logits, loss

    def evaluate(self, state=None):
        """Execute the evaluation loop on batches of data provided by the
        `eval_dataloader`.

        This method:
        1. Processes the evaluation dataset
        2. Computes model predictions and loss
        3. Tracks and reports evaluation metrics
        4. Handles callbacks for monitoring

        Args:
            state: Optional tuple of model state. If None, current model state is used.
            Contains (trainable_variables, non_trainable_variables, optimizer_variables)
        """

        if state is None:
            state = self._get_jax_state(
                trainable_variables=True,
                non_trainable_variables=True,
                optimizer_variables=True,
            )

        # Initialize evaluation
        self.callbacks.on_test_begin()
        eval_loss = 0
        eval_set_size = 0

        # Process each batch in evaluation dataset
        for step_i, batch_input in enumerate(self.eval_dataloader):
            if eval_set_size + self.global_batch_size > self.max_eval_samples:
                break

            start_time = time.time()
            # Prepare and shard input
            batch_input = self._prepare_batch_input_for_training(batch_input)
            self._validate_sharding_correctness(batch_input, state)

            # Eval step
            logits, loss = self.eval_step(state, batch_input)

            # Accumulate metrics
            eval_loss += loss
            eval_set_size += self.global_batch_size

            # Logging
            if (step_i + 1) % self.log_steps_interval == 0:
                step_time = time.time() - start_time
                print(f"Eval step {step_i+1} took {step_time:.3f}s")
                print(f"Eval step {step_i+1} loss {loss}")

        # Compute final metrics and report results
        eval_loss = eval_loss / eval_set_size
        self.callbacks.on_test_end({"loss": eval_loss})
        print(f"Eval loss after {self.step_count} training steps: ", eval_loss)
        return eval_loss

    def _make_train_step(self):
        return jax.jit(self._train_step, donate_argnums=(0,))

    def _make_eval_step(self):
        return jax.jit(self._eval_step, donate_argnums=(0,))

    def _get_jax_state(
        self,
        trainable_variables=False,
        non_trainable_variables=False,
        optimizer_variables=False,
    ):
        state = []
        if trainable_variables:
            state.append([v.value for v in self.model.trainable_variables])
        if non_trainable_variables:
            state.append([v.value for v in self.model.non_trainable_variables])
        if optimizer_variables:
            state.append([v.value for v in self.optimizer.variables])
        return tuple(state)

    def _form_global_array(self, path, array: np.ndarray) -> jax.Array:
        """Convert local array to globally sharded array for distributed
        computing. Each accelerator host should call `_form_global_array` with
        their local batch shard, this function will from a logical global batch
        that is sharded across all devices, abiding by the `self.data_sharding`
        partitioning.

        Args:
            path: Tree path for the array (used in error reporting)
            array (np.ndarray): Input array to be distributed

        Returns:
            jax.Array: Distributed global batch
        """

        seq_len = array.shape[1]
        global_shape = (self.global_batch_size, seq_len)

        try:
            local_device_arrays = np.split(
                array, len(self.data_sharding.mesh.local_devices), axis=0
            )
        except ValueError as array_split_error:
            raise ValueError(
                f"Unable to put to devices shape {array.shape} with "
                f"local device count {len(self.data_sharding.mesh.local_devices)} "
                f"at {jtu.keystr(path)}"
            ) from array_split_error

        local_device_buffers = jax.device_put(
            local_device_arrays, self.data_sharding.mesh.local_devices
        )
        return jax.make_array_from_single_device_arrays(
            global_shape, self.data_sharding, local_device_buffers
        )

    def _update_model_with_state(self, state):
        """Update model internal parameters with the provided state."""
        trainable_variables, non_trainable_variables, *_ = state
        for variable, value in zip(self.model.trainable_variables, trainable_variables):
            value = jax.lax.with_sharding_constraint(value, variable._layout)
            variable.assign(value)
        for variable, value in zip(
            self.model.non_trainable_variables, non_trainable_variables
        ):
            value = jax.lax.with_sharding_constraint(value, variable._layout)
            variable.assign(value)

    def _prepare_batch_input_for_training(self, batch: List[str]):
        return jtu.tree_map_with_path(self._form_global_array, batch)

    def _print_run_summary(self):
        # TODO: Implement more structured logging
        for attr_name, attr_value in vars(self).items():
            print(attr_name, attr_value)

    def _create_callbacks(self):
        callbacks = []
        if self.tensorboard_dir:
            callbacks.append(
                keras.callbacks.TensorBoard(
                    log_dir=self.tensorboard_dir, update_freq="batch"
                )
            )
        if self.profiler:
            callbacks.append(self.profiler)
        if self.checkpointer:
            callbacks.append(self.checkpointer)

        return keras.callbacks.CallbackList(callbacks, model=self.model)

    def _validate_sharding_correctness(self, data, state):
        """This method performs several sharding correctness checks and prints
        warnings for any sharding issues detected.

        1. Checks if data is properly sharded
        2. Validates sharding of trainable variables
        3. Validates sharding of non-trainable variables
        4. Validates sharding of optimizer variables

        Args:
            data: Input batch to validate
            state: Current model state tuple

        """

        try:
            if not entire_tree_is_sharded(data):
                print(
                    "Warning: data is not sharded",
                    data["y"].shape,
                    data["y"].sharding,
                )
            for variable, value in zip(self.model.trainable_variables, state[0]):
                if is_not_sharded_and_is_large(value):
                    print(
                        f"Step {self.step_count}: trainable variable is not sharded",
                        get_size_in_mb(value) + "mb",
                        variable.path,
                        value.shape,
                        value.sharding,
                    )
            for variable, value in zip(self.model.non_trainable_variables, state[1]):
                if is_not_sharded_and_is_large(value):
                    print(
                        f"Step {self.step_count}: nontrainable variable is not sharded",
                        get_size_in_mb(value) + "mb",
                        variable.path,
                        value.shape,
                        value.sharding,
                    )
            for variable, value in zip(self.optimizer.variables, state[2]):
                if is_not_sharded_and_is_large(value):
                    print(
                        f"Step {self.step_count}: optimizer variable is not sharded",
                        get_size_in_mb(value) + "mb",
                        variable.path,
                        value.shape,
                        value.sharding,
                    )
        except Exception as e:
            print(f"Error during sharding correctness validation: {e}")

    def _validate_memory_usage(self):
        """This method checks the current HBM usage matches the expected HBM
        usage.

        Current HBM usage is calculated by summing the size of all live arrays,
        expected HBM usage is calculated by summing the size of all model and
        optimizer variables.
        """

        total_size = 0
        for v in self.model.variables:
            total_size += get_size_in_mb(v.value)

        for v in self.optimizer.variables:
            total_size += get_size_in_mb(v.value)

        live_arrays = jax.live_arrays()
        live_arrays_size = 0
        for v in live_arrays:
            live_arrays_size += get_size_in_mb(v)

        if not np.isclose(total_size, live_arrays_size, atol=1.0):
            print(
                f"WARNING: Potential memory leakage. HBM usage is {live_arrays_size:.3f} MB "
                f"but model and optimizer are only {total_size:.3f} MB in size."
            )
        else:
            print(
                f"✅ No memory leakage detected. HBM usage ({live_arrays_size:.3f} MB) "
                f"matches model and optimizer size ({total_size:.3f} MB)."
            )

    def _validate_setup(self):
        assert (
            self.max_eval_samples >= self.global_batch_size
        ), "Number of eval examples must be greater or equal to global batch size"

        assert not (
            self.eval_steps_interval != sys.maxsize and self.eval_dataloader is None
        ), "Evaluation steps interval is set but no eval dataloader is provided"
