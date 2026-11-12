class NameString:
    pass

class Column:
    def __init__(self, name):
        self.name = name

class Fkey:
    pass

class Table:
    def __init__(self, name):
        self.name = name
    def hasColumn(self):
        raise NotImplementedError
    def hasFkey(self):
        raise NotImplementedError