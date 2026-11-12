from typing import List, Optional

class Macro:
    def __init__(self, value: str):
        self.value = value

class Comment:
    def __init__(self, text: str):
        self.text = text

class Element:
    def __init__(self, name: str):
        self.name = name

class Dependency:
    pass

class File:
    def __init__(self, name: str):
        self.name = name

class RuleDep:
    def __init__(self, rule: 'Rule', dependency: 'Dependency'):
        self.rule = rule
        self.dependency = dependency

class Rule:
    def __init__(self, dependencies: List[RuleDep]):
        self.dependencies = dependencies

    def add_dependency(self, dependency: RuleDep):
        raise NotImplementedError

    def get_dependencies(self) -> List[RuleDep]:
        raise NotImplementedError

class Makefile:
    def __init__(self, file_dependencies: List[File], comment: Optional[Comment] = None):
        self.file_dependencies = file_dependencies
        self.comment = comment

    def add_file_dependency(self, file: File):
        raise NotImplementedError

    def get_file_dependencies(self) -> List[File]:
        raise NotImplementedError

    def add_comment(self, comment: Comment):
        raise NotImplementedError

    def get_comment(self) -> Optional[Comment]:
        raise NotImplementedError

    def add_rule(self, rule: Rule):
        raise NotImplementedError

    def get_rules(self) -> List[Rule]:
        raise NotImplementedError

    def add_shell_line(self, shell_line: str):
        raise NotImplementedError

    def get_shell_lines(self) -> List[str]:
        raise NotImplementedError
