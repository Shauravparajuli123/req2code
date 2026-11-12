from typing import List, Optional

class MetaClass:
    pass

class Expression:
    def __init__(self, instruction: Instruction):
        self.instruction = instruction

class Inheritance:
    def __init__(self, rule: 'Rule', module: Module):
        self.rule = rule
        self.module = module

class Instruction:
    pass

class Module:
    def __init__(self, name: str):
        self.name = name

class MtransModel:
    def __init__(self):
        self.modules: List[Module] = []
        self.rules: List['Rule'] = []
        self.inheritances: List[Inheritance] = []
        self.expressions: List[Expression] = []
        self.sections: List[str] = []
        self.variables: List[Variable] = []

class Variable:
    def __init__(self, name: str, rule: 'Rule'):
        self.name = name
        self.rule = rule

class Rule:
    def __init__(self, abstract: bool, name: str, module: Module, source: MetaClass):
        self.abstract = abstract
        self.name = name
        self.module = module
        self.source = source
        self.sections: List[str] = []
        self.inheritances: List[Inheritance] = []
