from typing import List

class Definition:
    def __init__(self, className: str, superClassName: str):
        self.className = className
        self.superClassName = superClassName
    def createClassDefinition(self) -> None:
        raise NotImplementedError()
    def defineMethod(self) -> None:
        raise NotImplementedError()

class Method:
    def __init__(self, methodName: str):
        self.methodName = methodName
    def invokeMethod(self) -> None:
        raise NotImplementedError()

class MethodDefinition:
    pass