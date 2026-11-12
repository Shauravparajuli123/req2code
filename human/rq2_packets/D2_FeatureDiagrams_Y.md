# Artefact set D2_FeatureDiagrams_Y

## Use cases
(none)

## Class diagram
- Node: attributes ['description', 'reference']; methods ['verbObject']
- Attribute: attributes ['description', 'name', 'key']; methods []
- Node --association--> Attribute

## Python code
```python
class Node:
    def __init__(self, description, reference):
        self.description = description
        self.reference = reference

class Attribute:
    def __init__(self, description, name, key):
        self.description = description
        self.name = name
        self.key = key

# Example usage
node = Node('description', Attribute('attr description', 'attr name', True))

```