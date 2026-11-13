from typing import List, TypeVar, Generic

T = TypeVar('T')

class Classifier:
    pass

class Linkend:
    def setLink(self, link: 'Link') -> None:
        raise NotImplementedError()
    def setInstance(self, instance: 'Instance') -> None:
        raise NotImplementedError()

class Link(Generic[T]):
    def setAssociation(self, association: T) -> None:
        raise NotImplementedError()

class AttributeLink:
    def __init__(self):
        self.instance: Instance = None
        self.linkend: Linkend = None
    def setInstance(self, instance: Instance) -> None:
        self.instance = instance
    def setLinkend(self, linkend: Linkend) -> None:
        self.linkend = linkend

class Instance:
    def __init__(self):
        self.classifiers: List[Classifier] = []
        self.slots: List[AttributeLink] = []
    def addClassifier(self, classifier: Classifier) -> None:
        self.classifiers.append(classifier)
    def addSlot(self, slot: AttributeLink) -> None:
        self.slots.append(slot)

class ComponentInstance:
    def __init__(self):
        self.residents: List[NodeInstance] = []
    def addResident(self, resident: NodeInstance) -> None:
        self.residents.append(resident)

class NodeInstance:
    def __init__(self):
        self.componentInstances: List[ComponentInstance] = []
    def addComponentInstance(self, componentInstance: ComponentInstance) -> None:
        self.componentInstances.append(componentInstance)