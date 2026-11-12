from typing import List

class GraphElement:
    def __init__(self, label: str, zIndex: int, parentGraph: 'Graph'):
        self.label = label
        self.zIndex = zIndex
        self.parentGraph = parentGraph
    def DefineGraphElement(self) -> None:
        raise NotImplementedError
    def DefineNode(self) -> None:
        raise NotImplementedError
    def DefineDirectedArc(self) -> None:
        raise NotImplementedError

class Graph:
    def __init__(self, type: str, dimension: int):
        self.type = type
        self.dimension = dimension
    def DefineGraph(self) -> None:
        raise NotImplementedError

class Node:
    def __init__(self, shape: str):
        self.shape = shape
    def DefineNode(self) -> None:
        raise NotImplementedError

class DirectedArc:
    def __init__(self, sourceNode: 'Node', targetNode: 'Node', shape: str):
        self.sourceNode = sourceNode
        self.targetNode = targetNode
        self.shape = shape
    def DefineDirectedArc(self) -> None:
        raise NotImplementedError

class Constraint:
    def __init__(self, value: str):
        self.value = value
    def DefineConstraint(self) -> None:
        raise NotImplementedError