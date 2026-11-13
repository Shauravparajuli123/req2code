class Expression:
    def __init__(self, instruction):
        self.instruction = instruction

class Inheritance:
    def hasRule(self, rule):
        raise NotImplementedError

class Instruction:
    pass
class Metamodel:
    pass
class Module:
    def __init__(self, name):
        self.name = name
    def hasRule(self, rule):
        raise NotImplementedError
class MtransModel:
    def __init__(self, inheritance_objects, sections, rules, variables):
        self.inheritance_objects = inheritance_objects
        self.sections = sections
        self.rules = rules
        self.variables = variables
    def hasExpression(self, expression):
        raise NotImplementedError
    def hasInheritance(self, inheritance):
        raise NotImplementedError
    def hasInstruction(self, instruction):
        raise NotImplementedError
    def hasMetamodel(self, metamodel):
        raise NotImplementedError
    def hasModule(self, module):
        raise NotImplementedError
    def hasRule(self, rule):
        raise NotImplementedError
    def hasVariable(self, variable):
        raise NotImplementedError
class Rule:
    def __init__(self, name, property, source):
        self.name = name
        self.property = property
        self.source = source
    def hasModule(self, module):
        raise NotImplementedError
    def hasSection(self, section):
        raise NotImplementedError
class Variable:
    def __init__(self, name):
        self.name = name
    def hasRule(self, rule):
        raise NotImplementedError