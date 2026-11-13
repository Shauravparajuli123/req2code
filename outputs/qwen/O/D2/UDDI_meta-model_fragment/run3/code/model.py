class IdentifierBag:
    def __init__(self):
        self.identifiers = []

class BusinessEntity:
    def __init__(self, identifier_bag, business_contact=None):
        self.identifierBag = identifier_bag
        self.businessContact = business_contact
    def defineBusinessEntity(self):
        raise NotImplementedError

class Contact:
    pass
class Model:
    def __init__(self):
        self.businessTemplates = []
class OverviewDocument:
    pass
class PifModel(Model):
    def __init__(self):
        super().__init__()
    def addBusinessTemplate(self, business_template):
        raise NotImplementedError