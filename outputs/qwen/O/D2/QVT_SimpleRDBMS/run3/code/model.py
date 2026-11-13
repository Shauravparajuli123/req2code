class RmodelElement:
    def __init__(self, kind):
        self.kind = kind

class Schema:
    pass
class Table:
    def __init__(self, schema):
        self.schema = schema
        self.keys = []
        self.columns = []
    def add_column(self, column):
        if column.table is not self:
            raise ValueError('Column must belong to this table')
        self.columns.append(column)
    def add_key(self, key):
        if key.table is not self:
            raise ValueError('Key must belong to this table')
        self.keys.append(key)
class Column:
    def __init__(self, type, table):
        self.type = type
        self.table = table
        self.foreign_keys = []
    def add_foreign_key(self, foreign_key):
        if foreign_key.columns[0] is not self:
            raise ValueError('Column must be part of the foreign key')
        self.foreign_keys.append(foreign_key)
class Key:
    def __init__(self, table):
        self.table = table
    def add_opposite_foreign_key(self, foreign_key):
        if foreign_key.key is not self:
            raise ValueError('Foreign key must refer to this key')
class ForeignKey:
    def __init__(self, key):
        self.key = key
        self.columns = []
    def add_column(self, column):
        if column not in self.columns:
            self.columns.append(column)
    def set_key(self, key):
        if key is not self.key:
            raise ValueError('Key must be the same as the existing key')