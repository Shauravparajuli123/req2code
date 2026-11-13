from typing import List

class MetaClass:
    pass

class Module:
    def __init__(self, name: str):
        self.name = name

class Rule:
    def __init__(self, name: str, abstractProperty: bool, source: MetaClass, sections: List[Section], inheritances: List[Inheritance], module: Module):
        self.name = name
        self.abstractProperty = abstractProperty
        self.source = source
        self.sections = sections
        self.inheritances = inheritances
        self.module = module

class Section:
    def __init__(self, kind: str):
        self.kind = kind

class Expression:
    def __init__(self, instruction: Instruction):
        self.instruction = instruction

class Instruction:
    pass

class Variable:
    def __init__(self, name: str):
        self.name = name

class Inheritance:
    def __init__(self, rule: Rule):
        self.rule = rule

class MtransModel:
    def __init__(self, name: str, sections: List[Section], inheritanceObjects: List[Inheritance], expressions: List[Expression], instructions: List[Instruction], metamodels: List[MetaClass], modules: List[Module], rules: List[Rule], variables: List[Variable]):
        self.name = name
        self.sections = sections
        self.inheritanceObjects = inheritanceObjects
        self.expressions = expressions
        self.instructions = instructions
        self.metamodels = metamodels
        self.modules = modules
        self.rules = rules
        self.variables = variables
    def associate(self):
        raise NotImplementedError
    def define(self):
        raise NotImplementedError
    def compose(self):
        raise NotImplementedError