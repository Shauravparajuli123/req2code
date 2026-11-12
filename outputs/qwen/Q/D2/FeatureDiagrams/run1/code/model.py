from typing import List, Optional

class Node:
    def __init__(self, description: str, reference: Attribute):
        self.description = description
        self.reference = reference
        self.attributes: List[Attribute] = []
        self.xor_groups: List[XORGroup] = []
        self.or_groups: List[ORGroup] = []

    def addAttribute(self) -> None:
        raise NotImplementedError

    def addChild(self) -> None:
        raise NotImplementedError

    def addNode(self, node: 'Node') -> None:
        raise NotImplementedError

class Attribute:
    def __init__(self, description: str, name: str, key: bool):
        self.description = description
        self.name = name
        self.key = key

class XORGroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

    def addNode(self, node: Node) -> None:
        raise NotImplementedError

class ORGroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

    def addNode(self, node: Node) -> None:
        raise NotImplementedError

class Child:
    def __init__(self):
        pass

    def addNode(self, node: Node) -> None:
        raise NotImplementedError