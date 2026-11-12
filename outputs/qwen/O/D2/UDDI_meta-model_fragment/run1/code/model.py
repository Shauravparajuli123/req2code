class IdentifierBag:
    def __init__(self):
        self.identifiers = []

class BusinessEntity:
    def __init__(self, identifiers):
        self.identifiers = identifiers
        self.businessContacts = []
    def addBusinessContact(self, contact):
        self.businessContacts.append(contact)

class Contact:
    def __init__(self, contactDetails):
        self.contactDetails = contactDetails
class Model:
    def __init__(self):
        self.overviewDocuments = []
class OverviewDocument:
    def __init__(self, documentContent):
        self.documentContent = documentContent
class PifModel:
    def __init__(self, businessTemplates):
        self.businessTemplates = businessTemplates