from datetime import date

class PhoneNumber:
    pass

class Quantity:
    pass

class UnitPrice:
    pass

class State:
    pass

class TaxStatus:
    pass

class JobTitle:
    pass

class Record:
    def addRecord(self):
        raise NotImplementedError

class Company(Entity):
    def assignTaxStatus(self):
        raise NotImplementedError

class Contact:
    def __init__(self, first_name, last_name, primary_phone_number, secondary_phone_number, email_address, job_title, notes):
        self.first_name = first_name
        self.last_name = last_name
        self.primary_phone_number = primary_phone_number
        self.secondary_phone_number = secondary_phone_number
        self.email_address = email_address
        self.job_title = job_title
        self.notes = notes

class Customer(Company):
    pass

class Employee:
    def assignJobTitle(self):
        raise NotImplementedError

class Order:
    def assignStatus(self):
        raise NotImplementedError

class OrderDetailItem:
    def assignStatus(self):
        raise NotImplementedError

class Product:
    def assignStatus(self):
        raise NotImplementedError

class PurchaseOrder:
    def assignStatus(self):
        raise NotImplementedError

class PurchaseOrderDetailItem:
    pass

class Vendor(Entity):
    pass

class Shippers(Entity):
    pass