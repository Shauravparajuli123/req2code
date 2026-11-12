from typing import List

class Node:
    def __init__(self, name: str, startLine: int, endLine: int, parent: 'Element' = None):
        self.name = name
        self.startLine = startLine
        self.endLine = endLine
        self.parent = parent

    def hasParent(self) -> bool:
        raise NotImplementedError()

class Element:
    def __init__(self):
        pass

    def addChild(self, child: 'Node') -> None:
        raise NotImplementedError()

    def removeChild(self, child: 'Node') -> None:
        raise NotImplementedError()

class XmlFile:
    def __init__(self):
        self.rootElement: 'Element' = None
        self.textElements: List[Node] = []
