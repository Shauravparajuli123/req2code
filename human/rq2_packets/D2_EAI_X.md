# Artefact set D2_EAI_X

## Use cases
(none)

## Class diagram
- FCMSource: attributes []; methods []
- EAISource: attributes []; methods []
- FCMSink: attributes []; methods []
- EAISink: attributes []; methods []
- EAIResource: attributes []; methods []
- EAIQueue: attributes ['maxLength']; methods []
- EAISink --association--> EAIResource
- EAISource --association--> EAIResource

## Python code
```python
from typing import List

# Package EAI

class EAIResource:
    pass

class FCMSink:
    pass

class EAISink(FCMSink):
    def __init__(self):
        self.resources: List[EAIResource] = []

class FCMSource:
    pass

class EAISource(FCMSource):
    def __init__(self):
        self.resources: List[EAIResource] = []

class EAIQueue:
    def __init__(self, max_length: int):
        self.max_length: int = max_length

```