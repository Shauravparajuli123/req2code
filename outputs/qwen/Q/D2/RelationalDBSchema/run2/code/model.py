from typing import List

class Column:
    def __init__(self, datatype: str, default_value: str, owner: Table):
        self.datatype = datatype
        self.default_value = default_value
        self.owner = owner

class Table:
    def __init__(self, columns: List[Column]):
        self.columns = columns

class Database:
    def __init__(self, sgbd_name: str, tables: List[Table] =[]):
        self.sgbdName = sgbd_name
        self.tables = tables
