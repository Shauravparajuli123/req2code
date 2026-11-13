class Node:
    def __init__(self, description, reference):
        self.description = description
        self.reference = reference
        self.attributes = []
        self.orgroups = []
        self.xorgroups = []

    def addAttribute(self, attribute):
        if isinstance(attribute, Attribute):
            self.attributes.append(attribute)
        else:
            raise ValueError('Attribute must be an instance of Attribute class')

    def addChild(self, child):
        if isinstance(child, Node):
            self.orgroups.append(child)
        else:
            raise ValueError('Child must be an instance of Node class')

    def addXORGroup(self, xorgroup):
        if isinstance(xorgroup, Xorgroup):
            self.xorgroups.append(xorgroup)
        else:
            raise ValueError('Xorgroup must be an instance of Xorgroup class')

    def addORGroup(self, orgroup):
        if isinstance(orgroup, Orgroup):
            self.orgroups.append(orgroup)
        else:
            raise ValueError('Orgroup must be an instance of Orgroup class')

class Attribute:
    def __init__(self, description, name, key):
        self.description = description
        self.name = name
        self.key = key

class Orgroup:
    def __init__(self, preliminary):
        self.preliminary = preliminary

class Xorgroup:
    def __init__(self, preliminary):
        self.preliminary = preliminary