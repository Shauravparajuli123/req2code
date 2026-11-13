class Column:
    def __init__(self, datatype: str, default_value: str, owner: Table):
        self.datatype = datatype
        self.default_value = default_value
        self.owner = owner

    def StoreName(self):
        raise NotImplementedError

class Database:
    def __init__(self, sgbd_name: str):
        self.sgbd_name = sgbd_name
        self.tables = []

class Table:
    def __init__(self, database: Database):
        self.database = database