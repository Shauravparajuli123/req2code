class Column:
    def __init__(self, name: NameString):
        self.name = name
    def defineColumn(self):
        raise NotImplementedError

class Fkey:
    def __init__(self, referenced_table: Table):
        self.referenced_table = referenced_table
    def defineFKey(self):
        raise NotImplementedError

class NameString:
    pass

class Table:
    def __init__(self, name: NameString, columns: List[Column] = [], fkeys: List[Fkey] = []):
        self.name = name
        self.columns = columns
        self.fkeys = fkeys
    def defineTable(self):
        raise NotImplementedError