class Company:
    def __init__(self, name: str):
        self.name = name
        self.backOffice = None
        self.employees = []

    def addEmployee(self, employee):
        raise NotImplementedError

    def removeEmployee(self, employee):
        raise NotImplementedError


class CompanyStructureModel:
    def __init__(self, hq: Hq):
        self.hq = hq
        self.stores = []
        self.cashRegisters = []

    def addStore(self, store: Store):
        raise NotImplementedError

    def removeStore(self, store: Store):
        raise NotImplementedError

    def addCashRegister(self, cashRegister: CashRegister):
        raise NotImplementedError

    def removeCashRegister(self, cashRegister: CashRegister):
        raise NotImplementedError


class Hq:
    def __init__(self):
        pass


class Office:
    def __init__(self):
        pass


class Store:
    def __init__(self, name: str, backOffice: Office):
        self.name = name
        self.backOffice = backOffice
        self.cashRegisters = []

    def addCashRegister(self, cashRegister: CashRegister):
        raise NotImplementedError

    def removeCashRegister(self, cashRegister: CashRegister):
        raise NotImplementedError


class CashRegister:
    def __init__(self):
        pass