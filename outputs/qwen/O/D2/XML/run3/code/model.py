class Node:
    def __init__(self, name, startLine, endLine):
        self.name = name
        self.startLine = startLine
        self.endLine = endLine
        self.parent = None

    def setName(self, name):
        raise NotImplementedError

    def setStartLine(self, startLine):
        raise NotImplementedError

    def setEndLine(self, endLine):
        raise NotImplementedError

    def setParent(self, parent):
        raise NotImplementedError

class Element:
    def __init__(self):
        self.children = []

    def addChild(self, child):
        raise NotImplementedError

class XmlFile:
    def __init__(self):
        self.root_element = None
        self.text_elements = []

    def addRootElement(self, root_element):
        raise NotImplementedError

    def addTextElement(self, text_element):
        raise NotImplementedError