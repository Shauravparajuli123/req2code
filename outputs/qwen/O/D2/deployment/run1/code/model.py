class Node:
    def __init__(self, name: str):
        self.name = name

class CommunicationLink:
    def __init__(self, name: str, source_node: Node):
        self.name = name
        self.source_node = source_node

class Deployment:
    def __init__(self, execution_environment: ExecutionEnvironment):
        self.execution_environment = execution_environment
        self.nodes = Nodes()
    def add_node(self, node: Node):
        self.nodes.add_node(node)

class Nodes:
    def __init__(self):
        self.nodes = []
    def add_node(self, node: Node):
        self.nodes.append(node)

class Specification:
    pass

class ExecutionEnvironment:
    pass