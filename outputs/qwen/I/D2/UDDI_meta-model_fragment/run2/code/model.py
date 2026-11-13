from typing import List

class IdentifierBag:
    pass

class Contact:
    pass

class BusinessEntity:
    def __init__(self, identifier_bag: IdentifierBag):
        self.identifier_bag = identifier_bag
    def business_contact(self) -> Contact:
        raise NotImplementedError

class Model:
    pass

class OverviewDocument:
    pass

class PifModel(Model):
    def __init__(self, business_template: Contact):
        self.business_template = business_template

class UtilityClass:
    pass