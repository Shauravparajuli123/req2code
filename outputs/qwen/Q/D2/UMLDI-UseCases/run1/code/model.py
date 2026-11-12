from typing import List, TypeVar, Generic

# Define the types
Classifier = TypeVar('Classifier')
Association = TypeVar('Association')
ComponentInstance = TypeVar('ComponentInstance')
Linkend = TypeVar('Linkend')
NodeInstance = TypeVar('NodeInstance')

# Define the classes
class Instance(Generic[Classifier, Linkend, Association, ComponentInstance, NodeInstance]):
    def __init__(self):
        self.classifiers: List[Classifier] = []
        self.slots: List[AttributeLink] = []

    def add_classifier(self, classifier: Classifier) -> None:
        raise NotImplementedError

    def add_slot(self, slot: AttributeLink) -> None:
        raise NotImplementedError

    def get_classifiers(self) -> List[Classifier]:
        raise NotImplementedError

    def get_slots(self) -> List[AttributeLink]:
        raise NotImplementedError

class AttributeLink(Generic[Instance, Linkend]):
    def __init__(self):
        self.instance: Instance = None
        self.linkend: Linkend = None

    def set_instance(self, instance: Instance) -> None:
        raise NotImplementedError

    def set_linkend(self, linkend: Linkend) -> None:
        raise NotImplementedError

    def get_instance(self) -> Instance:
        raise NotImplementedError

    def get_linkend(self) -> Linkend:
        raise NotImplementedError

class Link(Generic[Association]):
    def __init__(self):
        self.association: Association = None

    def set_association(self, association: Association) -> None:
        raise NotImplementedError

    def get_association(self) -> Association:
        raise NotImplementedError

class Linkend(Generic[Link, Instance]):
    def __init__(self):
        self.link: Link = None
        self.instance: Instance = None

    def set_link(self, link: Link) -> None:
        raise NotImplementedError

    def set_instance(self, instance: Instance) -> None:
        raise NotImplementedError

    def get_link(self) -> Link:
        raise NotImplementedError

    def get_instance(self) -> Instance:
        raise NotImplementedError

class ComponentInstance(Generic[ComponentInstance]):
    def __init__(self):
        self.residents: List[ComponentInstance] = []

    def add_resident(self, resident: ComponentInstance) -> None:
        raise NotImplementedError

    def get_residents(self) -> List[ComponentInstance]:
        raise NotImplementedError

class NodeInstance(Generic[ComponentInstance]):
    def __init__(self):
        self.componentinstances: List[ComponentInstance] = []

    def add_componentinstance(self, componentinstance: ComponentInstance) -> None:
        raise NotImplementedError

    def get_componentinstances(self) -> List[ComponentInstance]:
        raise NotImplementedError