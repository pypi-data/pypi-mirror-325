import logging
import pandas as pd
from datasets import load_from_disk, load_dataset
from flair.data import Sentence, Span, Corpus
from flair.datasets import FlairDatapointDataset
from tqdm import tqdm

logger = logging.getLogger(__name__)


class DatasetProcessor:

    def load_dataset_file(self, file_path) -> dict:
        """
        Load a dataset from disk or other formats using the `datasets` library.
        """
        try:
            dataset = load_from_disk(file_path)
            logger.info("Loaded arrow dataset")
            if not dataset.keys():
                dataset = {"test": dataset}
            logger.info(f"Splits: {dataset.keys()}")
            self.dataset = dataset
            return dataset
        except FileNotFoundError:
            try:
                dataset = load_dataset("csv", data_files=file_path)
                dataset["test"] = dataset.pop("train")
                logger.info(f"Splits: {dataset.keys()}")
                self.dataset = dataset
                return dataset
            except Exception as error:
                try:
                    dataset = load_dataset(file_path)
                    logger.info("Loaded dataset")
                    logger.info(f"Splits: {dataset.keys()}")
                    self.dataset = dataset
                    return dataset
                except Exception as error:
                    raise ValueError(
                        f"Could not load dataset from {file_path}. "
                        f"Encountered error: {error}"
                    )

    def load_cache(self, dataset, use_cache: bool = False) -> tuple:
        """
        Filter out anonymized data and check if the dataset contains non-anonymized records.
        """
        if use_cache:
            try:
                target_dataset = dataset.filter(
                    lambda example: example["annonymised"] == 0
                )
                logger.info(
                    f"Cache enabled | skipping anonymization for {len(dataset['test'])} rows | Running on {len(target_dataset['test'])} rows"
                )
            except:
                target_dataset = dataset

            if len(target_dataset["test"]) == 0:
                logger.info("All data has been anonymized, exiting...")
                exit()
            else:
                logger.info(f"Anonymizing {len(target_dataset['test'])} rows")
        else:
            target_dataset = dataset

        return target_dataset, dataset

    def prepare_flair_dataset(
        self, dataset, text_col: str, label_col: str = None
    ) -> Corpus:
        """
        Prepare a Huggingface DatasetDict for FLAIR model training in NER.
        """
        flair_dataset = {}

        for split in dataset.keys():
            sentences = []
            try:
                for sentence_text, entities in tqdm(
                    zip(dataset[split][text_col], dataset[split][label_col]),
                    total=dataset[split].num_rows,
                    desc=f"Processing {split} split...",
                ):
                    sentence = Sentence(str(sentence_text))
                    sorted_entities = sorted(entities, key=lambda x: x.get("start", 0))

                    for entity in sorted_entities:
                        char_start = entity.get("start")
                        char_end = entity.get("end")
                        label = entity.get("label")

                        if any(v is None for v in [char_start, char_end, label]):
                            tqdm.write(
                                f"Skipping entity due to missing values: {entity}"
                            )
                            continue

                        start_token_idx, end_token_idx = None, None
                        for token_idx, token in enumerate(sentence.tokens):
                            token_start, token_end = (
                                token.start_position,
                                token.end_position,
                            )

                            if (
                                start_token_idx is None
                                and char_start >= token_start
                                and char_start <= token_end
                            ):
                                start_token_idx = token_idx

                            if char_end >= token_start and char_end <= token_end:
                                end_token_idx = token_idx
                                break

                        if start_token_idx is not None and end_token_idx is not None:
                            span = Span(
                                tokens=sentence.tokens[
                                    start_token_idx : end_token_idx + 1
                                ]
                            )
                            span.add_label("ner", label)
                        else:
                            tqdm.write(
                                f"Could not find matching tokens for entity: {entity}"
                            )
                            tqdm.write(f"In sentence: {sentence_text}")

                    sentences.append(sentence)
            except Exception as e:
                for i in tqdm(
                    range(len(dataset[split])),
                    total=len(dataset[split]),
                    desc=f"Processing {split} split...",
                ):
                    sentence_text = str(dataset[split][i][text_col])
                    sentences.append(Sentence(sentence_text))

            flair_dataset[split] = sentences

        try:
            train_dataset = FlairDatapointDataset(flair_dataset["train"])
            eval_dataset = FlairDatapointDataset(flair_dataset["eval"])
            test_dataset = FlairDatapointDataset(flair_dataset["test"])
            corpus = Corpus(train=train_dataset, dev=eval_dataset, test=test_dataset)
        except:
            test_dataset = FlairDatapointDataset(flair_dataset["test"])
            corpus = Corpus(test=test_dataset)

        return corpus

    def save_dataset_file(
        self,
        original_data,
        target_dataset,
        predictions: list = None,
        text_column: str = "text",
        output_dir: str = "predictions.csv",
        cache=False,
    ):
        """
        Save dataset predictions to a file.
        """
        logger.info(f"Saving predictions to {output_dir}")
        df_new = target_dataset["test"].to_pandas()
        if predictions:
            df_new[text_column] = predictions
        df_new["annonymised"] = 1

        if cache:
            df_old = original_data["test"].to_pandas()
            df_new = pd.concat([df_old, df_new], ignore_index=True)

        output_path = (
            output_dir
            if output_dir.endswith(".csv")
            else f"{output_dir}/predictions.csv"
        )
        df_new.to_csv(output_path, index=False)
