class Node:
    def __init__(self):
        self.expression = None
        self.inNode = None

    def setExpression(self, expression: Expression):
        self.expression = expression

    def setInNode(self, inNode: Node):
        self.inNode = inNode

    def __str__(self):
        return f'Node(expression={self.expression}, inNode={self.inNode})'

class Expression:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Expression(name={self.name})'

class ConditionalNode(Node):
    def __init__(self):
        super().__init__()
        self.trueNode = None

    def hasTrueNode(self) -> bool:
        return self.trueNode is not None

    def setTrueNode(self, trueNode: Node):
        self.trueNode = trueNode

    def __str__(self):
        return f'ConditionalNode(trueNode={self.trueNode})'