from typing import List, Dict, Optional

class Attribute:
    def __init__(self, key: str):
        self.key = key
        self.value: Optional[str | bool] = None

class MapEntry:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

class ListEntry:
    def __init__(self, value: str):
        self.value = value

class LaunchConfiguration:
    def __init__(self, type_: str):
        self.type = type_
        self.attributes: List[Attribute] = []
        self.map_attribute: Optional[MapAttribute] = None
        self.list_attribute: Optional[ListAttribute] = None

class MapAttribute:
    def __init__(self):
        self.entries: List[MapEntry] = []

class ListAttribute:
    def __init__(self):
        self.entries: List[ListEntry] = []