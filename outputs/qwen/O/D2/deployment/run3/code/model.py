class Node:
    def __init__(self, name: str):
        self.name = name

class CommunicationLink:
    def __init__(self, name: str, source_node: Node):
        self.name = name
        self.source_node = source_node
    def add_node(self, node: Node):
        raise NotImplementedError
    def add_link(self, link: CommunicationLink):
        raise NotImplementedError
class Deployment:
    def __init__(self, execution_environment: ExecutionEnvironment):
        self.execution_environment = execution_environment
        self.nodes = Nodes()
    def add_node(self, node: Node):
        raise NotImplementedError
    def add_link(self, link: CommunicationLink):
        raise NotImplementedError
class Nodes:
    def add_node(self, node: Node):
        raise NotImplementedError
class Specification:
    pass
class ExecutionEnvironment:
    pass