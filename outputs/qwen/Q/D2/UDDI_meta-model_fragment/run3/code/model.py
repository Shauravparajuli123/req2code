from typing import List, Optional

class BusinessEntity:
    def __init__(self, businessContact: Optional[Contact] = None, identifierBag: Optional[IdentifierBag] = None):
        self.businessContact = businessContact
        self.identifierBag = identifierBag
    def __str__(self):
        raise NotImplementedError

class Contact:
    def __init__(self):
        pass
    def __str__(self):
        raise NotImplementedError

class Model:
    def __init__(self, businessTemplate: BusinessTemplate):
        self.businessTemplate = businessTemplate
    def __str__(self):
        raise NotImplementedError

class OverviewDocument:
    def __init__(self):
        pass
    def __str__(self):
        raise NotImplementedError

class PifModel(Model):
    def __init__(self, businessTemplate: BusinessTemplate):
        super().__init__(businessTemplate)
    def __str__(self):
        raise NotImplementedError

class UtilityClass:
    def __init__(self, identifier: str):
        self.identifier = identifier
    def __str__(self):
        raise NotImplementedError

class BusinessTemplate:
    def __init__(self):
        pass
    def __str__(self):
        raise NotImplementedError

class IdentifierBag:
    def __init__(self):
        pass
    def __str__(self):
        raise NotImplementedError