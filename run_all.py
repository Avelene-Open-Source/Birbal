import argparse
import logging
import rasa.core.run

from rasa.core.channels.console import CmdlineInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.tracker_store import MongoTrackerStore
from rasa.core.utils import EndpointConfig

logger = logging.getLogger(__name__)


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu")
    agent = Agent.load("models/dialogue", interpreter=interpreter)
    action_endpoint = EndpointConfig(url="http://localhost:5056/webhook")

    if serve_forever:
        agent.handle_channels([CmdlineInput()])
    return agent


from rasa.core.training import interactive


def interactive_learning(serve_forever=True):
    import logging

    from rasa.core import utils, train

    logger = logging.getLogger(__name__)

    return train(domain_file="domain.yml",
                 output_path="model/dialogue",
                 policy_config = "config_nlu.yml",
                 kwargs={"batch_size": 50,
                         "epochs": 200,
                         "max_training_samples": 300
                         },
                 training_resource='data/stories.md')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="debug log for development and production"
    )
    parser.add_argument("-d", "--debug", help="Set the logging level")
    args = parser.parse_args()
    if args == "debug":
        logging.DEBUG = True
    else:
        logging.DEBUG = False
    # run()
    # agent = interactive_learning()
    # interactive.run_interactive_learning('data/stories.md')
