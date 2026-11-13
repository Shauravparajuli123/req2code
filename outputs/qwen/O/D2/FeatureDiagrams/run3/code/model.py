class Node:
    def __init__(self, description, reference):
        self.description = description
        self.reference = reference
        self.attributes = []
        self.xorgroups = []
        self.orgroups = []

    def addAttribute(self, attribute):
        if isinstance(attribute, Attribute):
            self.attributes.append(attribute)
        else:
            raise ValueError('Attribute must be an instance of Attribute class')

    def addXorgroup(self, xorgroup):
        if isinstance(xorgroup, Xorgroup):
            self.xorgroups.append(xorgroup)
        else:
            raise ValueError('Xorgroup must be an instance of Xorgroup class')

    def addOrgroup(self, orgroup):
        if isinstance(orgroup, Orgroup):
            self.orgroups.append(orgroup)
        else:
            raise ValueError('Orgroup must be an instance of Orgroup class')

class Attribute:
    def __init__(self, description, name, key):
        self.description = description
        self.name = name
        self.key = key

class Child:
    def __init__(self):
        self.nodes = []
        self.orgroups = []
        self.xorgroups = []

    def addNode(self, node):
        if isinstance(node, Node):
            self.nodes.append(node)
        else:
            raise ValueError('Node must be an instance of Node class')

    def addOrgroup(self, orgroup):
        if isinstance(orgroup, Orgroup):
            self.orgroups.append(orgroup)
        else:
            raise ValueError('Orgroup must be an instance of Orgroup class')

    def addXorgroup(self, xorgroup):
        if isinstance(xorgroup, Xorgroup):
            self.xorgroups.append(xorgroup)
        else:
            raise ValueError('Xorgroup must be an instance of Xorgroup class')

class Orgroup:
    def __init__(self, preliminary):
        self.preliminary = preliminary
        self.nodes = []

    def addNode(self, node):
        if isinstance(node, Node):
            self.nodes.append(node)
        else:
            raise ValueError('Node must be an instance of Node class')

class Xorgroup:
    def __init__(self, preliminary):
        self.preliminary = preliminary
        self.nodes = []

    def addNode(self, node):
        if isinstance(node, Node):
            self.nodes.append(node)
        else:
            raise ValueError('Node must be an instance of Node class')