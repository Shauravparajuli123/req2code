class RelationalDatabaseContent:
    def __init__(self):
        self.tables = []
        self.tuples = []

    def add_table(self, table: Table):
        raise NotImplementedError

    def add_tuple(self, tuple: Tuple):
        raise NotImplementedError


class TupleElement:
    def __init__(self, value: str):
        self.value = value


class Tuple:
    pass


class Database:
    def __init__(self, sgbdName: str):
        self.sgbdName = sgbdName


class Table:
    def __init__(self, database: Database):
        self.database = database

    def set_database(self, database: Database):
        raise NotImplementedError

