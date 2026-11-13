from typing import List

class QoSConstraint:
    def __init__(self, qualificationKind: str, value: str):
        self.qualificationKind = qualificationKind
        self.value = value

class Parameter:
    pass

class Domain:
    def __init__(self):
        self.qosConstraints: List[QoSConstraint] = []

class QoSStatement:
    def defineQoSStatement(self):
        raise NotImplementedError

class SingleQoSStatement(QoSStatement):
    def __init__(self, qosConstraint: QoSConstraint):
        self.qosConstraint = qosConstraint

class CompoundQoSStatement(QoSStatement):
    def __init__(self, qosStatements: List[QoSStatement]):
        self.qosStatements = qosStatements