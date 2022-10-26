from dataclasses import dataclass
import sqlite3

@dataclass(init=True, repr=True, match_args=True)
class Data:
    db_type: str
    db_name: str
    # if db_type == "inmemory":
    #     con = sqlite3.connect(":memory:")
    # if db_type == "file":
    #     con = sqlite3.connect(db_name)


