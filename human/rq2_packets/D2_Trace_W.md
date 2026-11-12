# Artefact set D2_Trace_W

## Use cases
- CreateTrace (actor: User)

## Class diagram
- Trace: attributes ['name']; methods []
- Level: attributes []; methods []
- Call: attributes ['methodName', 'databaseRows']; methods ['verbObject']
- Trace --association--> Level
- Level --association--> Trace
- Call --association--> Level

## Python code
```python
class Trace:
    def __init__(self, name):
        self.name = name

class Level:
    def __init__(self, trace):
        self.trace = trace

class Call:
    def __init__(self, methodName, databaseRows):
        self.methodName = methodName
        self.databaseRows = databaseRows
    def verbObject(self):
        raise NotImplementedError
```