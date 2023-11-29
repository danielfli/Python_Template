from .auth import Auth
# from .db.sqllite import DatabaseSQL
from .db.storebin import Store_DB

FILE_PATH =".some_data.bin"

class Model:
    def __init__(self):
        self.auth = Auth()
        # self.db = DatabaseSQL()
        self.db = Store_DB(FILE_PATH)

