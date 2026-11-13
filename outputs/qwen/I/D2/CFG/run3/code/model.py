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

class Cfg(Node):
    def __init__(self, expression: Expression, true_condition_node: 'Node'):
        super().__init__()
        self.expression = expression
        self.true_condition_node = true_condition_node

    def get_expression(self) -> Expression:
        return self.expression

    def set_true_condition_node(self, node: 'Node'):
        self.true_condition_node = node

    def get_true_condition_node(self) -> 'Node':
        return self.true_condition_node

    def __str__(self):
        return f'Cfg(expression={self.expression}, true_condition_node={self.true_condition_node})'

    def __repr__(self):
        return self.__str__()

    def __bool__(self):
        raise NotImplementedError

    def evaluate(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def __le__(self, other):
        raise NotImplementedError

    def __gt__(self, other):
        raise NotImplementedError

    def __ge__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __sub__(self, other):
        raise NotImplementedError