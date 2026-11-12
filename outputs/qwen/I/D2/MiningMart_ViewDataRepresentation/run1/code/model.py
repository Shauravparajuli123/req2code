from typing import List

class ModelElement:
    pass
class SimplifiedMiningMart:
    pass
class Classifier:
    def __init__(self, name: str):
        self.name = name
class StructuralFeature:
    pass
class Class(Classifier):
    def __init__(self, name: str):
        self.name = name
        self.attributes: List[Attribute] = []
class DataType(Classifier):
    def __init__(self, name: str):
        self.name = name
        self.attribute: Attribute = None
class Attribute:
    def __init__(self, name: str, class_: Class):
        self.name = name
        self.class_ = class_
        self.data_type: DataType = None