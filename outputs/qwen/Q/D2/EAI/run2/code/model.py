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

class FCMSink:
    def __init__(self):
        pass
    def method(self):
        raise NotImplementedError

class EAISink(FCMSink):
    def __init__(self):
        super().__init__()
    def method(self):
        raise NotImplementedError
    def eai_resources(self) -> List[EAIResource]:
        raise NotImplementedError

class EAIResource:
    def __init__(self):
        pass
    def method(self):
        raise NotImplementedError

class EAIQueue:
    def __init__(self, max_length: int):
        self.max_length = max_length
    def method(self):
        raise NotImplementedError