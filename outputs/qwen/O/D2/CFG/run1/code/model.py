class Node:
    def __init__(self, condition_node=None):
        self.condition_node = condition_node
    def has_expression(self):
        raise NotImplementedError

class Expression:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        raise NotImplementedError

class ConditionalNode:
    def __init__(self):
        pass
