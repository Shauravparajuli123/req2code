class Expression:
    def __init__(self, instruction):
        self.instruction = instruction
    def associateExpressionWithInstruction(self):
        raise NotImplementedError

class Inheritance:
    def __init__(self, name, property, source):
        self.name = name
        self.property = property
        self.source = source
    def associateInheritanceWithModule(self):
        raise NotImplementedError

class Instruction:
    pass

class MetaClass:
    def __init__(self, name):
        self.name = name

class Module:
    def __init__(self, name):
        self.name = name

class MtransModel:
    def __init__(self):
        self.inheritanceObjects = []
        self.sections = []
        self.rules = []
        self.variables = []
        self.metamodels = []
        self.modules = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addVariable(self, variable):
        self.variables.append(variable)

class Section:
    def __init__(self, kind):
        self.kind = kind

class Variable:
    def __init__(self, name, rule):
        self.name = name
        self.rule = rule