from typing import List, Union, Optional

class Attribute:
    def __init__(self, key: str):
        self.key = key
    def __str__(self):
        return self.key
    def __repr__(self):
        return f'Attribute(key={self.key})'

class StringAttribute(Attribute):
    def __init__(self, key: str, value: str):
        super().__init__(key)
        self.value = value
    def __str__(self):
        return f'{self.key}={self.value}'
    def __repr__(self):
        return f'StringAttribute(key={self.key}, value={self.value})'

class BooleanAttribute(Attribute):
    def __init__(self, key: str, value: bool):
        super().__init__(key)
        self.value = value
    def __str__(self):
        return f'{self.key}={self.value}'
    def __repr__(self):
        return f'BooleanAttribute(key={self.key}, value={self.value})'

class MapEntry:
    def __init__(self, key: str, value: Attribute):
        self.key = key
        self.value = value
    def __str__(self):
        return f'{self.key}={self.value}'
    def __repr__(self):
        return f'MapEntry(key={self.key}, value={self.value})'

class MapAttribute(Attribute):
    def __init__(self, key: str, entries: List[MapEntry]):
        super().__init__(key)
        self.entries = entries
    def __str__(self):
        return f'{self.key}={self.entries}'
    def __repr__(self):
        return f'MapAttribute(key={self.key}, entries={self.entries})'

class ListEntry:
    def __init__(self, value: str):
        self.value = value
    def __str__(self):
        return self.value
    def __repr__(self):
        return f'ListEntry(value={self.value})'

class ListAttribute(Attribute):
    def __init__(self, key: str, entries: List[ListEntry]):
        super().__init__(key)
        self.entries = entries
    def __str__(self):
        return f'{self.key}={self.entries}'
    def __repr__(self):
        return f'ListAttribute(key={self.key}, entries={self.entries})'

class LaunchConfiguration:
    def __init__(self, type: str, attributes: List[Attribute] = None):
        self.type = type
        self.attributes = attributes if attributes else []
    def add_attribute(self, attribute: Attribute):
        self.attributes.append(attribute)
    def __str__(self):
        return f'Type={self.type}, Attributes={self.attributes}'
    def __repr__(self):
        return f'LaunchConfiguration(type={self.type}, attributes={self.attributes})'
