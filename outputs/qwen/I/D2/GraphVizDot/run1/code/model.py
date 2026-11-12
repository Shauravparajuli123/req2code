from typing import List, Optional

class Element:
    def __init__(self, label: str, z_index: int, parent_graph: Optional['Graph'] = None):
        self.label = label
        self.z_index = z_index
        self.parent_graph = parent_graph

class Graph:
    def __init__(self, type: str, dimension: int, elements: List[Element] = []) -> None:
        self.type = type
        self.dimension = dimension
        self.elements = elements
        self.location = None

class Shape:
    pass

class Node(Element):
    def __init__(self, label: str, z_index: int, shape: Shape, parent_graph: Optional['Graph'] = None):
        super().__init__(label, z_index, parent_graph)
        self.shape = shape

class DirectedArc:
    def __init__(self, source_node: Node, target_node: Node, shape: Shape) -> None:
        self.source_node = source_node
        self.target_node = target_node
        self.shape = shape

class Constraint:
    def __init__(self, value: str) -> None:
        self.value = value

class SubGraph(Graph):
    pass