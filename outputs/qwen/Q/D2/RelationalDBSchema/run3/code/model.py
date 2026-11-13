from typing import List

class Column:
    def __init__(self, datatype: str, default_value: str, owner: Table):
        self.datatype = datatype
        self.default_value = default_value
        self.owner = owner
    def __str__(self):
        return f'Column(datatype={self.datatype}, default_value={self.default_value}, owner={self.owner})'

class Table:
    def __init__(self, columns: List[Column]):
        self.columns = columns
    def __str__(self):
        return f'Table(columns={self.columns})'

class Database:
    def __init__(self, sgbdName: str, tables: List[Table] = []):
        self.sgbdName = sgbdName
        self.tables = tables
    def __str__(self):
        return f'Database(sgbdName={self.sgbdName}, tables={self.tables})'
