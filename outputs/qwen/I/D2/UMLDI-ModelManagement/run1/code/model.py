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
    def __init__(self, parent: Optional[GeneralizableElement], discriminator: Optional[str] = None):
        self.parent: Optional[GeneralizableElement] = parent
        self.discriminator: Optional[str] = discriminator

class GeneralizableElement(Element):
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool, generalization: Optional[Generalization] = None):
        super().__init__(name, is_specification, root, abstract)
        self.generalization: Optional[Generalization] = generalization

class ModelElement(Element):
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool):
        super().__init__(name, is_specification, root, abstract)

class Namespace(ModelElement):
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool, elements: List[ModelElement] = []):
        super().__init__(name, is_specification, root, abstract)
        self.elements: List[ModelElement] = elements

class Classifier(ModelElement):
    def __init__(self, name: str, is_specification: bool, root: bool, abstract: bool, power_type_ranges: List[Generalization] = []):
        super().__init__(name, is_specification, root, abstract)
        self.power_type_ranges: List[Generalization] = power_type_ranges

class Feature:
    def __init__(self, owner_scope: ScopeKind, owner: Optional[Classifier] = None):
        self.owner_scope: ScopeKind = owner_scope
        self.owner: Optional[Classifier] = owner