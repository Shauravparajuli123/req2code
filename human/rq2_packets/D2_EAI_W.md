# Artefact set D2_EAI_W

## Use cases
(none)

## Class diagram
- FCMSource: attributes []; methods []
- EAISource: attributes []; methods []
- EAIQueue: attributes ['maxLength']; methods []
- EAIResource: attributes []; methods []
- FCMSink: attributes []; methods []
- EAISink: attributes ['resources']; methods []
- EAISink --association--> EAIResource

## Python code
```python
from typing import List

class FCMSource:
    def __init__(self):
        pass
    def method(self):
        raise NotImplementedError

class EAISource(FCMSource):
    def __init__(self):
        super().__init__()
    def method(self):
        raise NotImplementedError

class EAIQueue:
    def __init__(self, max_length: int):
        self.max_length = max_length
    def method(self):
        raise NotImplementedError

class EAIResource:
    def __init__(self):
        pass
    def method(self):
        raise NotImplementedError

class FCMSink:
    def __init__(self):
        pass
    def method(self):
        raise NotImplementedError

class EAISink(FCMSink):
    def __init__(self, resources: List[EAIResource] = None):
        self.resources = resources if resources else []
    def method(self):
        raise NotImplementedError
```