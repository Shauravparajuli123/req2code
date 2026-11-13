class IdentifierBag:
    def __init__(self):
        self.identifiers = []

class BusinessEntity:
    def __init__(self):
        self.businessContacts = []
        self.identifierBag = IdentifierBag()
    def addBusinessContact(self, contact):
        raise NotImplementedError
    def removeBusinessContact(self, contact):
        raise NotImplementedError
class Contact:
    pass
class Model:
    def __init__(self):
        self.overviewDocuments = []
    def addOverviewDocument(self, document):
        raise NotImplementedError
    def removeOverviewDocument(self, document):
        raise NotImplementedError
class OverviewDocument:
    pass
class PifModel:
    def __init__(self):
        self.businessTemplates = []
    def addBusinessTemplate(self, template):
        raise NotImplementedError
    def removeBusinessTemplate(self, template):
        raise NotImplementedError