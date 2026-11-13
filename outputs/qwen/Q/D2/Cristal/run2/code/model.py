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
    def hasActivityDefinition(self) -> bool:
        raise NotImplementedError
    def hasCondition(self) -> bool:
        raise NotImplementedError

class ActivityDefinition:
    def hasActCompositeMember(self) -> bool:
        raise NotImplementedError

class Cristal:
    def __init__(self, elementaryActDef: ElementaryActDef, elementaryPartDef: ElementaryPartDef, compositeActDef: CompositeActDef, compositeParDef: List[CompositeParDef], condition: Condition):
        self.elementaryActDef = elementaryActDef
        self.elementaryPartDef = elementaryPartDef
        self.compositeActDef = compositeActDef
        self.compositeParDef = compositeParDef
        self.condition = condition
    def hasActivityDefinition(self) -> bool:
        raise NotImplementedError
    def hasPartDefinition(self) -> bool:
        raise NotImplementedError
    def hasPartCompositeMember(self) -> bool:
        raise NotImplementedError
