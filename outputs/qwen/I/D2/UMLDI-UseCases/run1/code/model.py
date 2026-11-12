from typing import List, Optional

class Instance:
    def __init__(self, classifiers: List[str] = None):
        self.classifiers: List[str] = classifiers if classifiers else []
        self.slots: List[AttributeLink] = []
        self.owned_instances: List[Instance] = []

    def add_owned_instance(self, instance: 'Instance') -> None:
        raise NotImplementedError

    def add_classifier(self, classifier: str) -> None:
        raise NotImplementedError

    def add_slot(self, slot: AttributeLink) -> None:
        raise NotImplementedError

    def get_classifiers(self) -> List[str]:
        raise NotImplementedError

    def get_slots(self) -> List[AttributeLink]:
        raise NotImplementedError

    def get_owned_instances(self) -> List[Instance]:
        raise NotImplementedError

class AttributeLink:
    def __init__(self, instance: Optional[Instance] = None, linkend: Optional['Linkend'] = None):
        self.instance: Optional[Instance] = instance
        self.linkend: Optional[Linkend] = linkend

    def get_instance(self) -> Optional[Instance]:
        raise NotImplementedError

    def get_linkend(self) -> Optional[Linkend]:
        raise NotImplementedError

    def set_instance(self, instance: Instance) -> None:
        raise NotImplementedError

    def set_linkend(self, linkend: Linkend) -> None:
        raise NotImplementedError

class Linkend:
    def __init__(self, link: Optional['Link'] = None, instance: Optional[Instance] = None):
        self.link: Optional['Link'] = link
        self.instance: Optional[Instance] = instance

    def get_link(self) -> Optional['Link']:
        raise NotImplementedError

    def get_instance(self) -> Optional[Instance]:
        raise NotImplementedError

    def set_link(self, link: 'Link') -> None:
        raise NotImplementedError

    def set_instance(self, instance: Instance) -> None:
        raise NotImplementedError

class Link:
    def __init__(self, association: str):
        self.association: str = association
        self.linkends: List[Linkend] = []

    def add_linkend(self, linkend: Linkend) -> None:
        raise NotImplementedError

    def get_linkends(self) -> List[Linkend]:
        raise NotImplementedError

    def get_association(self) -> str:
        raise NotImplementedError

    def set_association(self, association: str) -> None:
        raise NotImplementedError

class ComponentInstance:
    def __init__(self, residents: List[Instance] = None):
        self.residents: List[Instance] = residents if residents else []

    def add_resident(self, resident: Instance) -> None:
        raise NotImplementedError

    def get_residents(self) -> List[Instance]:
        raise NotImplementedError

    def remove_resident(self, resident: Instance) -> None:
        raise NotImplementedError

class NodeInstance:
    def __init__(self, componentinstances: List[ComponentInstance] = None):
        self.componentinstances: List[ComponentInstance] = componentinstances if componentinstances else []

    def add_componentinstance(self, componentinstance: ComponentInstance) -> None:
        raise NotImplementedError

    def get_componentinstances(self) -> List[ComponentInstance]:
        raise NotImplementedError

    def remove_componentinstance(self, componentinstance: ComponentInstance) -> None:
        raise NotImplementedError