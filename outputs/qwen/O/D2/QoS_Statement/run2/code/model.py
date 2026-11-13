class Domain:
    pass

class Parameter:
    def __init__(self, value: str):
        self.value = value

class QoSConstraint:
    pass

class QoSStatement:
    def __init__(self):
        pass
    def CompoundQoSStatement(self) -> CompoundQoSStatement:
        raise NotImplementedError

class SingleQoSStatement(QoSStatement):
    def __init__(self, qos_constraint: QoSConstraint):
        super().__init__()
        self.qos_constraint = qos_constraint

class CompoundQoSStatement(QoSStatement):
    def __init__(self, qos_statements: List[QoSStatement]):
        super().__init__()
        self.qos_statements = qos_statements