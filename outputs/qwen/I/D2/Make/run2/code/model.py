from typing import List, Optional

class Macro:
    def __init__(self, value: str):
        self.value = value
    def __str__(self):
        raise NotImplementedError

class Comment:
    def __init__(self, text: str):
        self.text = text
    def __str__(self):
        raise NotImplementedError

class Element:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        raise NotImplementedError

class Dependency:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        raise NotImplementedError

class File:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        raise NotImplementedError

class RuleDep:
    def __init__(self, rule: 'Rule', dependency: Dependency):
        self.rule = rule
        self.dependency = dependency
    def __str__(self):
        raise NotImplementedError

class Rule:
    def __init__(self, dependencies: List[RuleDep]):
        self.dependencies = dependencies
    def __str__(self):
        raise NotImplementedError

class Makefile:
    def __init__(self, file_dependencies: List[File], comment: Optional[Comment] = None):
        self.file_dependencies = file_dependencies
        self.comment = comment
    def __str__(self):
        raise NotImplementedError

class ShellLine:
    def __init__(self, rule: Rule):
        self.rule = rule
    def __str__(self):
        raise NotImplementedError

class MakeModel:
    def __init__(self, shell_lines: List[ShellLine]):
        self.shell_lines = shell_lines
    def __str__(self):
        raise NotImplementedError