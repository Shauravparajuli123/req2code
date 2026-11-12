from enum import Enum

class PhoneNumber:
    def __init__(self, number: str):
        self.number = number

class ProductCategory(Enum):
    def __init__(self, name: str, code: str, description: str, image: str = ''):
        self.name = name
        self.code = code
        self.description = description
        self.image = image

class OrderStatus(Enum):
    Pending = 'Pending'
    Processing = 'Processing'
    Shipped = 'Shipped'
    Delivered = 'Delivered'
    Cancelled = 'Cancelled'

class PurchaseOrderStatus(Enum):
    Pending = 'Pending'
    Processing = 'Processing'
    Shipped = 'Shipped'
    Delivered = 'Delivered'
    Cancelled = 'Cancelled'

class UnitPrice:
    def __init__(self, value: float):
        self.value = value

class Quantity:
    def __init__(self, value: int):
        self.value = value

class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

class Company:
    def __init__(self, name: str, phoneNumbers: list[PhoneNumber], addressDetails: str, state: str, zipCode: str, website: str, companyType: str, taxStatus: str, contacts: list[Contact] = []):
        self.name = name
        self.phoneNumbers = phoneNumbers
        self.addressDetails = addressDetails
        self.state = state
        self.zipCode = zipCode
        self.website = website
        self.companyType = companyType
        self.taxStatus = taxStatus
        self.contacts = contacts

def addContact(self, contact: Contact):
    raise NotImplementedError

def removeContact(self, contact: Contact):
    raise NotImplementedError

class Contact:
    def __init__(self, firstName: str, lastName: str, primaryPhoneNumber: PhoneNumber, secondaryPhoneNumber: PhoneNumber, email: str, jobTitle: str, notes: str):
        self.firstName = firstName
        self.lastName = lastName
        self.primaryPhoneNumber = primaryPhoneNumber
        self.secondaryPhoneNumber = secondaryPhoneNumber
        self.email = email
        self.jobTitle = jobTitle
        self.notes = notes

class Employee:
    def __init__(self, firstName: str, lastName: str, phoneNumbers: list[PhoneNumber], jobTitle: str, privileges: list[str], supervisor: 'Employee' = None, subordinates: list['Employee'] = []):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumbers = phoneNumbers
        self.jobTitle = jobTitle
        self.privileges = privileges
        self.supervisor = supervisor
        self.subordinates = subordinates

def assignPrivilege(self, privilege: str):
    raise NotImplementedError

def removePrivilege(self, privilege: str):
    raise NotImplementedError

class Product:
    def __init__(self, code: str, name: str, description: str, price: UnitPrice, category: ProductCategory, unitCost: UnitPrice, retailPrice: UnitPrice, reorderLevel: Quantity, targetLevel: Quantity, minReorderQuantity: Quantity, discontinued: bool):
        self.code = code
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.unitCost = unitCost
        self.retailPrice = retailPrice
        self.reorderLevel = reorderLevel
        self.targetLevel = targetLevel
        self.minReorderQuantity = minReorderQuantity
        self.discontinued = discontinued

def updatePrice(self, newPrice: UnitPrice):
    raise NotImplementedError

class Order:
    def __init__(self, date: Date, customer: Company, employee: Employee, status: OrderStatus):
        self.date = date
        self.customer = customer
        self.employee = employee
        self.status = status

def addOrderDetail(self, orderDetailItem: 'OrderDetailItem'):
    raise NotImplementedError

def removeOrderDetail(self, orderDetailItem: 'OrderDetailItem'):
    raise NotImplementedError

class OrderDetailItem:
    def __init__(self, product: Product, quantity: Quantity, unitPrice: UnitPrice, discount: UnitPrice = None):
        self.product = product
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.discount = discount

def updateQuantity(self, newQuantity: Quantity):
    raise NotImplementedError

def updateUnitPrice(self, newUnitPrice: UnitPrice):
    raise NotImplementedError

def updateDiscount(self, newDiscount: UnitPrice):
    raise NotImplementedError

class PurchaseOrder:
    def __init__(self, date: Date, vendor: Company, employee: Employee, status: PurchaseOrderStatus):
        self.date = date
        self.vendor = vendor
        self.employee = employee
        self.status = status

def addPurchaseOrderDetail(self, purchaseOrderDetailItem: 'PurchaseOrderDetailItem'):
    raise NotImplementedError

def removePurchaseOrderDetail(self, purchaseOrderDetailItem: 'PurchaseOrderDetailItem'):
    raise NotImplementedError

class PurchaseOrderDetailItem:
    def __init__(self, product: Product, quantity: Quantity, unitPrice: UnitPrice):
        self.product = product
        self.quantity = quantity
        self.unitPrice = unitPrice

class Vendor:
    def __init__(self, name: str, phoneNumbers: list[PhoneNumber], addressDetails: str, state: str, zipCode: str, website: str):
        self.name = name
        self.phoneNumbers = phoneNumbers
        self.addressDetails = addressDetails
        self.state = state
        self.zipCode = zipCode
        self.website = website