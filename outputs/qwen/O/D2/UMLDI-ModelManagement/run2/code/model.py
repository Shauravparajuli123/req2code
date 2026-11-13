class CoreModel:
    def __init__(self, namespaces=None):
        self.namespaces = namespaces if namespaces else []

class Classifier:
    def __init__(self, powerTypeRanges=None):
        self.powerTypeRanges = powerTypeRanges if powerTypeRanges else []
    def features(self):
        raise NotImplementedError

class Element:
    def __init__(self, name, isSpecification, root, abstract):
        self.name = name
        self.isSpecification = isSpecification
        self.root = root
        self.abstract = abstract

class Generalization:
    def __init__(self, discriminator, parent):
        self.discriminator = discriminator
        self.parent = parent
    def generalizableElements(self):
        raise NotImplementedError

class ModelElement(Element):
    def __init__(self, name, isSpecification):
        super().__init__(name, isSpecification, False, False)

class Namespace:
    def __init__(self, modelElements=None):
        self.modelElements = modelElements if modelElements else []