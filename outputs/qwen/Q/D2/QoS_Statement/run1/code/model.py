from typing import List

class Parameter:
    def __init__(self, value: str):
        self.value = value

class QoSConstraint:
    pass

class QoSStatement:
    def __init__(self):
        pass

class SingleQoSStatement(QoSStatement):
    def __init__(self, constraint: QoSConstraint):
        super().__init__()
        self.constraint = constraint

class CompoundQoSStatement(QoSStatement):
    def __init__(self, statements: List[QoSStatement]):
        super().__init__()
        self.statements = statements
