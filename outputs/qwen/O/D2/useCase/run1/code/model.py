class UseCaseDiagram:
    def __init__(self, name):
        self.name = name
        self.use_cases = []
        self.actors = []
        self.associations = []
        self.containers = []

    def addUseCase(self, use_case):
        raise NotImplementedError

    def addActor(self, actor):
        raise NotImplementedError

    def addAssociation(self, association):
        raise NotImplementedError

class CaseContainer:
    pass
class Extend:
    def extend(self, use_case):
        raise NotImplementedError
class UseCase:
    def include(self, use_case):
        raise NotImplementedError
class Association:
    pass