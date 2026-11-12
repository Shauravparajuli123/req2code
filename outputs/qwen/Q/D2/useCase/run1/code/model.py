from typing import List

class Actor:
    pass

class UseCaseDiagram:
    def __init__(self, name: str):
        self.name = name
        self.actors: List[Actor] = []
        self.use_cases: List[UseCase] = []
        self.extend_relations: List[Extend] = []
        self.include_relations: List[UseCase] = []
        self.case_containers: List[CaseContainer] = []
        self.associations: List[Association] = []
    def has(self, use_case: UseCase, use_case_id: str):
        if use_case_id == 'R13':
            self.actors.append(use_case)
        elif use_case_id == 'R12':
            self.use_cases.append(use_case)
        raise NotImplementedError
    def has(self, extend: Extend, use_case_id: str):
        if use_case_id == 'R12':
            self.extend_relations.append(extend)
        raise NotImplementedError

class UseCase:
    def __init__(self):
        self.includes: List[UseCase] = []
        self.extends: List[Extend] = []
    def includes(self, use_case: UseCase, use_case_id: str):
        if use_case_id == 'R9':
            self.includes.append(use_case)
        raise NotImplementedError
    def extends(self, extend: Extend, use_case_id: str):
        if use_case_id == 'R10':
            self.extends.append(extend)
        raise NotImplementedError

class Extend:
    def __init__(self):
        pass
    def extends(self, use_case: UseCase, use_case_id: str):
        if use_case_id == 'R10':
            pass
        raise NotImplementedError

class CaseContainer:
    def __init__(self):
        pass
    def isOwnedBy(self, use_case: UseCase, use_case_id: str):
        if use_case_id == 'R12':
            pass
        raise NotImplementedError

class Association:
    def __init__(self):
        pass
    def linksTo(self, actor: Actor, use_case_id: str):
        if use_case_id == 'R13':
            pass
        raise NotImplementedError