import logging
import os
import rasa.utils.io
import asyncio

from rasa.core.agent import Agent
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.policies.fallback import FallbackPolicy
from rasa.core.policies.mapping_policy import MappingPolicy

logger = logging.getLogger(__name__)


async def train_core(domain_file, training_data_file, model_directory):
    agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=3), MappingPolicy(), KerasPolicy(epochs=500)])
    training_data = await agent.load_data(training_data_file, augmentation_factor=10)
    agent.train(training_data)

    # Attention: agent.persist stores the model and all meta data into a folder.
    # The folder itself is not zipped.
    model_path = os.path.join(model_directory, "core")
    agent.persist(model_path)

    logger.info(f"Model trained. Stored in '{model_path}'.")

    return model_path


if __name__ == "__main__":
    rasa.utils.io.configure_colored_logging(loglevel="INFO")
    training_data_file = "./data/stories.md"
    model_path = "./models/dialogue"
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback", core_threshold=0.25, nlu_threshold=0.75)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(train_core(domain_file='domain.yml', training_data_file=training_data_file, model_directory=model_path))
