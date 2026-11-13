from typing import List, Optional

class LocatedElement:
    def __init__(self, location: str):
        self.location = location

class Label:
    def __init__(self, label: str):
        self.label = label

class LabelSuite:
    def __init__(self, label: str):
        self.label = label

class Map:
    def __init__(self, map_string: str):
        self.map_string = map_string

class Node(LocatedElement):
    def __init__(self, name: str, icon: str, labels: List[Label], maps: List[Map], label_suites: List[LabelSuite] = None):
        super().__init__(location=None)  # Location is not specified for Node
        self.name = name
        self.icon = icon
        self.labels = labels
        self.maps = maps
        self.label_suites = label_suites if label_suites else []

class Outline(LocatedElement):
    def __init__(self, extension: str, nodes: List[Node]):
        super().__init__(location=None)  # Location is not specified for Outline
        self.extension = extension
        self.nodes = nodes
