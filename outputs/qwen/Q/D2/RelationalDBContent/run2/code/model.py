from typing import List

class RelationalDBContent:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def add_table(self, table: 'Table') -> None:
        raise NotImplementedError
    
    def add_tuple(self, tuple: 'Tuple') -> None:
        raise NotImplementedError
    
    src = ['R1', 'R4', 'R6', 'R8']

class Database:
    def __init__(self, sgbdName: str):
        self.sgbdName = sgbdName
    
    def __str__(self):
        return self.sgbdName
    
    src = ['R2']

class Table:
    def __init__(self, database: Database):
        self.database = database
    
    def __str__(self):
        return f'Table in {self.database}'
    
    src = ['R7']

class Tuple:
    def __init__(self, table: Table):
        self.table = table
    
    def __str__(self):
        return f'Tuple in {self.table}'
    
    src = ['R6', 'R8']

class TupleElement:
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self):
        return self.value
    
    src = ['R5']