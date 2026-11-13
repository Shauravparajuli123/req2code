from typing import List, Optional

class Instance:
    def __init__(self, classifiers: List[str] = []):
        self.classifiers = classifiers
        self.owned_instances: List[Instance] = []
        self.slots: List[AttributeLink] = []

def __init__(self, classifier: str):
    self.classifier = classifier

class AttributeLink:
    def __init__(self, instance: Optional[Instance] = None, linkend: Optional['Linkend'] = None):
        self.instance = instance
        self.linkend = linkend

class Linkend:
    def __init__(self, link: Optional['Link'] = None, instance: Optional[Instance] = None):
        self.link = link
        self.instance = instance

class Link:
    def __init__(self, association: str):
        self.association = association
        self.linkends: List[Linkend] = []

class ComponentInstance(Instance):
    def __init__(self, residents: List[NodeInstance] = []):
        super().__init__()
        self.residents = residents

class NodeInstance(Instance):
    def __init__(self, componentinstances: List[ComponentInstance] = []):
        super().__init__()
        self.componentinstances = componentinstances