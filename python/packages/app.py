from packages.os.arguments import Arguments
from packages.persistency.data import Data
from packages.config.config import Config
class App:

    def start():
        db_memory = Data(db_type="inmemory", db_name="inmemory.db")
        print(db_memory.db_name)
