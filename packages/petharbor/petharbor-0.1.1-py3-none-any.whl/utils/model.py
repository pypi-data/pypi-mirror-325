import torch
import flair
from petharbor.utils.logging_setup import get_logger
from petharbor.utils.dataset import DatasetProcessor
from petharbor.utils.annonymisation import replace_token
from tqdm import tqdm

logger = get_logger()

def load_model(model_path, device):
    try:
        try:
            logger.info(f"Loading model from {model_path}")
            model = torch.load(model_path, weights_only=False)
            model = flair.models.SequenceTagger.load(model).to(device)
            logger.info(f"Model loaded successfully")
        except Exception as e:
            logger.error(f"Could not load model from {model_path}: {e}")
            model = flair.models.SequenceTagger.load(model_path).to(device)
            logger.info(f"Model loaded successfully")
    except:
        raise RuntimeError(f"Could not load model from {model_path}")
    return model

def get_predictions_and_anonymise(model, target_data, replaced=True, text_column="text"):
    predictions = []
    data_processor = DatasetProcessor()
    corpus = data_processor.prepare_flair_dataset(target_data, text_col=text_column)
    for sentence in tqdm(corpus.test, desc="Inferencing..."):
        model.predict(sentence)
        if sentence.to_dict(tag_type="ner")["entities"]:
            predictions.append(sentence.to_dict(tag_type="ner")["entities"])
        else:
            predictions.append([])
    if replaced:
        predictions = replace_token(
            target_data["test"], predictions, text_column
        )
    predictions = [item.get(text_column) for item in predictions]
    return predictions