class TupleElement:
    def __init__(self, value):
        self.value = value
    def defineValue(self):
        raise NotImplementedError

class Tuple:
    def __init__(self):
        pass
    def addTupleElement(self, tuple_element):
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
    def addRelationalDBcontent(self, relational_db_content):
        raise NotImplementedError