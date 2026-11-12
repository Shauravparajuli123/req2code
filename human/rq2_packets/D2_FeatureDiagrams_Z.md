# Artefact set D2_FeatureDiagrams_Z

## Use cases
(none)

## Class diagram
- Node: attributes ['description', 'reference']; methods ['addAttribute', 'addXORGroup']
- Attribute: attributes ['description', 'name', 'key']; methods []
- XORGroup: attributes ['preliminary']; methods ['addNode']
- ORGroup: attributes ['preliminary']; methods ['addNode']
- Child: attributes []; methods ['addNode', 'addORGroup']
- Node --composition--> Attribute
- Node --composition--> XORGroup
- Node --composition--> ORGroup
- Child --composition--> Node
- Child --composition--> ORGroup

## Python code
```python
from typing import List, Optional

class Attribute:
    def __init__(self, description: str, name: str, key: bool):
        self.description = description
        self.name = name
        self.key = key

class XORGroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

class ORGroup:
    def __init__(self, preliminary: bool):
        self.preliminary = preliminary

class Node:
    def __init__(self, description: str, attributes: List[Attribute], xor_groups: List[XORGroup], or_groups: List[ORGroup]):
        self.description = description
        self.attributes = attributes
        self.xor_groups = xor_groups
        self.or_groups = or_groups
        self.reference = None

class Child:
    def __init__(self, nodes: Optional[List[Node]] = None, or_groups: Optional[List[ORGroup]] = None):
        self.nodes = nodes if nodes else []
        self.or_groups = or_groups if or_groups else []

```