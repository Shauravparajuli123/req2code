# Artefact set D2_WTIP_SimpleClass_Z

## Use cases
(none)

## Class diagram
- Classifier: attributes ['name']; methods []
- PrimitiveDataType: attributes ['name']; methods []
- SimpleClass: attributes ['name', 'type']; methods []
- Association: attributes ['name', 'src']; methods []
- PrimitiveDataType --generalization--> Classifier
- Type --generalization--> Classifier
- SimpleClass --association--> Type

## Python code
```python
from typing import Type, TypeVar

Association = TypeVar('Association')
Classifier = TypeVar('Classifier')
PrimitiveDataType = TypeVar('PrimitiveDataType')
TypeString = TypeVar('TypeString')
SimpleClass = TypeVar('SimpleClass')
Class = TypeVar('Class')


class Classifier:
    def __init__(self, name: str):
        self.name = name

class PrimitiveDataType(Classifier):
    def __init__(self, name: str):
        super().__init__(name)

class TypeString(Classifier):
    def __init__(self, name: str):
        super().__init__(name)

class Association:
    def __init__(self, name: str, src: Class):
        self.name = name
        self.src = src

class SimpleClass(Classifier):
    def __init__(self, name: str, parent: Class = None):
        super().__init__(name)
        self.parent = parent

class Class(SimpleClass):
    def __init__(self, name: str, parent: Class = None):
        super().__init__(name, parent)
        self.attributes = []
        self.associations = []

class Attribute:
    def __init__(self, name: str, type: Classifier):
        self.name = name
        self.type = type

```