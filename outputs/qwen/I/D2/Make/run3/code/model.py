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
    def __init__(self, rule: 'Rule'):
        self.rule = rule

    def __eq__(self, other: 'RuleDep') -> bool:
        return self.rule == other.rule

    def __hash__(self) -> int:
        return hash(self.rule)

class Rule:
    def __init__(self, dependencies: List[RuleDep]):
        self.dependencies = dependencies

    def add_dependency(self, dep: RuleDep):
        self.dependencies.append(dep)

    def remove_dependency(self, dep: RuleDep):
        self.dependencies.remove(dep)

    def has_dependency(self, dep: RuleDep) -> bool:
        return dep in self.dependencies

    def __eq__(self, other: 'Rule') -> bool:
        return self.dependencies == other.dependencies

    def __hash__(self) -> int:
        return hash(tuple(self.dependencies))

    def __str__(self) -> str:
        return f'Rule({self.dependencies})'

    def __repr__(self) -> str:
        return str(self)

class Makefile:
    def __init__(self, file_dependencies: List[File], comment: Optional[Comment] = None):
        self.file_dependencies = file_dependencies
        self.comment = comment

    def add_file_dependency(self, file: File):
        self.file_dependencies.append(file)

    def remove_file_dependency(self, file: File):
        self.file_dependencies.remove(file)

    def has_file_dependency(self, file: File) -> bool:
        return file in self.file_dependencies

    def __eq__(self) -> bool:
        return self.file_dependencies == self.file_dependencies

    def __hash__(self) -> int:
        return hash(tuple(self.file_dependencies))
