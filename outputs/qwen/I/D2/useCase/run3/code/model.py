from typing import List

class Actor:
    pass
class Association:
    pass
class CaseContainer:
    pass
class Extend:
    def __init__(self, use_cases: List[UseCase]):
        self.use_cases = use_cases
class UseCase:
    pass
class UseCaseDiagram:
    def __init__(self, name: str, actors: List[Actor], associations: List[Association], containers: List[CaseContainer]):
        self.name = name
        self.actors = actors
        self.associations = associations
        self.containers = containers
    def has(self, actor: Actor) -> None:
        raise NotImplementedError
    def has(self, association: Association) -> None:
        raise NotImplementedError
    def has(self, container: CaseContainer) -> None:
        raise NotImplementedError
    def extends(self, use_cases: List[UseCase]) -> None:
        raise NotImplementedError
    def includes(self, use_cases: List[UseCase]) -> None:
        raise NotImplementedError