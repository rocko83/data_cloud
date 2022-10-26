from packages.os.arguments import Arguments
from packages.persistency.data import Data
from packages.config.config import Config
import logging
class App:

    def start():
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.debug("app start")

        args = Arguments()

        db_memory = Data(db_type="inmemory", db_name="inmemory.db")
        db_memory.get_data()
        db_memory.get_data()
