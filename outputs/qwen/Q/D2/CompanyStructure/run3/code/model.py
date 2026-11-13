from typing import List

class CompanyStructureModel:
    def __init__(self):
        self.cash_registers: List[CashRegister] = []
        self.companies: List[Company] = []
        self.hq: Hq = Hq()
        self.stores: List[Store] = []
        self.offices: List[Office] = []
    def add_cash_register(self, cash_register: CashRegister):
        raise NotImplementedError
    def add_company(self, company: Company):
        raise NotImplementedError
    def add_store(self, store: Store):
        raise NotImplementedError
    def add_office(self, office: Office):
        raise NotImplementedError
    def get_hq(self) -> Hq:
        raise NotImplementedError
    def get_stores(self) -> List[Store]:
        raise NotImplementedError
    def get_offices(self) -> List[Office]:
        raise NotImplementedError

class Company:
    def __init__(self, office: Office):
        self.office: Office = office
    def get_office(self) -> Office:
        raise NotImplementedError

class Store:
    def __init__(self, office: Office):
        self.office: Office = office
    def get_office(self) -> Office:
        raise NotImplementedError

class Hq:
    def __init__(self):
        pass

class Office:
    def __init__(self):
        pass

class CashRegister:
    def __init__(self):
        pass