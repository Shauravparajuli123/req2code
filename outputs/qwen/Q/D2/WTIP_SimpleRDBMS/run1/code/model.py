from typing import List

class NameString:
    pass

class Column:
    def __init__(self, name: str):
        self.name = name

class Fkey:
    def __init__(self):
        pass
    def referencesTable(self) -> None:
        raise NotImplementedError
    def getReferencedTable(self) -> None:
        raise NotImplementedError

class Table:
    def __init__(self, name: str):
        self.name = name
        self.columns: List[Column] = []
        self.fkeys: List[Fkey] = []
    def hasColumn(self) -> None:
        raise NotImplementedError
    def hasFkey(self) -> None:
        raise NotImplementedError