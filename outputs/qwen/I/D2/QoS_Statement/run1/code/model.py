from typing import List

class QualificationKind:
    pass

class Parameter:
    pass

class QoSConstraint:
    pass

class QoSStatement:
    def __init__(self, compound_qos_statement: 'CompoundQoSStatement'):
        self.compound_qos_statement = compound_qos_statement

class SingleQoSStatement(QoSStatement):
    def __init__(self, qos_constraint: QoSConstraint):
        super().__init__(compound_qos_statement=None)
        self.qos_constraint = qos_constraint

class CompoundQoSStatement(QoSStatement):
    def __init__(self, qos_statements: List[QoSStatement]):
        if len(qos_statements) < 2:
            raise ValueError("A CompoundQoSStatement must contain at least 2 QoSStatements.")
        self.qos_statements = qos_statements
