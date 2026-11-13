from typing import List

class Actor:
    pass
class Association:
    pass
class CaseContainer:
    pass
class Extend:
    def __init__(self, use_cases: List['UseCase']):
        self.use_cases = use_cases
class UseCase:
    pass
class UseCaseDiagram:
    def __init__(self, name: str):
        self.name = name
        self.case_containers = []
        self.actors = []
        self.associations = []

    def has(self, actor: Actor) -> None:
        raise NotImplementedError

    def has(self, association: Association) -> None:
        raise NotImplementedError

class UseCaseDiagram:
    def __init__(self, name: str):
        self.name = name
        self.case_containers = []
        self.actors = []
        self.associations = []

    def has(self, actor: Actor) -> None:
        self.actors.append(actor)

    def has(self, association: Association) -> None:
        self.associations.append(association)
