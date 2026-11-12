from typing import Optional, List

class Expression:
    def __init__(self, name: str):
        self.name = name

class Node:
    def __init__(self):
        self.expression: Optional[Expression] = None
        self.conditionNode: Optional[Node] = None
        self.in_nodes: List[Node] = []

    def has_expression(self) -> bool:
        raise NotImplementedError()

    def set_condition_node(self, node: Node) -> None:
        raise NotImplementedError()