class Node:
    def __init__(self, name, startLine, endLine, parent=None):
        self.name = name
        self.startLine = startLine
        self.endLine = endLine
        self.parent = parent
    def hasName(self):
        raise NotImplementedError

class Element:
    def __init__(self):
        self.children = []
    def addChild(self, child):
        self.children.append(child)

class XmlFile:
    def __init__(self):
        self.root_element = None
        self.text_elements = []