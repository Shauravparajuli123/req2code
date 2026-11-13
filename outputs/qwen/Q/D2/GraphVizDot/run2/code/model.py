class Graph:
    def __init__(self, type: str, dimension: str, location: str):
        self.type = type
        self.dimension = dimension
        self.location = location

    def __str__(self):
        return f'Graph(type={self.type}, dimension={self.dimension}, location={self.location})'


class GraphElement:
    def __init__(self, label: str, zIndex: int, parentGraph: Graph):
        self.label = label
        self.zIndex = zIndex
        self.parentGraph = parentGraph

    def __str__(self):
        return f'GraphElement(label={self.label}, zIndex={self.zIndex}, parentGraph={self.parentGraph})'


class Node(GraphElement):
    def __init__(self, shape: str):
        super().__init__(label=None, zIndex=0, parentGraph=None)
        self.shape = shape

    def __str__(self):
        return f'Node(shape={self.shape})'


class DirectedArc(GraphElement):
    def __init__(self, sourceNode: Node, targetNode: Node, shape: str):
        super().__init__(label=None, zIndex=0, parentGraph=None)
        self.sourceNode = sourceNode
        self.targetNode = targetNode
        self.shape = shape

    def __str__(self):
        return f'DirectedArc(sourceNode={self.sourceNode}, targetNode={self.targetNode}, shape={self.shape})'


class Constraint:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f'Constraint(value={self.value})'