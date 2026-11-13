class Node:
    def __init__(self, name: str):
        self.name = name

class CommunicationLink:
    def __init__(self, name: str, source_node: Node):
        self.name = name
        self.source_node = source_node

class Deployment:
    def __init__(self, execution_environment: ExecutionEnvironment):
        self.nodes = Nodes()
        self.execution_environment = execution_environment
    def add_node(self, node: Node):
        raise NotImplementedError
    def get_nodes(self) -> Nodes:
        raise NotImplementedError
    def set_execution_environment(self, environment: ExecutionEnvironment):
        raise NotImplementedError
    def get_execution_environment(self) -> ExecutionEnvironment:
        raise NotImplementedError

class Nodes:
    def __init__(self):
        pass
    def add_node(self, node: Node):
        raise NotImplementedError
    def get_nodes(self) -> List[Node]:
        raise NotImplementedError

class Specification:
    def __init__(self):
        pass

class ExecutionEnvironment:
    def __init__(self):
        pass