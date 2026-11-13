from typing import List

class Contact:
    pass

class IdentifierBag:
    pass

class BusinessEntity:
    def __init__(self):
        self.businessContacts: List[Contact] = []
        self.identifiers: IdentifierBag = IdentifierBag()

class Model:
    def __init__(self):
        self.overviewDocuments: List[OverviewDocument] = []

class OverviewDocument:
    pass
class PifModel:
    def __init__(self):
        self.businessTemplates: List[Contact] = []
