from typing import List

class TemplateExpression:
    def __init__(self, boundVariable: str):
        self.boundVariable = boundVariable
    def bindToVariable(self):
        raise NotImplementedError()

class ObjectTemplateExpression(TemplateExpression):
    def __init__(self, propertyTemplateItems: List['PropertyTemplateItem'] = []):
        super().__init__('')
        self.propertyTemplateItems = propertyTemplateItems
    def addPropertyTemplateItem(self, item: 'PropertyTemplateItem'):
        raise NotImplementedError()

class CollectionTemplateExpression(TemplateExpression):
    def __init__(self, oclExpressions: List['OclExpression'] = []):
        super().__init__('')
        self.oclExpressions = oclExpressions
    def addOclExpression(self, expression: 'OclExpression'):
        raise NotImplementedError()

class PropertyTemplateItem:
    def __init__(self, objectContainer: 'ObjectTemplateExpression', referredProperty: 'Property'):
        self.objectContainer = objectContainer
        self.referredProperty = referredProperty
    def setObjectContainer(self, container: 'ObjectTemplateExpression'):
        raise NotImplementedError()
    def setReferredProperty(self, property: 'Property'):
        raise NotImplementedError()

class OclExpression:
    pass

class Property:
    pass