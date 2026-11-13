from typing import List, String

class File:
    def __init__(self, name: String):
        self.name = name
    # src: R1

class Element:
    def __init__(self, name: String):
        self.name = name
    # src: R2
class Macro:
    def __init__(self, value: String):
        self.value = value
    # src: R4
class Comment:
    def __init__(self, text: String):
        self.text = text
    # src: R10
class Dependency:
    def __init__(self, name: String):
        self.name = name
    # src: R9
class RuleDep:
    def __init__(self):
        pass
    # src: R8
class Rule:
    def __init__(self):
        self.dependencies = []
    # src: R7, R12
class ShellLine:
    def __init__(self, rule: Rule):
        self.rule = rule
    # src: R12
class Makefile:
    def __init__(self):
        self.fileDependencies = []
        self.comment = None
        self.rules = []
    # src: R9, R11