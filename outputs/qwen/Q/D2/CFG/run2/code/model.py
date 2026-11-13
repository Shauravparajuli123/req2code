from typing import TypeVar, Generic, Type

Expression = TypeVar('Expression', bound='Expression')
Node = TypeVar('Node', bound='Node')
ConditionalNode = TypeVar('ConditionalNode', bound='ConditionalNode')
class Expression(Generic[Expression]): 
    def __init__(self, name: str):
        self.name = name

class Node(Generic[Node]):
    def __init__(self, expression: Expression, in_node: Node = None):
        self.expression: Expression = expression
        self.inNode: Node = in_node

def hasExpression(self) -> Expression:
    raise NotImplementedError

def setInNode(self, in_node: Node) -> None:
    self.inNode = in_node

class ConditionalNode(Node[ConditionalNode]):
    def __init__(self, true_condition: Node, expression: Expression):
        super().__init__(expression)
        self.trueCondition: Node = true_condition

def trueCondition(self) -> Node:
    raise NotImplementedError