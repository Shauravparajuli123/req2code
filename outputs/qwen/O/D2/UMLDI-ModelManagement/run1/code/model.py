class CoreModel:
    def __init__(self):
        self.namespaces = []
        self.elements = []

class Element:
    def __init__(self, name, isSpecification, root, abstract):
        self.name = name
        self.isSpecification = isSpecification
        self.root = root
        self.abstract = abstract

class Namespace:
    def __init__(self):
        self.modelElements = []

class Classifier:
    def __init__(self):
        self.powerTypeRanges = []

class Generalization:
    def __init__(self, discriminator, parent):
        self.discriminator = discriminator
        self.parent = parent

# Method stubs

class CoreModel:
    def verbObject(self):
        raise NotImplementedError

class Element:
    def verbObject(self):
        raise NotImplementedError

class Namespace:
    def verbObject(self):
        raise NotImplementedError

class Classifier:
    def verbObject(self):
        raise NotImplementedError

class Generalization:
    def verbObject(self):
        raise NotImplementedError