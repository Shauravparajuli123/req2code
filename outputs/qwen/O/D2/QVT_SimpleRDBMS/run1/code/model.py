class RmodelElement:
    def __init__(self, kind: str):
        self.kind = kind


class Schema:
    pass

class Table:
    def __init__(self, schema: Schema):
        self.schema = schema
        self.keys = []
        self.columns = []
    def add_column(self, column: Column):
        self.columns.append(column)
    def add_key(self, key: Key):
        self.keys.append(key)

class Column:
    def __init__(self, type: str, table: Table):
        self.type = type
        self.table = table
        self.foreign_keys = []
    def add_foreign_key(self, foreign_key: ForeignKey):
        self.foreign_keys.append(foreign_key)

class Key:
    def __init__(self, table: Table):
        self.table = table
    def add_opposite_foreign_key(self, foreign_key: ForeignKey):
        pass

class ForeignKey:
    def __init__(self, key: Key):
        self.key = key
        self.columns = []
    def add_column(self, column: Column):
        self.columns.append(column)
    def set_key(self, key: Key):
        self.key = key