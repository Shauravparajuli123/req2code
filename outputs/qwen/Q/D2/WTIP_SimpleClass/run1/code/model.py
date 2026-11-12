from typing import Type, List

class Classifier:
    def __init__(self):
        pass
    def __str__(self) -> str:
        raise NotImplementedError()

class PrimitiveDataType(Classifier):
    def __init__(self, name: str):
        self.name = name
    def __str__(self) -> str:
        raise NotImplementedError()

class Association(Classifier):
    def __init__(self, name: str, src: Type[Classifier]):
        self.name = name
        self.src = src
    def __str__(self) -> str:
        raise NotImplementedError()

class Attribute(Classifier):
    def __init__(self, name: str, type: Type[Classifier]):
        self.name = name
        self.type = type
    def __str__(self) -> str:
        raise NotImplementedError()

class SimpleClass(Classifier):
    def __init__(self, parent: Type[Classifier], association: Association, attribute: Attribute):
        self.parent = parent
        self.association = association
        self.attribute = attribute
    def __str__(self) -> str:
        raise NotImplementedError()