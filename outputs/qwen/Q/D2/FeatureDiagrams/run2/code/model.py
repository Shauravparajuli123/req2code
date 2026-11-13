from typing import List, Optional

class Node:
    def __init__(self, description: str, reference: Attribute):
        self.description = description
        self.reference = reference
        self.attributes: List[Attribute] = []
        self.xorgroups: List[Xorgroup] = []
        self.orgroups: List[Orgroup] = []

    def addAttribute(self) -> None:
        raise NotImplementedError('Method implementation required')

    def addXorgroup(self) -> None:
        raise NotImplementedError('Method implementation required')

    def addOrgroup(self) -> None:
        raise NotImplementedError('Method implementation required')

    def hasNode(self, node: 'Node') -> bool:
        raise NotImplementedError('Method implementation required')

class Attribute:
    def __init__(self, description: str, name: str, key: bool):
        self.description = description
        self.name = name
        self.key = key

class Xorgroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

    def addNode(self, node: Node) -> None:
        raise NotImplementedError('Method implementation required')

class Orgroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

    def addNode(self, node: Node) -> None:
        raise NotImplementedError('Method implementation required')

class Child:
    def hasNode(self, node: Node) -> bool:
        raise NotImplementedError('Method implementation required')