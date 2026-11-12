from abc import ABC, abstractmethod

class Definition(ABC):
    def __init__(self, name: str):
        self.name = name
    @abstractmethod
defineClass(self):
        pass
    @abstractmethod
defineMethod(self):
        pass

class MethodDefinition:
    def __init__(self):
        pass
    def methodDefinition(self):
        raise NotImplementedError

class Method:
    def __init__(self):
        pass
    def invokeMethod(self):
        raise NotImplementedError
