from abc import ABC

class Class:
    pass

class UtilityClass(Class):
    def __init__(self, identifier: str):
        self.identifier = identifier

class Contact(Class):
    pass

class BusinessTemplate(Class):
    pass

class Model(ABC):
    def __init__(self):
        self.overview_documents = []

class OverviewDocument(Class):
    pass

class PifModel(Model):
    def __init__(self, business_template: BusinessTemplate):
        super().__init__()
        self.business_template = business_template

class IdentifierBag(UtilityClass):
    pass

class BusinessEntity(UtilityClass):
    def __init__(self, business_contact: Contact, identifiers: IdentifierBag):
        super().__init__(identifier=identifiers)
        self.business_contact = business_contact
        self.identifiers = identifiers

    def __str__(self):
        raise NotImplementedError