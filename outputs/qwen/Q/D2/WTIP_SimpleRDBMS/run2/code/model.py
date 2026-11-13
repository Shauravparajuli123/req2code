class Table:
    def __init__(self, name: str):
        self.name = name

    def hasColumn(self, column: Column) -> bool:
        raise NotImplementedError

    def hasFkey(self, fkey: Fkey) -> bool:
        raise NotImplementedError

class Column:
    def __init__(self, name: str):
        self.name = name
class Fkey:
    def __init__(self):
        pass
    def referencesTable(self, table: Table) -> bool:
        raise NotImplementedError
    def getReferencedTable(self) -> Table:
        raise NotImplementedError
class NameString:
    pass