from abc import ABC, abstractmethod

class Parameter:
    pass

class QoSConstraint:
    pass

class QualificationKind:
    pass

class QoSStatement(ABC):
    def __init__(self, compound_qos_statement: 'CompoundQoSStatement'):
        self.compound_qos_statement = compound_qos_statement

    @abstractmethod
define_qos_constraint(self) -> QoSConstraint:
        pass

class SingleQoSStatement(QoSStatement):
    def __init__(self, qos_constraint: QoSConstraint):
        super().__init__(compound_qos_statement=None)
        self.qos_constraint = qos_constraint

    def define_qos_constraint(self) -> QoSConstraint:
        return self.qos_constraint

class CompoundQoSStatement(QoSStatement):
    def __init__(self, qos_statements: list[QoSStatement]):
        super().__init__(compound_qos_statement=None)
        if len(qos_statements) < 2:
            raise ValueError("A CompoundQoSStatement must contain at least 2 QoSStatements.")
        self.qos_statements = qos_statements

    def define_qos_constraint(self) -> QoSConstraint:
        # Implement logic to define a QoSConstraint based on the compound statements
        raise NotImplementedError()
