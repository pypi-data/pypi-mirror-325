from kithara.dataset.dataset import Dataset
from kithara.dataset.utils import initialize_tokenizer, HFtokenize
import ray
from keras.src.backend.common import global_state
import numpy as np
from kithara.dataset.utils import HFtokenize
from typing import Dict
from transformers import AutoTokenizer


class TextCompletionDataset(Dataset):
    """
    A dataset class for standard text completion tasks.

    Args:
        source (ray.data.Dataset): The source Ray dataset containing the text data.
        tokenizer: The tokenizer instance to use.
        tokenizer_handle: Handle/name of the tokenizer to load if not provided.
        column_mapping (Optional[Dict]): Mapping of source column name to expected
            column name ("text")
        model_type (Optional[ModelImplementationType]): Type of model implementation to use.
            Please specify model_type or set MODEL_IMPLEMENTATION in global state. Global
            state is automatically set upon model initialization. Supported types:
            ModelImplementationType.KERASHUB, ModelImplementationType.MAXTEXT
        max_seq_len (int): Maximum sequence length for tokenization (default: 1024).

    """

    def __init__(
        self,
        source: ray.data.Dataset,
        tokenizer: AutoTokenizer = None,
        tokenizer_handle: str = None,
        column_mapping: Dict[str, str] = None,
        model_type: "ModelImplementationType" = None,
        max_seq_len: int = 1024,
    ):
        super().__init__(source)

        assert (tokenizer is not None) or (
            tokenizer_handle is not None
        ), "Either a HF Tokenizer or a HF tokenizer handle must be provided"

        self.source = source
        self.max_seq_len = max_seq_len
        self.tokenizer = (
            initialize_tokenizer(tokenizer_handle) if tokenizer is None else tokenizer
        )
        self.tokenizer.pad_token = "<pad>"
        self.column_mapping = {"text": "text"}
        self.model_type = model_type
        if column_mapping:
            self.column_mapping = {**self.column_mapping, **column_mapping}

    def task_transform(self, sample):
        """Transform the raw sample with standardized key."""
        return {"text": sample[self.column_mapping["text"]]}

    def model_transform(self, sample: Dict[str, str]) -> Dict[str, str]:
        """Transform the text sample into model inputs.

        Returns:
            tuple: Tuple containing input_ids, attention_mask, and label_ids.
        """
        text = sample["text"]
        full_seq = HFtokenize(
            f"<bos>{text}<eos>", self.tokenizer, seq_len=self.max_seq_len
        )
        input_ids = full_seq["input_ids"]
        attention_mask = full_seq["attention_mask"]

        label_ids = np.roll(input_ids, -1)
        label_ids[:, -1] = self.tokenizer.pad_token_id
        return input_ids, attention_mask, label_ids

    def convert_to_model_specific_input(
        self, input_ids: np.ndarray, attention_mask: np.ndarray, label_ids: np.ndarray
    ):
        """
        Convert tokenized inputs into format expected by either the MaxText model
        for the KerasHub model.

        Args:
            input_ids (np.ndarray): Token IDs.
            attention_mask (np.ndarray): Attention mask.
            label_ids (np.ndarray): Label IDs.

        Returns:
            Dict[str, ndarray]: Model-specific formatted inputs.
        """
        # Avoid circular import
        from kithara.model import ModelImplementationType

        model_type = self.model_type or global_state.get_global_attribute(
            "MODEL_IMPLEMENTATION"
        )

        if not model_type:
            raise ValueError(
                "Did you forget to specify model_type during Dataset creation? Please specify model_type or set MODEL_IMPLEMENTATION "
                "in global state. Supported types: `KerasHub`, `MaxText`. You don't need to specify model type if you have already created"
                " a model. "
            )

        input_formats = {
            ModelImplementationType.MAXTEXT: lambda: {
                "x": {
                    "tokens": input_ids,
                    "segment_ids": attention_mask,
                    "positions": np.arange(self.max_seq_len, dtype=np.int32)[None, :],
                },
                "y": label_ids,
            },
            ModelImplementationType.KERASHUB: lambda: {
                "x": {"token_ids": input_ids, "padding_mask": attention_mask},
                "y": label_ids,
            },
        }

        if model_type not in input_formats:
            raise ValueError(f"Unsupported model type: {model_type}")

        return input_formats[model_type]()

    def process_sample(self, sample: int) -> Dict[str, np.ndarray]:
        """Overrides the base class implementation. This function
        process a single sample through the complete transformation pipeline.

        Args:
            sample: Raw sample from the dataset.

        Returns:
            Dict[str, np.ndarray]: Processed sample in model-specific format.
        """
        sample = self.task_transform(sample)
        input_ids, attention_mask, label_ids = self.model_transform(sample)
        sample = self.convert_to_model_specific_input(
            input_ids, attention_mask, label_ids
        )
        return sample

    def to_packed_dataset(self) -> "PackedDataset":
        raise NotImplementedError("Packing is not currently supported")
