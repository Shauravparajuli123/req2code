class TemplateExp:
    def __init__(self, boundVariable):
        self.boundVariable = boundVariable
    def bindTemplateExpressionToVariable(self):
        raise NotImplementedError

class CollectionTemplateExpression(TemplateExp):
    def __init__(self, collectionKind):
        super().__init__(boundVariable=None)
        self.collectionKind = collectionKind
        self.oclExpressions = []
    def addOclExpression(self, oclExpression):
        self.oclExpressions.append(oclExpression)

class ObjectTemplateExpression(TemplateExp):
    def __init__(self):
        super().__init__(boundVariable=None)
        self.propertyTemplateItems = []
    def addPropertyTemplateItem(self, propertyTemplateItem):
        self.propertyTemplateItems.append(propertyTemplateItem)

class OclExpression:
    pass

class Property:
    pass

class PropertyTemplateItem:
    def __init__(self, objectContainer, referredProperty):
        self.objectContainer = objectContainer
        self.referredProperty = referredProperty
