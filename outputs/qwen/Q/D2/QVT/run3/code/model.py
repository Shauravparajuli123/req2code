from typing import List

class TemplateExp:
    def bindToVariable(self) -> None:
        raise NotImplementedError()

class ObjectTemplateExp(TemplateExp):
    pass

class PropertyTemplateItem:
    def haveObjectContainer(self, objectContainer: ObjectTemplateExp) -> None:
        raise NotImplementedError()
    def haveReferredProperty(self, referredProperty: Property) -> None:
        raise NotImplementedError()

class CollectionTemplateExp(TemplateExp):
    def __init__(self, oclExpressions: List[OclExpression]):
        self.oclExpressions = oclExpressions
    def containPropertyTemplateItems(self) -> None:
        raise NotImplementedError()
    def containOCLExpressions(self) -> None:
        raise NotImplementedError()
    def matchToOCLExpression(self, oclExpression: OclExpression) -> None:
        raise NotImplementedError()

class OclExpression:
    pass

class Property:
    pass