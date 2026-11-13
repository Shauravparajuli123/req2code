class CoreModel:
    def __init__(self):
        self.namespaces = []
        self.classifiers = []

class Classifier:
    def __init__(self):
        self.powerTypeRanges = []
    def hasOwner(self):
        raise NotImplementedError

class Element:
    def __init__(self, name, isSpecification, root, abstract):
        self.name = name
        self.isSpecification = isSpecification
        self.root = root
        self.abstract = abstract
    def verbObject(self):
        raise NotImplementedError
class Generalization:
    def __init__(self, discriminator, parent):
        self.discriminator = discriminator
        self.parent = parent
    def generalizes(self):
        raise NotImplementedError
class ModelElement(Element):
    def __init__(self, name, isSpecification, root, abstract, namespace):
        super().__init__(name, isSpecification, root, abstract)
        self.namespace = namespace
class Namespace:
    def __init__(self):
        self.elements = []