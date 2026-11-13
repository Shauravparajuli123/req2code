from typing import List

class CashRegister:
    pass

class Company:
    def __init__(self, office: Office):
        self.office = office
        self.employees = []

class CompanyStructureModel:
    def __init__(self, hq: Hq, stores: List[Store], cash_registers: List[CashRegister]):
        self.hq = hq
        self.stores = stores
        self.cash_registers = cash_registers

class Hq:
    pass

class Office:
    pass

class Store:
    def __init__(self, office: Office):
        self.office = office
        self.cash_registers = []
