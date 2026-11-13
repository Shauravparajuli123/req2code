from typing import List

class ModelElement:
    def __init__(self):
        pass
    def __str__(self) -> str:
        raise NotImplementedError()

class Classifier:
    def __init__(self, name: str):
        self.name = name
    def __str__(self) -> str:
        raise NotImplementedError()

class Class:
    def __init__(self, name: str):
        self.name = name
        self.attributes: List[Attribute] = []
    def __str__(self) -> str:
        raise NotImplementedError()

class DataType:
    def __init__(self, attribute: Attribute):
        self.attribute = attribute
    def __str__(self) -> str:
        raise NotImplementedError()

class Attribute:
    def __init__(self, name: str, class_: Class):
        self.name = name
        self.class_ = class_
    def __str__(self) -> str:
        raise NotImplementedError()