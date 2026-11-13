from typing import List

class TemplateExp:
    def __init__(self, variable: str):
        self.variable = variable
    def bind_to_variable(self, variable: str):
        raise NotImplementedError

class ObjectTemplateExp(TemplateExp):
    def __init__(self, variable: str):
        super().__init__(variable)
    def has_property_template_items(self) -> List[PropertyTemplateItem]:
        raise NotImplementedError

class CollectionTemplateExpression(TemplateExp):
    def __init__(self, variable: str, collection_kind: str):
        super().__init__(variable)
        self.collection_kind = collection_kind
    def has_ocl_expressions(self) -> List['OclExpression']:
        raise NotImplementedError
    def match_to_ocl_expression(self, ocl_expression: 'OclExpression'):
        raise NotImplementedError

class PropertyTemplateItem:
    def __init__(self, object_container: ObjectTemplateExp, property: Property):
        self.object_container = object_container
        self.property = property
    def has_object_container(self) -> ObjectTemplateExp:
        return self.object_container
    def has_property(self) -> Property:
        return self.property

class OclExpression:
    pass

class Property:
    pass