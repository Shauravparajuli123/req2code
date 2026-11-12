# Artefact set D2_UIML-3_0_Y

## Use cases
- CreateUIML (actor: User)

## Class diagram
- UIML: attributes ['header', 'interfaces']; methods ['createHeader']
- Header: attributes ['metas']; methods []
- MetaData: attributes ['name']; methods []
- UIML --composition--> Header
- UIML --aggregation--> Interface
- Header --aggregation--> MetaData

## Python code
```python
from typing import List

class MetaData:
    def __init__(self, name: str):
        self.name = name

class Interface:
    pass
class Header:
    def __init__(self):
        self.metas: List[MetaData] = []
class UIML:
    def __init__(self):
        self.header: Header = Header()
        self.interfaces: List[Interface] = []
    def createHeader(self):
        raise NotImplementedError
```