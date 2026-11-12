class Company:
    def __init__(self, name):
        self.name = name
        self.office = None
    def addOffice(self, office):
        raise NotImplementedError

class CompanyStructureModel:
    def __init__(self):
        self.hq = None
        self.companies = []
        self.stores = []
    def addCompany(self, company):
        raise NotImplementedError
    def addStore(self, store):
        raise NotImplementedError
class Hq:
    def __init__(self):
        pass
    def manageStores(self):
        raise NotImplementedError
class Office:
    def __init__(self, type):
        self.type = type
class Store:
    def __init__(self, name):
        self.name = name
    def addCashRegister(self):
        raise NotImplementedError
class CashRegister:
    def __init__(self):
        pass