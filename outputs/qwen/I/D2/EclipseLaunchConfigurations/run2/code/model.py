from typing import List, Dict, Optional

class MapEntry:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

class ListEntry:
    def __init__(self, value: str):
        self.value = value

class Attribute:
    def __init__(self, key: str):
        self.key = key

class StringAttribute(Attribute):
    def __init__(self, key: str, value: str):
        super().__init__(key)
        self.value = value

class BooleanAttribute(Attribute):
    def __init__(self, key: str, value: bool):
        super().__init__(key)
        self.value = value

class MapAttribute(Attribute):
    def __init__(self, key: str):
        super().__init__(key)
        self.entries: List[MapEntry] = []

class ListAttribute(Attribute):
    def __init__(self, key: str):
        super().__init__(key)
        self.entries: List[ListEntry] = []

class LaunchConfiguration:
    def __init__(self, type: str):
        self.type = type
        self.attributes: List[Attribute] = []
        self.map_attribute: Optional[MapAttribute] = None
        self.list_attribute: Optional[ListAttribute] = None
