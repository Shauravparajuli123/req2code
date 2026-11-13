from typing import Optional

class Element:
    pass

class Graph:
    def __init__(self, type: str, dimension: int):
        self.type = type
        self.dimension = dimension

class GraphElement(Element):
    def __init__(self, label: str, z_index: int, parent_graph: Optional[Graph] = None):
        self.label = label
        self.z_index = z_index
        self.parent_graph = parent_graph

class Node(GraphElement):
    def __init__(self, label: str, z_index: int, parent_graph: Optional[Graph], shape: str):
        super().__init__(label, z_index, parent_graph)
        self.shape = shape

class DirectedArc(Element):
    def __init__(self, source_node: Node, target_node: Node, shape: str):
        self.source_node = source_node
        self.target_node = target_node
        self.shape = shape

class Constraint(Element):
    def __init__(self, value: str):
        self.value = value

class SubGraph(Graph):
    pass