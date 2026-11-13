class LocatedElement:
    def __init__(self, location: str):
        self.location = location

class Label:
    def label(self) -> str:
        raise NotImplementedError

class LabelSuite:
    def label(self) -> str:
        raise NotImplementedError

class Map:
    def __init__(self, mapString: str):
        self.mapString = mapString

class Node:
    def __init__(self, name: str, icon: str):
        self.name = name
        self.icon = icon
        self.labels = []
        self.maps = []
    def label(self) -> str:
        raise NotImplementedError
    def maps(self) -> List[str]:
        raise NotImplementedError

class Outline:
    def __init__(self, extension: str):
        self.extension = extension