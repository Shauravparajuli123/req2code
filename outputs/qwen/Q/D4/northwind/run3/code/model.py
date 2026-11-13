from typing import List, Optional, Union

class PhoneNumber:
    def __init__(self, number: str):
        self.number = number

class State:
    pass

class TaxStatus:
    pass

class UnitPrice:
    def __init__(self, value: float):
        self.value = value

class ProductCategory:
    def __init__(self, name: str, code: str, description: str, image: Optional[str] = None):
        self.name = name
        self.code = code
        self.description = description
        self.image = image

class Product:
    def __init__(self, product_code: str, name: str, description: str, price: UnitPrice, category: ProductCategory, unit_cost: UnitPrice, retail_price: UnitPrice, reorder_level: int, target_level: int, min_reorder_quantity: int, discontinued: bool):
        self.product_code = product_code
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.unit_cost = unit_cost
        self.retail_price = retail_price
        self.reorder_level = reorder_level
        self.target_level = target_level
        self.min_reorder_quantity = min_reorder_quantity
        self.discontinued = discontinued

class Company:
    def __init__(self, name: str, phoneNumbers: List[PhoneNumber], addressDetails: str, state: State, zipCode: str, website: str, taxStatus: TaxStatus, companyType: str, contacts: List['Contact']):
        self.name = name
        self.phoneNumbers = phoneNumbers
        self.addressDetails = addressDetails
        self.state = state
        self.zipCode = zipCode
        self.website = website
        self.taxStatus = taxStatus
        self.companyType = companyType
        self.contacts = contacts

    def addContact(self, contact: 'Contact'):
        raise NotImplementedError

    def removeContact(self, contact: 'Contact'):
        raise NotImplementedError

class Contact:
    def __init__(self, firstName: str, lastName: str, primaryPhoneNumber: PhoneNumber, secondaryPhoneNumber: Optional[PhoneNumber] = None, email: str, jobTitle: str, notes: str):
        self.firstName = firstName
        self.lastName = lastName
        self.primaryPhoneNumber = primaryPhoneNumber
        self.secondaryPhoneNumber = secondaryPhoneNumber
        self.email = email
        self.jobTitle = jobTitle
        self.notes = notes

class Employee:
    def __init__(self, firstName: str, lastName: str, phoneNumbers: List[PhoneNumber], jobTitle: str, email: str, privileges: List[str], supervisor: Optional['Employee'] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumbers = phoneNumbers
        self.jobTitle = jobTitle
        self.email = email
        self.privileges = privileges
        self.supervisor = supervisor

    def assignSupervisor(self, supervisor: 'Employee'):
        raise NotImplementedError

    def removeSupervisor(self, supervisor: 'Employee'):
        raise NotImplementedError

class Order:
    def __init__(self, orderDate: str, customer: 'Customer', employee: 'Employee', status: str, shipper: 'Shippers', taxStatus: TaxStatus, invoiceDate: str, paymentMethod: str, paymentDate: str):
        self.orderDate = orderDate
        self.customer = customer
        self.employee = employee
        self.status = status
        self.shipper = shipper
        self.taxStatus = taxStatus
        self.invoiceDate = invoiceDate
        self.paymentMethod = paymentMethod
        self.paymentDate = paymentDate

    def addOrderDetail(self, orderDetailItem: 'OrderDetailItem'):
        raise NotImplementedError

    def removeOrderDetail(self, orderDetailItem: 'OrderDetailItem'):
        raise NotImplementedError

class OrderDetailItem:
    def __init__(self, product: Product, quantity: int, unitPrice: UnitPrice, discount: Optional[UnitPrice] = None, status: str = 'Pending'):
        self.product = product
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.discount = discount
        self.status = status

class PurchaseOrder:
    def __init__(self, orderDate: str, vendor: 'Vendor', employee: 'Employee', status: str):
        self.orderDate = orderDate
        self.vendor = vendor
        self.employee = employee
        self.status = status

    def addPurchaseOrderDetail(self, purchaseOrderDetailItem: 'PurchaseOrderDetailItem'):
        raise NotImplementedError

    def removePurchaseOrderDetail(self, purchaseOrderDetailItem: 'PurchaseOrderDetailItem'):
        raise NotImplementedError

class PurchaseOrderDetailItem:
    def __init__(self, product: Product, quantity: int, unitPrice: UnitPrice):
        self.product = product
        self.quantity = quantity
        self.unitPrice = unitPrice
