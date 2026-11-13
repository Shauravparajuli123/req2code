from typing import Type, TypeVar

T = TypeVar('T')

class Classifier:
    pass

class PrimitiveDataType(Classifier):
    def __init__(self, name: str):
        self.name = name

class Type(Classifier):
    pass

class Association:
    def __init__(self, name: str, src: 'Class'):
        self.name = name
        self.src = src

class SimpleClass(Classifier):
    def __init__(self, name: str, parent: 'SimpleClass' = None):
        self.name = name
        self.parent = parent

class Attribute:
    def __init__(self, name: str, type_: Type):
        self.name = name
        self.type = type_
