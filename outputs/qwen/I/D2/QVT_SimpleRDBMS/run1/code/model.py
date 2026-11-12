from typing import List

class RmodelElement:
    def __init__(self, kind: str):
        self.kind: str = kind

class SimpleRDBMS:
    pass

class Schema:
    def __init__(self, tables: List[Table] = []) -> None:
        self.tables: List[Table] = tables

class Table:
    def __init__(self, schema: Schema, keys: List[Key] = [], columns: List[Column] = []) -> None:
        self.schema: Schema = schema
        self.keys: List[Key] = keys
        self.columns: List[Column] = columns

class Column:
    def __init__(self, table: Table, type: str) -> None:
        self.table: Table = table
        self.type: str = type

class Key:
    def __init__(self, table: Table, opposite_keys: List[ForeignKey] = []) -> None:
        self.table: Table = table
        self.opposite_keys: List[ForeignKey] = opposite_keys

class ForeignKey:
    def __init__(self, columns: List[Column] = [], key: Key = None) -> None:
        self.columns: List[Column] = columns
        self.key: Key = key
