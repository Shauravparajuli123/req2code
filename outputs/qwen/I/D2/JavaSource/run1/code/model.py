from abc import ABC, abstractmethod

class Definition(ABC):
    @abstractmethod
definition_id(self) -> str:
        pass

class MethodDefinition:
    def __init__(self, name: str):
        self.name = name

class Method(Definition):
    def __init__(self, method_definition: MethodDefinition):
        self.method_definition = method_definition
        self.name = method_definition.name
    def invoke(self):
        raise NotImplementedError

class ClassDefinition(Definition):
    def __init__(self, name: str, superclass: 'ClassDefinition' = None):
        self.name = name
        self.superclass = superclass
    def definition_id(self) -> str:
        return self.name

class JavaSource:
    def __init__(self):
        self.classes = []
    def add_class(self, class_def: ClassDefinition):
        self.classes.append(class_def)
    def invoke_method(self, method: Method):
        method.invoke()