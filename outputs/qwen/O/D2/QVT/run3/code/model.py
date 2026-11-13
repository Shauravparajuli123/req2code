class TemplateExp:
    def __init__(self, expression: str):
        self.expression = expression
    def create_expression(self, expression: str):
        raise NotImplementedError

class CollectionTemplateExpression(TemplateExp):
    def __init__(self, collectionKind: str):
        super().__init__('CollectionTemplateExpression')
        self.collectionKind = collectionKind
        self.oclExpressions = []
    def add_ocl_expression(self, ocl_expression: OclExpression):
        self.oclExpressions.append(ocl_expression)

class ObjectTemplateExpression(TemplateExp):
    def __init__(self):
        super().__init__('ObjectTemplateExpression')
        self.propertyTemplateItems = []
    def add_property_template_item(self, property_template_item: PropertyTemplateItem):
        self.propertyTemplateItems.append(property_template_item)

class OclExpression:
    pass

class Property:
    pass

class PropertyTemplateItem:
    def __init__(self, objectContainer: ObjectTemplateExpression, referredProperty: Property):
        self.objectContainer = objectContainer
        self.referredProperty = referredProperty