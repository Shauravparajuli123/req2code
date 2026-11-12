# Artefact set D2_EAI_Y

## Use cases
(none)

## Class diagram
- EAIResource: attributes []; methods []
- EAIQueue: attributes ['maxLength']; methods []
- FCMSource: attributes []; methods []
- EAIModel: attributes []; methods []
- FCMSink: attributes []; methods []
- EAISink: attributes ['resources']; methods []
- EAISink --association--> EAIResource

## Python code
```python
class EAIResource:
    pass

class EAIQueue:
    def __init__(self):
        self.maxLength = 0

class FCMSource:
    pass

class EAIModel:
    pass

class FCMSink:
    pass

class EAISink:
    def __init__(self):
        self.resources = []
```