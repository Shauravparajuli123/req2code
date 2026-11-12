from typing import List, Optional

class Node:
    def __init__(self, name: str):
        self.name: str = name

class ExecutionEnvironment:
    pass
class CommunicationLink:
    def __init__(self, name: str, source_node: Optional[Node] = None):
        self.name: str = name
        self.source_node: Optional[Node] = source_node
class Specification:
    def __init__(self):
        self.nodes: List[Node] = []
class Deployment:
    def __init__(self):
        self.execution_environment: Optional[ExecutionEnvironment] = None
        self.communication_links: List[CommunicationLink] = []
        self.nodes: Nodes = Nodes()
class Nodes:
    pass