from typing import List

class NameString(str):
    pass

class Column:
    def __init__(self, name: NameString):
        self.name = name

class Fkey:
    def __init__(self, referenced_table: 'Table'):
        self.referenced_table = referenced_table

class Table:
    def __init__(self, name: NameString):
        self.name = name
        self.columns: List[Column] = []
        self.fkeys: List[Fkey] = []
