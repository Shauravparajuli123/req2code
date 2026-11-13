class Call:
    def __init__(self, method_name, database_row, name):
        self.method_name = method_name
        self.database_row = database_row
        self.name = name

class Level:
    def __init__(self, trace, value):
        self.trace = trace
        self.value = value

class Trace:
    def __init__(self, name):
        self.name = name