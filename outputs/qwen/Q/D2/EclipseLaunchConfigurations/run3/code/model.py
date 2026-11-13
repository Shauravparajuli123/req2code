from typing import List, Union, Mapping, TypeVar, Generic, Optional

String = str
Boolean = bool
MapEntry = TypeVar('MapEntry')
ListEntry = TypeVar('ListEntry')

class Attribute:
    def __init__(self, key: str, value: Union[str, Boolean, Mapping[str, str], List[str]]):
        self.key = key
        self.value = value

    def __str__(self):
        return f'Attribute(key={self.key}, value={self.value})'

class MapEntry:
    def __init__(self, key: str, value: Union[str, Boolean, Mapping[str, str]]):
        self.key = key
        self.value = value

    def __str__(self):
        return f'MapEntry(key={self.key}, value={self.value})'

class Map(Generic[MapEntry]):
    def __init__(self, entries: List[MapEntry] = []) -> None:
        self.entries = entries

    def __str__(self):
        return f'Map(entries={self.entries})'

class ListEntry:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f'ListEntry(value={self.value})'

    class List(Generic[ListEntry]):
        def __init__(self, entries: List[ListEntry] = []) -> None:
            self.entries = entries

        def __str__(self):
            return f'List(entries={self.entries})'

    class LaunchConfiguration:
        def __init__(self, type: str, attributes: List[Attribute] = []) -> None:
            self.type = type
            self.attributes = attributes

        def DefineLaunchConfiguration(self):
            raise NotImplementedError

        def __str__(self):
            return f'LaunchConfiguration(type={self.type}, attributes={self.attributes})'