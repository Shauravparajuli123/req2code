from typing import List, Optional

class MetaClass:
    pass

class Expression:
    def __init__(self, instruction: Instruction):
        self.instruction = instruction

class Inheritance:
    def __init__(self, rule: Rule):
        self.rule = rule

class Instruction:
    pass

class Module:
    def __init__(self, name: str):
        self.name = name

class MtransModel:
    def __init__(self):
        self.expressions: List[Expression] = []
        self.inheritances: List[Inheritance] = []
        self.instructions: List[Instruction] = []
        self.metamodels: List[MetaClass] = []
        self.modules: List[Module] = []
        self.rules: List[Rule] = []
        self.variables: List[Variable] = []
        self.sections: List[str] = []

class Rule:
    def __init__(self, name: str, module: Module, source: MetaClass):
        self.name = name
        self.module = module
        self.source = source
        self.sections: List[str] = []
        self.abstract: bool = False

class Variable:
    def __init__(self, name: str, rule: Rule):
        self.name = name
        self.rule = rule

class Section:
    def __init__(self, kind: str):
        self.kind = kind
