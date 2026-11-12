from typing import List, Optional

class Dependency:
    def __init__(self, name: str):
        self.name = name

class Comment:
    def __init__(self, text: str):
        self.text = text

class RuleDep:
    def __init__(self, targetRule: Rule):
        self.targetRule = targetRule

class Rule:
    def __init__(self):
        self.dependencies: List[RuleDep] = []
    def addDependency(self, dep: RuleDep) -> None:
        raise NotImplementedError

class Makefile:
    def __init__(self):
        self.fileDependencies: List[Dependency] = []
        self.comment: Optional[Comment] = None
    def addFileDependency(self, dep: Dependency) -> None:
        raise NotImplementedError
    def addRule(self, rule: Rule) -> None:
        raise NotImplementedError