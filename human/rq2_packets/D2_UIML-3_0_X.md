# Artefact set D2_UIML-3_0_X

## Use cases
- CreateUIML (actor: User)

## Class diagram
- Model: attributes ['uimls']; methods []
- Uiml: attributes ['header', 'interfaces']; methods ['addInterface']
- Header: attributes ['name', 'metas']; methods ['addMetaData']
- MetaData: attributes ['name']; methods []
- Interface: attributes []; methods []
- Uiml --composition--> Header
- Uiml --aggregation--> Interface
- Header --aggregation--> MetaData

## Python code
```python
from typing import List, Optional

class MetaData:
    def __init__(self, name: str):
        self.name = name

class Header:
    def __init__(self, metas: List[MetaData]):
        self.metas = metas

class Uiml:
    def __init__(self, header: Optional[Header] = None, interfaces: Optional[List[str]] = None):
        self.header = header
        self.interfaces = interfaces

class Model:
    def __init__(self, uiml: Uiml):
        self.uiml = uiml
        raise NotImplementedError

```