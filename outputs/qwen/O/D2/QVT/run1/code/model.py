class TemplateExp:
    def bindToVariable(self):
        raise NotImplementedError

class CollectionTemplateExpression(TemplateExp):
    def __init__(self):
        self.kind = None
        self.ocl_expressions = []
    def addOclExpression(self, ocl_expression):
        self.ocl_expressions.append(ocl_expression)
    def matchOclExpression(self, ocl_expression):
        raise NotImplementedError
class ObjectTemplateExpression(TemplateExp):
    def __init__(self):
        self.property_template_items = []
    def addPropertyTemplateItem(self, property_template_item):
        self.property_template_items.append(property_template_item)
class OclExpression:
    pass
class Property:
    pass
class PropertyTemplateItem:
    def __init__(self, object_container, referred_property):
        self.object_container = object_container
        self.referred_property = referred_property