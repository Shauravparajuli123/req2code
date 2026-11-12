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
