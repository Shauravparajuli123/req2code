from typing import List

class QualificationKind:
    pass

class QoSConstraint:
    def __init__(self, qualificationKind: QualificationKind, value: str):
        self.qualificationKind = qualificationKind
        self.value = value

class QoSStatement:
    def defineQoSStatement(self):
        raise NotImplementedError()

class SingleQoSStatement(QoSStatement):
    def __init__(self, qosConstraint: QoSConstraint):
        self.qosConstraint = qosConstraint

class CompoundQoSStatement(QoSStatement):
    def __init__(self, qosStatements: List[QoSStatement]):
        self.qosStatements = qosStatements