class Database:
    def __init__(self, sgbdName: str):
        self.sgbdName = sgbdName
        self.tables = []

    def add_table(self, table: 'Table'):
        raise NotImplementedError

    def remove_table(self, table: 'Table'):
        raise NotImplementedError

    def get_table(self, table_name: str) -> 'Table':
        raise NotImplementedError

    src = ['R2', 'R5', 'R6']

class Table:
    def __init__(self, columns: 'Column[]'):
        self.columns = columns

    def add_column(self, column: 'Column'):
        raise NotImplementedError

    def remove_column(self, column: 'Column'):
        raise NotImplementedError

    def get_column(self, column_name: str) -> 'Column':
        raise NotImplementedError

    src = ['R3', 'R7']

class Column:
    def __init__(self, datatype: str, default_value: str, owner: 'Table'):
        self.datatype = datatype
        self.default_value = default_value
        self.owner = owner

    src = ['R4', 'R8']