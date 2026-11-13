class ModelElement:
    pass

class Class:
    def __init__(self, name):
        self.name = name
    def verbObject(self):
        raise NotImplementedError

class DataType:
    pass

class Attribute:
    pass