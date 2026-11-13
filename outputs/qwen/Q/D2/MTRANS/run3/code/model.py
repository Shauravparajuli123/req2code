from typing import List, Dict, Union

class MetaClass:
    def verbObject(self):
        raise NotImplementedError

class Module:
    def __init__(self, name: str):
        self.name: str = name

class Rule:
    def __init__(self, name: str, property: str, source: MetaClass, module: Module, sections: List[Section], inheritances: List[Inheritance]):
        self.name: str = name
        self.property: str = property
        self.source: MetaClass = source
        self.module: Module = module
        self.sections: List[Section] = sections
        self.inheritances: List[Inheritance] = inheritances

class Inheritance:
    def __init__(self, rule: Rule):
        self.rule: Rule = rule

class Expression:
    def __init__(self, instruction: 'Instruction'):
        self.instruction: Instruction = instruction

class Instruction:
    pass

class Variable:
    def __init__(self, name: str, rule: Rule):
        self.name: str = name
        self.rule: Rule = rule

class Section:
    pass

class Metamodel:
    pass

class MtransModel:
    def __init__(self, modules: List[Module], metamodels: List[Metamodel], rules: List[Rule], inheritances: List[Inheritance], expressions: List[Expression], sections: List[Section], instructions: List[Instruction], variables: List[Variable]):
        self.modules: List[Module] = modules
        self.metamodels: List[Metamodel] = metamodels
        self.rules: List[Rule] = rules
        self.inheritances: List[Inheritance] = inheritances
        self.expressions: List[Expression] = expressions
        self.sections: List[Section] = sections
        self.instructions: List[Instruction] = instructions
        self.variables: List[Variable] = variables