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

class UtilityClass:
    pass

class Model(UtilityClass):
    pass

class OverviewDocument:
    pass

class PifModel(Model):
    def __init__(self, business_template: Contact):
        self.business_template = business_template
    def business_template(self) -> Contact:
        return self.business_template

class Model:
    def __init__(self):
        self.overview_documents: List[OverviewDocument] = []
    def has_overview_documents(self) -> List[OverviewDocument]:
        return self.overview_documents