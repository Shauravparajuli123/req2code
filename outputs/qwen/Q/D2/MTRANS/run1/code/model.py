from typing import List, Optional

class Metaclass:
    pass

class Inheritance:
    def __init__(self, name: str, property: str, source: Metaclass):
        self.name = name
        self.property = property
        self.source = source

class Module:
    def __init__(self, name: str):
        self.name = name

class Rule:
    def __init__(self, moduleName: str, isAbstract: bool, name: str, sections: List[str], inheritances: List[Inheritance], module: Module):
        self.moduleName = moduleName
        self.isAbstract = isAbstract
        self.name = name
        self.sections = sections
        self.inheritances = inheritances
        self.module = module

class Section:
    def __init__(self, kind: str):
        self.kind = kind

class Variable:
    def __init__(self, name: str):
        self.name = name

class Expression:
    def __init__(self, instruction: Instruction):
        self.instruction = instruction

class Instruction:
    pass

class MtransModel:
    def __init__(self, inheritanceObjects: List[Inheritance], sections: List[Section], rules: List[Rule], variables: List[Variable], metamodels: List[str], modules: List[Module]):
        self.inheritanceObjects = inheritanceObjects
        self.sections = sections
        self.rules = rules
        self.variables = variables
        self.metamodels = metamodels
        self.modules = modules
    def verbCreateMTRANSModel(self):
        raise NotImplementedError
    def verbDefineRule(self):
        raise NotImplementedError