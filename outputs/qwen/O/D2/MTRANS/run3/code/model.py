class Expression:
    def __init__(self, instruction):
        self.instruction = instruction

class Inheritance:
    def hasRule(self):
        raise NotImplementedError

class Instruction:
    pass
class Metamodel:
    pass
class Module:
    def __init__(self, name):
        self.name = name
    def hasRule(self):
        raise NotImplementedError
class MtransModel:
    def __init__(self, inheritance_objects, sections, rules, variables, metamodels, modules):
        self.inheritance_objects = inheritance_objects
        self.sections = sections
        self.rules = rules
        self.variables = variables
        self.metamodels = metamodels
        self.modules = modules
    def hasExpression(self):
        raise NotImplementedError
    def hasInheritance(self):
        raise NotImplementedError
    def hasInstruction(self):
        raise NotImplementedError
    def hasMetamodel(self):
        raise NotImplementedError
    def hasModule(self):
        raise NotImplementedError
    def hasRule(self):
        raise NotImplementedError
    def hasVariable(self):
        raise NotImplementedError
class Rule:
    def __init__(self, name, abstract, source, sections, inheritances):
        self.name = name
        self.abstract = abstract
        self.source = source
        self.sections = sections
        self.inheritances = inheritances
    def hasModule(self):
        raise NotImplementedError
    def hasSource(self):
        raise NotImplementedError
class Variable:
    def __init__(self, name):
        self.name = name
    def hasRule(self):
        raise NotImplementedError