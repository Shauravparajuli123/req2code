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
    def __init__(self, name: str, actors: List[Actor], associations: List[Association]):
        self.name = name
        self.actors = actors
        self.associations = associations
        self.case_containers = []
        self.extends = []
        self.includes = []

    def add_case_container(self, container: CaseContainer):
        self.case_containers.append(container)

    def add_extend(self, extend: Extend):
        self.extends.append(extend)

    def add_include(self, include: Extend):
        self.includes.append(include)