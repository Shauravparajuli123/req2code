class QoSStatement:
    def __init__(self):
        pass
    def verbObject(self):
        raise NotImplementedError

class SingleQoSStatement(QoSStatement):
    def __init__(self):
        super().__init__()

class CompoundQoSStatement(QoSStatement):
    def __init__(self):
        super().__init__()

class QoSConstraint:
    def __init__(self):
        pass

class QualificationKind:
    def __init__(self):
        pass