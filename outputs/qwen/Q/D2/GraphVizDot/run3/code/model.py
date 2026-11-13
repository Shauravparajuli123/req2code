class Element:
    def __init__(self, location: str):
        self.location = location


class GraphElement(Element):
    def __init__(self, label: str, zIndex: int, parentGraph: Graph):
        super().__init__(location="")
        self.label = label
        self.zIndex = zIndex
        self.parentGraph = parentGraph


class Graph:
    def __init__(self, type: str, dimension: str):
        self.type = type
        self.dimension = dimension
        self.graph_elements = []

    def add_element(self, element: GraphElement):
        raise NotImplementedError

if __name__ == '__main__':
    pass