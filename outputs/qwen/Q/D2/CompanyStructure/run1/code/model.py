from typing import List

class CompanyStructureModel:
    def __init__(self):
        self.companies: List[Company] = []
        self.hq: Hq = Hq()
        self.stores: List[Store] = []
        self.back_offices: List[BackOffice] = []
        self.cash_registers: List[CashRegister] = []
    
    def add_company(self, company: Company):
        raise NotImplementedError
    
    def add_store(self, store: Store):
        raise NotImplementedError
    
    def add_back_office(self, back_office: BackOffice):
        raise NotImplementedError
    
    def add_cash_register(self, cash_register: CashRegister):
        raise NotImplementedError

class Company:
    def __init__(self, employees: List[str]):
        self.employees: List[str] = employees
        self.back_office: BackOffice = BackOffice()
    
    def add_back_office(self, back_office: BackOffice):
        raise NotImplementedError

class Hq:
    pass
class Store:
    def __init__(self, back_office: BackOffice, cash_registers: List[CashRegister] = []):
        self.back_office: BackOffice = back_office
        self.cash_registers: List[CashRegister] = cash_registers
class BackOffice:
    pass
class CashRegister:
    pass