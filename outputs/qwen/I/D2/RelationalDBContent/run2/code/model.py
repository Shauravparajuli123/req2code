from typing import List

class String:
    pass

class TupleElement:
    def __init__(self, value: str):
        self.value: str = value

class Tuple:
    def __init__(self, tuple_element: TupleElement):
        self.tuple_element: TupleElement = tuple_element

class Table:
    def __init__(self, database: 'Database'):
        self.database: Database = database

class Database:
    def __init__(self, sgbd_name: str):
        self.sgbd_name: str = sgbd_name
        self.tables: List[Table] = []

class RelationalDBContent:
    def __init__(self):
        self.tables: List[Table] = []
        self.tuples: List[Tuple] = []

class Association:
    def __init__(self, owner: 'Object'):
        self.owner: 'Object' = owner

# Association between TupleElement and Tuple
association = Association(owner=None)

class Object:
    pass