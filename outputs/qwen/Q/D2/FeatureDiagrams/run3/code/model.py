from typing import List, Optional

class Node:
    def __init__(self, description: str, reference: Attribute):
        self.description = description
        self.reference = reference
        self.xorgroups: List[Xorgroup] = []
        self.orgroups: List[Orgroup] = []

    def add_xorgroup(self, xorgroup: Xorgroup) -> None:
        self.xorgroups.append(xorgroup)

    def add_orgroup(self, orgroup: Orgroup) -> None:
        self.orgroups.append(orgroup)

    def __str__(self) -> str:
        return self.description

    src: List[str] = ['R1', 'R9', 'R10', 'R11']

class Attribute:
    def __init__(self, description: str, name: str, key: bool):
        self.description = description
        self.name = name
        self.key = key

    src: List[str] = ['R2']

class Xorgroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

    def add_node(self, node: Node) -> None:
        pass

    src: List[str] = ['R5', 'R8', 'R12']

class Orgroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

    def add_node(self, node: Node) -> None:
        pass

    src: List[str] = ['R6', 'R13']

class Child:
    def __init__(self):
        pass

    def add_node(self, node: Node) -> None:
        pass

    src: List[str] = ['R10', 'R11']