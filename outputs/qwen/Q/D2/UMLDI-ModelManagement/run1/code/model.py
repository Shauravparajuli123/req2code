from typing import List, Union

class CoreModel:
    def __init__(self):
        self.namespaces: List[Namespace] = []
        self.classifiers: List[Classifier] = []
        self.generalizations: List[Generalization] = []
        self.elements: List[ModelElement] = []

    def contains(self, element: Union[Namespace, Classifier, Generalization, ModelElement]) -> bool:
        raise NotImplementedError('Method not implemented')

class Classifier:
    def __init__(self):
        self.powerTypeRanges: List[Generalization] = []

class Element:
    def __init__(self, name: str, isSpecification: bool, isRoot: bool, isAbstract: bool):
        self.name: str = name
        self.isSpecification: bool = isSpecification
        self.isRoot: bool = isRoot
        self.isAbstract: bool = isAbstract

class Generalization:
    def __init__(self, discriminator: str, parent: GeneralizableElement):
        self.discriminator: str = discriminator
        self.parent: GeneralizableElement = parent

class ModelElement:
    def __init__(self, name: str, namespace: Namespace):
        self.name: str = name
        self.namespace: Namespace = namespace

class Namespace:
    def __init__(self, name: str):
        self.name: str = name
        self.elements: List[ModelElement] = []