from typing import List

class TemplateExp:
    def bindToVariable(self) -> None:
        raise NotImplementedError()

class CollectionTemplateExp:
    def __init__(self):
        self.oclExpressions: List[OclExpression] = []
    def containPropertyTemplateItems(self) -> None:
        raise NotImplementedError()
    def containObjectTemplateExp(self) -> None:
        raise NotImplementedError()

class PropertyTemplateItem:
    def __init__(self, objectContainer: ObjectTemplateExp, referredProperty: Property):
        self.objectContainer: ObjectTemplateExp = objectContainer
        self.referredProperty: Property = referredProperty
    def referProperty(self) -> None:
        raise NotImplementedError()

class ObjectTemplateExp:
    pass

class OclExpression:
    pass

class Property:
    pass