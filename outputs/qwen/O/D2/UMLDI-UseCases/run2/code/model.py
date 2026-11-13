class Instance:
    def __init__(self):
        self.classifiers = []
        self.slots = []
    def addClassifier(self, classifier):
        raise NotImplementedError
    def addSlot(self, slot):
        raise NotImplementedError
class AttributeLink:
    def __init__(self):
        self.instance = None
        self.linkend = None
    def setInstance(self, instance):
        raise NotImplementedError
    def setLinkend(self, linkend):
        raise NotImplementedError
class Linkend:
    def __init__(self):
        self.link = None
        self.instance = None
    def setLink(self, link):
        raise NotImplementedError
    def setInstance(self, instance):
        raise NotImplementedError
class Link:
    def __init__(self):
        self.association = None
    def setAssociation(self, association):
        raise NotImplementedError
class ComponentInstance:
    def __init__(self):
        self.residents = []
    def addResident(self, resident):
        raise NotImplementedError
class NodeInstance:
    def __init__(self):
        self.componentinstances = []
    def addComponentInstance(self, componentinstance):
        raise NotImplementedError