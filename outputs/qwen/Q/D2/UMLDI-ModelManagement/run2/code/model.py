from typing import List, Optional

class CoreModel:
    def __init__(self):
        self.namespaces: List[Namespace] = []
        self.classifiers: List[Classifier] = []
        self.generalizations: List[Generalization] = []
        self.modelElements: List[ModelElement] = []

    def contains(self, element: ModelElement) -> bool:
        raise NotImplementedError('Method not implemented.')

    src: List[str] = ['R1', 'R5', 'R11', 'R12', 'R14']

class Classifier:
    def __init__(self):
        self.powerTypeRanges: List[Generalization] = []

    src: List[str] = ['R12']

class Element:
    def __init__(self, name: str, isSpecification: bool, isRoot: bool, isAbstract: bool):
        self.name: str = name
        self.isSpecification: bool = isSpecification
        self.isRoot: bool = isRoot
        self.isAbstract: bool = isAbstract

    src: List[str] = ['R2', 'R3']

class Generalization:
    def __init__(self, discriminator: str, parent: Optional[GeneralizableElement] = None):
        self.discriminator: str = discriminator
        self.parent: Optional[GeneralizableElement] = parent

    src: List[str] = ['R8', 'R14']

class ModelElement(Element):
    def __init__(self, name: str, namespace: Namespace):
        super().__init__(name, False, False, False)
        self.namespace: Namespace = namespace

    src: List[str] = ['R2', 'R11']

class Namespace:
    def __init__(self):
        self.modelElements: List[ModelElement] = []

    src: List[str] = ['R11']