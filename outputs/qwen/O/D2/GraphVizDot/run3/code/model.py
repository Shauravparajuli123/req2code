class Element:
    pass

class GraphElement(Element):
    def __init__(self, label, parent_graph, z_index):
        self.label = label
        self.parent_graph = parent_graph
        self.z_index = z_index
    def verbObject(self):
        raise NotImplementedError

class Graph:
    def __init__(self, type, dimension):
        self.type = type
        self.dimension = dimension
