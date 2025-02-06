from petharbor.utils.dataset import DatasetProcessor
from petharbor.utils.device import configure_device
from petharbor.utils.model import load_model, get_predictions_and_anonymise
from petharbor.utils.logging_setup import get_logger
from typing import Optional, Dict, Any
import os


class Anonymiser:
    def __init__(
        self,
        dataset_path: str,
        model_path: str,
        text_column: str = "text",
        cache: bool = True,
        logs: Optional[str] = None,
        device: Optional[str] = None,
        output_dir: str = "output/",
    ):
        self.dataset_path = dataset_path
        self.model_path = model_path
        self.text_column = text_column
        self.cache = cache
        self.logs = logs
        self.device = device
        self.output_dir = output_dir

        self._validate_paths()
        self.logger = self._setup_logger()
        self.device = configure_device(self.device)
        self.model = load_model(self.model_path, self.device)
        self.dataset_processor = DatasetProcessor()

    def _validate_paths(self) -> None:
        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(f"Dataset path does not exist: {self.dataset_path}")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model path does not exist: {self.model_path}")

    def _setup_logger(self) -> Any:
        return (
            get_logger(log_dir=self.logs, method="Advance")
            if self.logs
            else get_logger(method="Advance")
        )

    def _validate_dataset(self, dataset, empty_tag="<<EMPTY>>") -> None:
        if self.text_column not in dataset["test"].column_names:
            raise ValueError(f"Text column '{self.text_column}' not found in dataset")
        if dataset["test"][self.text_column].str.strip().str.len().sum() == 0:
            # Replace empty strings with a tag
            dataset["test"][self.text_column] = dataset["test"][
                self.text_column
            ].str.replace("", f"{empty_tag}")
            self.logger.warning(
                f"Replaced {dataset['test'][self.text_column].str.count(f'{empty_tag}').sum()} empty strings with '{empty_tag}' in {self.text_column} column"
            )

    def anonymise(self) -> None:
        """Anonymizes the text data in the dataset and saves the results."""
        original_data = self.dataset_processor.load_dataset_file(self.dataset_path)
        self._validate_dataset(original_data)

        target_dataset, original_data = self.dataset_processor.load_cache(
            dataset=original_data, use_cache=self.cache
        )

        predictions = get_predictions_and_anonymise(
            model=self.model,
            target_data=target_dataset,
            replaced=True,
            text_column=self.text_column,
        )

        self.dataset_processor.save_dataset_file(
            original_data=original_data,
            target_dataset=target_dataset,
            predictions=predictions,
            text_column=self.text_column,
            output_dir=self.output_dir,
        )

    def predict(self) -> None:
        """Runs the model to predict entities without replacing them."""
        try:
            original_data = self.dataset_processor.load_dataset_file(self.dataset_path)
            self._validate_dataset(original_data)

            target_dataset, original_data = self.dataset_processor.load_cache(
                dataset=original_data, use_cache=self.cache
            )

            predictions = get_predictions_and_anonymise(
                model=self.model,
                targetsq_data=target_dataset,
                replaced=False,
                text_column=self.text_column,
            )

            self.dataset_processor.save_dataset_file(
                original_data=original_data,
                target_dataset=target_dataset,
                predictions=predictions,
                text_column="identifiers",
                output_dir=self.output_dir,
            )
        except Exception as e:
            self.logger.error(f"Anonymisation failed: {e}")
            raise

    def eval(self):
        """Evaluates the trained NER model on the test set."""
        original_data = self.dataset_processor.load_dataset_file(self.dataset_path)
        original_data = self.dataset_processor.prepare_flair_dataset(
            dataset=original_data, text_col=self.text_column, label_col="label"
        )
        test_results = self.model.evaluate(
            original_data.test,
            gold_label_type="ner",
            mini_batch_size=32,
            out_path="predictions.txt",
        )
        print(f"\nTest Set Results: {test_results}")
        return test_results
