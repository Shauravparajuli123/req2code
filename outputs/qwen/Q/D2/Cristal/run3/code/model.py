from typing import List

class Condition:
    pass

class ElementaryActDef:
    pass

class ElementaryPartDef:
    pass

class CompositeActDef:
    pass

class CompositeParDef:
    pass

class ActCompositeMember:
    pass

class ActivityDefinition:
    pass

class PartCompositeMember:
    pass

class PartDefinitionNode:
    pass

class Cristal:
    def __init__(self, elementaryActDef: ElementaryActDef, elementaryPartDef: ElementaryPartDef, compositeActDef: CompositeActDef, compositeParDef: List[CompositeParDef], condition: List[Condition] = None):
        self.elementaryActDef = elementaryActDef
        self.elementaryPartDef = elementaryPartDef
        self.compositeActDef = compositeActDef
        self.compositeParDef = compositeParDef
        self.condition = condition if condition else []

class ActCompositeMember:
    pass

class ActivityDefinition:
    pass

class PartCompositeMember:
    pass

class PartDefinitionNode:
    pass