class UseCaseDiagram:
    def __init__(self, name: str):
        self.name = name
        self.actors = []
        self.useCases = []
        self.extends = []
        self.includes = []
        self.containers = []
        self.associations = []

    def addActor(self, actor: Actor):
        self.actors.append(actor)
        raise NotImplementedError

    def addUseCase(self, use_case: UseCase):
        self.useCases.append(use_case)
        raise NotImplementedError

    def addExtend(self, extend: Extend):
        self.extends.append(extend)
        raise NotImplementedError

    def addInclude(self, include: UseCase):
        self.includes.append(include)
        raise NotImplementedError

    def addContainer(self, container: CaseContainer):
        self.containers.append(container)
        raise NotImplementedError

    def addAssociation(self, association: Association):
        self.associations.append(association)
        raise NotImplementedError

class Actor:
    pass
class Extend:
    pass
class UseCase:
    pass
class CaseContainer:
    pass
class Association:
    pass