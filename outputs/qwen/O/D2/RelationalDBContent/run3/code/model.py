class TupleElement:
    def __init__(self, value):
        self.value = value
    def define_value(self):
        raise NotImplementedError

class Tuple:
    def __init__(self):
        pass
    def add_element(self):
        raise NotImplementedError

class Database:
    def __init__(self, sgbdName):
        self.sgbdName = sgbdName

class RelationalDBcontent:
    def __init__(self):
        pass

class Table:
    def __init__(self):
        pass
    def add_tuple(self):
        raise NotImplementedError