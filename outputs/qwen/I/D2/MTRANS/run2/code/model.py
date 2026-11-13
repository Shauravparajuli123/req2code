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
        self.modules: List[Module] = []
        self.rules: List[Rule] = []
        self.inheritances: List[Inheritance] = []
        self.expressions: List[Expression] = []
        self.sections: List[str] = []
        self.variables: List[Variable] = []

class Rule:
    def __init__(self, name: str, abstract: bool, module: Module, source: MetaClass):
        self.name = name
        self.abstract = abstract
        self.module = module
        self.source = source
        self.sections: List[str] = []

class Variable:
    def __init__(self, name: str, rule: Rule):
        self.name = name
        self.rule = rule
