from typing import List, Optional

class File:
    def __init__(self, name: str):
        self.name = name
    def execute(self):
        raise NotImplementedError('execute method not implemented')

class Dependency:
    def __init__(self, rule: Rule):
        self.rule = rule

class Comment:
    def __init__(self, text: str):
        self.text = text

class Rule:
    def __init__(self):
        pass
    def addDependency(self, dependency: Dependency):
        raise NotImplementedError('addDependency method not implemented')

class Makefile:
    def __init__(self, fileDependencies: List[File], comment: Optional[Comment] = None, rules: List[Rule] = None):
        self.fileDependencies = fileDependencies
        self.comment = comment
        self.rules = rules if rules else []
