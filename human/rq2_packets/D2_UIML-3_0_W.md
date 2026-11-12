# Artefact set D2_UIML-3_0_W

## Use cases
- CreateUIML (actor: User)

## Class diagram
- MetaData: attributes ['name']; methods []
- Header: attributes []; methods []
- UIML: attributes ['header', 'interface']; methods ['add_interface']
- Interface: attributes []; methods []
- UIML --association--> Header
- UIML --association--> Interface
- Header --aggregation--> MetaData

## Python code
```python
class MetaData:
    def __init__(self, name: str):
        self.name = name

class Header:
    pass
class Interface:
    pass
class UIML:
    def __init__(self, header: Header):
        self.header = header
        self.interface = []
    def add_interface(self, interface: Interface):
        self.interface.append(interface)
```