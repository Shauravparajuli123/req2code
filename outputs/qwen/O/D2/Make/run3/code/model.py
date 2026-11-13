class Comment:
    def __init__(self, text):
        self.text = text

class Dependency:
    pass
class Element:
    def __init__(self, name):
        self.name = name
class File:
    def __init__(self, name):
        self.name = name
class Makefile:
    def __init__(self):
        self.file_dependencies = []
        self.comment = None
        self.rules = []
    def add_file_dependency(self, dependency):
        self.file_dependencies.append(dependency)
    def add_rule(self, rule):
        self.rules.append(rule)
class Rule:
    def __init__(self):
        self.dependencies = []
    def add_dependency(self, dependency):
        self.dependencies.append(dependency)
class RuleDep(Dependency):
    def __init__(self, value):
        self.value = value