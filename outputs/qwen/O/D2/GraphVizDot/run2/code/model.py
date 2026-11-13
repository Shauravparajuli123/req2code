class Element:
    def __init__(self, label, z_index):
        self.label = label
        self.z_index = z_index
    def define(self):
        raise NotImplementedError

class Graph:
    def __init__(self, type, dimension, location):
        self.type = type
        self.dimension = dimension
        self.location = location

class GraphElement(Element):
    def __init__(self, label, z_index, parent_graph):
        super().__init__(label, z_index)
        self.parent_graph = parent_graph
    def get_parent_graph(self):
        raise NotImplementedError

class Node(GraphElement):
    def __init__(self, label, z_index, parent_graph, shape):
        super().__init__(label, z_index, parent_graph)
        self.shape = shape

class DirectedArc:
    def __init__(self, source_node, target_node, shape):
        self.source_node = source_node
        self.target_node = target_node
        self.shape = shape

class Constraint:
    def __init__(self, value):
        self.value = value

class SubGraph:
    pass