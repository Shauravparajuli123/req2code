class Element:
    def __init__(self, label: str, parent: Graph, z_index: int):
        self.label = label
        self.parent = parent
        self.z_index = z_index

    def define(self):
        raise NotImplementedError

class Graph:
    def __init__(self, type: str, dimension: int, location: str):
        self.type = type
        self.dimension = dimension
        self.location = location
        self.elements = []

class Shape:
    pass