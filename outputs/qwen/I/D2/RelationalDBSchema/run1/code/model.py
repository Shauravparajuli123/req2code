from typing import List

class Column:
    def __init__(self, datatype: str, default_value: str, owner: 'Table'):
        self.datatype = datatype
        self.default_value = default_value
        self.owner = owner

    def __str__(self) -> str:
        raise NotImplementedError

class Database:
    def __init__(self, sgbd_name: str):
        self.sgbd_name = sgbd_name
        self.tables: List['Table'] = []

    def add_table(self, table: 'Table'):
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

class Table:
    def __init__(self, database: Database):
        self.database = database

    def add_column(self, column: Column) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError