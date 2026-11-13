from typing import TypeVar, Generic, Optional

class Classifier:
    pass

class PrimitiveDataType(Classifier):
    def __init__(self, name: str):
        self.name = name

class Association:
    def __init__(self, name: str, src: Class):
        self.name = name
        self.src = src

class Attribute:
    def __init__(self, type: Classifier):
        self.type = type

class Class:
    pass

class SimpleClass(Class, Generic[Class, Association, Attribute]):
    def __init__(self, parent: Optional[Class] = None, association: Optional[Association] = None, attribute: Optional[Attribute] = None):
        self.parent = parent
        self.association = association
        self.attribute = attribute