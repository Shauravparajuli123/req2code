from typing import List

class Definition:
    def __init__(self, name: str):
        self.name = name
    def defineClass(self) -> None:
        raise NotImplementedError()
    def declareClasses(self) -> None:
        raise NotImplementedError()
    def defineMethod(self) -> None:
        raise NotImplementedError()

class Method:
    def invoke(self) -> None:
        raise NotImplementedError()

class MethodDefinition:
    pass
