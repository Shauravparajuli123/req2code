from typing import List, Union

class CoreModel:
    def __init__(self):
        self.namespaces: List[Namespace] = []
        self.classifiers: List[Classifier] = []
        self.generalizations: List[Generalization] = []

    def contains(self, element: Union[Namespace, Classifier, Generalization]) -> bool:
        raise NotImplementedError

    def has(self, element: Union[Namespace, Classifier, Generalization]) -> bool:
        raise NotImplementedError

    def isLinkedTo(self, element: Union[Namespace, Classifier, Generalization]) -> bool:
        raise NotImplementedError

    def hasPowerTypeRanges(self, classifier: Classifier) -> bool:
        raise NotImplementedError

    def hasFeature(self, feature: Element) -> bool:
        raise NotImplementedError

class Classifier:
    def __init__(self, name: str, powerTypeRanges: List[Generalization], ownerScope: str):
        self.name = name
        self.powerTypeRanges = powerTypeRanges
        self.ownerScope = ownerScope

    def hasPowerTypeRanges(self) -> bool:
        raise NotImplementedError

class Element:
    def __init__(self, name: str, isSpecification: bool, root: bool, abstract: bool):
        self.name = name
        self.isSpecification = isSpecification
        self.root = root
        self.abstract = abstract

    def contains(self, element: Element) -> bool:
        raise NotImplementedError

    def isLinkedTo(self, generalization: Generalization) -> bool:
        raise NotImplementedError

class Generalization:
    def __init__(self, discriminator: str, parent: GeneralizableElement):
        self.discriminator = discriminator
        self.parent = parent

    def isLinkedTo(self, generalizableElement: GeneralizableElement) -> bool:
        raise NotImplementedError

class ModelElement:
    def __init__(self, name: str, namespace: Namespace):
        self.name = name
        self.namespace = namespace

    def contains(self, element: Element) -> bool:
        raise NotImplementedError

    def isLinkedTo(self, generalization: Generalization) -> bool:
        raise NotImplementedError

class Namespace:
    def __init__(self, name: str, modelElements: List[Element]):
        self.name = name
        self.modelElements = modelElements

    def contains(self, element: Element) -> bool:
        raise NotImplementedError