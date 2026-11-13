from typing import List, Optional

class Node:
    def __init__(self, description: str, reference: str):
        self.description = description
        self.reference = reference
        self.attributes: List[Attribute] = []
        self.xorgroups: List[Xorgroup] = []
        self.orgroups: List[Orgroup] = []

class Attribute:
    def __init__(self, description: str, name: str, key: bool, node: Node):
        self.description = description
        self.name = name
        self.key = key
        self.node = node

class Orgroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary
        self.nodes: List[Node] = []

class Xorgroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary
        self.nodes: List[Node] = []

class Child:
    def __init__(self):
        self.nodes: List[Node] = []
        self.orgroups: List[Orgroup] = []
        self.xorgroups: List[Xorgroup] = []