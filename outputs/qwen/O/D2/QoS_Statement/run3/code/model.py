class Domain:
    pass

class QoSConstraint:
    def __init__(self, qualification: QualificationKind):
        self.qualification = qualification

class Parameter:
    def __init__(self, value: str):
        self.value = value

class QoSStatement:
    def __init__(self):
        pass
    def compoundQoSStatement(self) -> CompoundQoSStatement:
        raise NotImplementedError

class SingleQoSStatement:
    def __init__(self, qosConstraint: QoSConstraint):
        self.qosConstraint = qosConstraint

class CompoundQoSStatement:
    def __init__(self, qosStatements: List[QoSStatement]):
        self.qosStatements = qosStatements