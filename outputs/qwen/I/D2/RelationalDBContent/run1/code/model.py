from typing import List

class String:
    pass

class TupleElement:
    def __init__(self, value: str):
        self.value: str = value

class Tuple:
    def __init__(self, elements: List[TupleElement]):
        self.elements: List[TupleElement] = elements

class Table:
    def __init__(self, database: 'Database', name: str):
        self.database: Database = database
        self.name: str = name

class Database:
    def __init__(self, sgbd_name: str):
        self.sgbd_name: str = sgbd_name
        self.tables: List[Table] = []

class RelationalDBContent:
    def __init__(self, tables: List[Table], tuples: List[Tuple]):
        self.tables: List[Table] = tables
        self.tuples: List[Tuple] = tuples

class Association:
    def __init__(self, tuple_element: TupleElement):
        self.tuple_element: TupleElement = tuple_element

# Association class is not directly used in the classes but represents the relationship
# between TupleElement and Tuple
