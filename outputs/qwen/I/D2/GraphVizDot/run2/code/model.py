from typing import Optional, List

class Element:
    pass

class Graph:
    def __init__(self, type: str, dimension: int, location: Optional[str] = None):
        self.type = type
        self.dimension = dimension
        self.location = location
        self.elements: List[GraphElement] = []

class GraphElement:
    def __init__(self, label: str, z_index: int, parent_graph: Graph):
        self.label = label
        self.z_index = z_index
        self.parent_graph = parent_graph

class GraphObject:
    pass

class Shape:
    pass

class Node(GraphElement):
    def __init__(self, label: str, z_index: int, parent_graph: Graph, shape: Shape):
        super().__init__(label, z_index, parent_graph)
        self.shape = shape

class DirectedArc:
    def __init__(self, source_node: Node, target_node: Node, shape: Shape):
        self.source_node = source_node
        self.target_node = target_node
        self.shape = shape

class Constraint:
    def __init__(self, value: str):
        self.value = value

class SubGraph(Graph):
    pass