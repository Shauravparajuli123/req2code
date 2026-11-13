class Classifier:
    def __init__(self, name):
        self.name = name

class PrimitiveDataType(Classifier):
    def __init__(self, name):
        super().__init__(name)

class Association:
    def __init__(self, name, src):
        self.name = name
        self.src = src

class Attribute:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class SimpleClass:
    def __init__(self, parent, association, attribute):
        self.parent = parent
        self.association = association
        self.attribute = attribute
