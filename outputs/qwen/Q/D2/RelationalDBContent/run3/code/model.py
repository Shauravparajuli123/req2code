class RelationalDBContent:
    def __init__(self, name: str):
        self.name = name


class Database:
    def __init__(self, sgbdName: str):
        self.sgbdName = sgbdName


class Table:
    def __init__(self, database: Database):
        self.database = database


class Tuple:
    def __init__(self, table: Table):
        self.table = table


class TupleElement:
    def __init__(self, value: str):
        self.value = value