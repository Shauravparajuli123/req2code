class Classifier:
    def __init__(self, name: str):
        self.name = name

class PrimitiveDataType(Classifier):
    def __init__(self, name: str):
        super().__init__(name)

class TypeString(Classifier):
    def __init__(self, name: str):
        super().__init__(name)

class Association:
    def __init__(self, name: str, src: Classifier):
        self.name = name
        self.src = src

class SimpleClass:
    def __init__(self, parent: Classifier, association: Association, attribute: TypeString):
        self.parent = parent
        self.association = association
        self.attribute = attribute

    def verbObject(self):
        raise NotImplementedError