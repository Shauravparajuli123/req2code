from typing import List

class Definition:
    pass

class Method:
    def __init__(self, definition: Definition):
        self.definition = definition
        self.name: str = ''
        self.return_type: str = ''
        self.parameters: List[str] = []

class MethodDefinition:
    def __init__(self, name: str):
        self.name = name
        self.parameters: List[str] = []

class JavaSource:
    def __init__(self):
        self.classes: List[Definition] = []

def invoke_class(class_name: str):
    raise NotImplementedError

def invoke_method(method: Method):
    raise NotImplementedError
