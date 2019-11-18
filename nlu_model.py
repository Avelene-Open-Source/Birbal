import logging

from rasa.nlu.training_data import load_data
from rasa.nlu import config
from rasa.nlu.model import Trainer
# from rasa_nlu.model import Metadata, Interpreter

logger = logging.getLogger(__name__)


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name="nlu")
    logger.info(f"Model trained. Stored in '{model_directory}'.")
    return model_directory


# def run_nlu():
#     interpreter = Interpreter.load('./models/default/nlu')

if __name__ == "__main__":
    train_nlu("./data/data/", "config.yml", "./models")
    # run_nlu()
