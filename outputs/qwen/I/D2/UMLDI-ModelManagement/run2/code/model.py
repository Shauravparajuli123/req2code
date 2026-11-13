from typing import List, Optional

class ScopeKind:
    pass

class CoreModel:
    def __init__(self):
        self.classifiers: List[Classifier] = []
        self.elements: List[ModelElement] = []
        self.generalizations: List[Generalization] = []
        self.namespaces: List[Namespace] = []

class Element:
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool):
        self.name: str = name
        self.is_specification: bool = is_specification
        self.root: bool = root
        self.abstract: bool = abstract

class Generalization:
    def __init__(self, parent: Optional[GeneralizableElement], discriminator: Optional[str]):
        self.parent: Optional[GeneralizableElement] = parent
        self.discriminator: Optional[str] = discriminator

class GeneralizableElement(Element):
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool, generalization: Optional[Generalization]):
        super().__init__(name, is_specification, root, abstract)
        self.generalization: Optional[Generalization] = generalization

class ModelElement(Element):
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool, namespace: Optional[Namespace]):
        super().__init__(name, is_specification, root, abstract)
        self.namespace: Optional[Namespace] = namespace

class Namespace:
    def __init__(self):
        self.elements: List[ModelElement] = []

class Classifier(Element):
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool, power_type_range: Optional[Generalization]):
        super().__init__(name, is_specification, root, abstract)
        self.power_type_range: Optional[Generalization] = power_type_range

class Feature:
    def __init__(self, owner_scope: ScopeKind, owner: Optional[Classifier]):
        self.owner_scope: ScopeKind = owner_scope
        self.owner: Optional[Classifier] = owner
