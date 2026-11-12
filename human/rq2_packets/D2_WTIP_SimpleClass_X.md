# Artefact set D2_WTIP_SimpleClass_X

## Use cases
- DefineClassifier (actor: User)

## Class diagram
- Classifier: attributes ['name']; methods []
- PrimitiveDataType: attributes ['name']; methods []
- TypeString: attributes ['name']; methods []
- Association: attributes ['name', 'src']; methods ['verbObject']
- SimpleClass: attributes ['parent', 'association', 'attribute']; methods []
- PrimitiveDataType --generalization--> Classifier
- TypeString --generalization--> Classifier
- SimpleClass --association--> Association

## Python code
```python
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
    def __init__(self, name: str, src: Classifier):
        self.name = name
        self.src = src

class SimpleClass:
    def __init__(self, parent: Classifier, association: Association, attribute: TypeString):
        self.parent = parent
        self.association = association
        self.attribute = attribute

    def verbObject(self):
        raise NotImplementedError
```