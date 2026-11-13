from typing import List

class Node:
    def __init__(self, name: str, startLine: int, endLine: int, parent: 'Element' = None):
        self.name = name
        self.startLine = startLine
        self.endLine = endLine
        self.parent = parent

    def hasParent(self) -> bool:
        raise NotImplementedError()

    def verbObject(self) -> str:
        raise NotImplementedError()

class Element:
    def __init__(self):
        pass

    def hasChildren(self) -> bool:
        raise NotImplementedError()

    def verbObject(self) -> str:
        raise NotImplementedError()

class XmlFile:
    def __init__(self):
        pass