# Artefact set D2_FeatureDiagrams_X

## Use cases
(none)

## Class diagram
- Node: attributes ['description', 'reference']; methods ['addAttribute', 'addChild']
- Attribute: attributes ['description', 'name', 'key']; methods []
- XORGroup: attributes ['preliminary']; methods ['addNode']
- ORGroup: attributes ['preliminary']; methods ['addNode']
- Child: attributes []; methods ['addNode']
- Node --composition--> Attribute
- Node --composition--> XORGroup
- Node --composition--> ORGroup
- Child --association--> Node

## Python code
```python
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
```