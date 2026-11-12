from abc import ABC

class Node(ABC):
    def __init__(self, in_node: 'Node' = None):
        self.in_node = in_node

    def set_in_node(self, node: 'Node'):
        self.in_node = node

    def get_in_node(self) -> 'Node':
        return self.in_node

    def __str__(self):
        return f'Node(in_node={self.in_node})'

    def __repr__(self):
        return self.__str__()

class Expression:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Expression(name={self.name})'

    def __repr__(self):
        return self.__str__()

    def get_name(self) -> str:
        return self.name

class Cfg(Node):
    def __init__(self, expression: Expression, condition_node: 'ConditionalNode' = None):
        super().__init__()
        self.expression = expression
        self.condition_node = condition_node

    def set_expression(self, expression: Expression):
        self.expression = expression

    def get_expression(self) -> Expression:
        return self.expression

    def set_condition_node(self, condition_node: 'ConditionalNode'):
        self.condition_node = condition_node

    def get_condition_node(self) -> 'ConditionalNode':
        return self.condition_node

    def __str__(self):
        return f'Cfg(expression={self.expression}, condition_node={self.condition_node})'

    def __repr__(self):
        return self.__str__()

class ConditionalNode(Node):
    def __init__(self, true_condition_node: 'ConditionalNode' = None):
        super().__init__()
        self.true_condition_node = true_condition_node

    def set_true_condition_node(self, true_condition_node: 'ConditionalNode'):
        self.true_condition_node = true_condition_node

    def get_true_condition_node(self) -> 'ConditionalNode':
        return self.true_condition_node

    def __str__(self):
        return f'ConditionalNode(true_condition_node={self.true_condition_node})'

    def __repr__(self):
        return self.__str__()