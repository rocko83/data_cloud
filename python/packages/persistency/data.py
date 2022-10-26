import logging
from dataclasses import dataclass
import sqlite3

@dataclass(init=True, repr=True, match_args=True)
class Data:
    db_type: str
    db_name: str
    logger = logging.getLogger(__name__)

    def get_db_type(self):
        return self.db_type

    def get_db_name(self):
        return self.db_name
    def get_data(self):
        self.__init_db()
    def __init_db(self):

        try:
            self.db_init
        except AttributeError as e:
            self.logger.debug(f"db init false")
            db_init = False
        else:
            self.logger.debug(f"db init true")
            db_init = True
        if db_init == False:
            try:
                if self.db_type == "inmemory":
                    self.con = sqlite3.connect(":memory:")
                if self.db_type == "file":
                    self.con = sqlite3.connect(self.db_name)
            except Exception as e:
                logging.error(f"{e}")
            else:
                self.db_init = True



