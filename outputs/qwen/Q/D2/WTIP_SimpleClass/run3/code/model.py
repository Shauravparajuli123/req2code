from typing import Type, Optional

class Classifier:
    def __init__(self, name: str):
        self.name = name

class PrimitiveDataType(Classifier):
    def __init__(self, name: str):
        super().__init__(name)

class Class:
    def __init__(self, name: str, parent: Optional['Class'] = None):
        self.name = name
        self.parent = parent
class SimpleClass(Class):
    def __init__(self, name: str, type: Classifier):
        super().__init__(name)
        self.type = type
class Association:
    def __init__(self, name: str, src: Class):
        self.name = name
        self.src = src