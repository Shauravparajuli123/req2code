from typing import List, Optional

class Instance:
    def __init__(self, classifiers: List[str], slots: Optional[List[AttributeLink]] = None):
        self.classifiers = classifiers
        self.slots = slots if slots else []

    def association(self):
        raise NotImplementedError

    src = ['R1', 'R8', 'R9']

class AttributeLink:
    def __init__(self, instance: Instance, linkend: Optional[Linkend] = None):
        self.instance = instance
        self.linkend = linkend

    src = ['R10', 'R11']

class Link:
    def __init__(self):
        pass

    def association(self):
        raise NotImplementedError

    src = ['R12']

class Linkend:
    def __init__(self, link: Link, instance: Instance):
        self.link = link
        self.instance = instance

    src = ['R13', 'R14']

class ComponentInstance:
    def __init__(self, residents: Optional[List[NodeInstance]] = None):
        self.residents = residents if residents else []

    src = ['R15']

class NodeInstance:
    def __init__(self, componentinstances: Optional[List[ComponentInstance]] = None):
        self.componentinstances = componentinstances if componentinstances else []

    src = ['R16']