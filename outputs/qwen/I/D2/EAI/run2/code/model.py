from typing import List, Optional

package EAI:
class EAIResource:
    pass
class FCMSink:
    pass
class EAISink(FCMSink):
    def __init__(self):
        self.resources: List[Optional[EAIResource]] = []
class FCMSource:
    pass
class EAISource(FCMSource):
    def __init__(self):
        self.resources: List[Optional[EAIResource]] = []
class EAIQueue:
    def __init__(self, maxLength: int):
        self.maxLength: int = maxLength
