from typing import List, Optional, Union

class PhoneNumber:
    def __init__(self, number: str):
        self.number = number

class JobTitle:
    def __init__(self, name: str):
        self.name = name

class State:
    def __init__(self, name: str):
        self.name = name

class TaxStatus:
    def __init__(self, name: str):
        self.name = name

class UnitPrice:
    def __init__(self, value: float):
        self.value = value

class Quantity:
    def __init__(self, value: float):
        self.value = value

class ProductCategory:
    def __init__(self, name: str, code: str, description: str, image: Optional[str] = None):
        self.name = name
        self.code = code
        self.description = description
        self.image = image

class Company:
    def __init__(self, name: str, phoneNumbers: List[PhoneNumber], addressDetails: str, state: State, zipCode: str, website: str, taxStatus: TaxStatus, companyType: str):
        self.name = name
        self.phoneNumbers = phoneNumbers
        self.addressDetails = addressDetails
        self.state = state
        self.zipCode = zipCode
        self.website = website
        self.taxStatus = taxStatus
        self.companyType = companyType
        self.contacts = []

    def addContact(self, contact: 'Contact') -> None:
        raise NotImplementedError

    def recordCompanyInformation(self) -> None:
        raise NotImplementedError

class Employee:
    def __init__(self, firstName: str, lastName: str, phoneNumbers: List[PhoneNumber], jobTitle: JobTitle, privileges: List[str], supervisor: Optional['Employee'] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumbers = phoneNumbers
        self.jobTitle = jobTitle
        self.privileges = privileges
        self.supervisor = supervisor
        self.subordinates = []

    def assignPrivileges(self, privileges: List[str]) -> None:
        raise NotImplementedError

    def assignSupervisor(self, supervisor: 'Employee') -> None:
        raise NotImplementedError

class Product:
    def __init__(self, productCode: str, name: str, description: str, price: UnitPrice, category: ProductCategory, unitCost: UnitPrice, retailPrice: UnitPrice, reorderLevel: Quantity, targetLevel: Quantity, minReorderQuantity: Quantity, discontinued: bool):
        self.productCode = productCode
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

    def updateInventory(self) -> None:
        raise NotImplementedError

class OrderDetailItem:
    def __init__(self, product: Product, quantity: Quantity, unitPrice: UnitPrice, discount: UnitPrice):
        self.product = product
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.discount = discount

    def recordOrderDetail(self) -> None:
        raise NotImplementedError

class Order:
    def __init__(self, orderDate: str, customer: 'Customer', employee: 'Employee', status: str, shipper: 'Shippers', taxStatus: TaxStatus, invoiceDate: str, paymentMethod: str, paymentDate: str, orderDetails: List[OrderDetailItem]):
        self.orderDate = orderDate
        self.customer = customer
        self.employee = employee
        self.status = status
        self.shipper = shipper
        self.taxStatus = taxStatus
        self.invoiceDate = invoiceDate
        self.paymentMethod = paymentMethod
        self.paymentDate = paymentDate
        self.orderDetails = orderDetails

    def recordOrder(self) -> None:
        raise NotImplementedError

    def updateOrderStatus(self, status: str) -> None:
        raise NotImplementedError

class PurchaseOrderDetailItem:
    def __init__(self, product: Product, quantity: Quantity, unitPrice: UnitPrice):
        self.product = product
        self.quantity = quantity
        self.unitPrice = unitPrice

    def recordPurchaseOrderDetail(self) -> None:
        raise NotImplementedError

class PurchaseOrder:
    def __init__(self, orderDate: str, vendor: 'Vendor', employee: 'Employee', status: str, purchaseOrderDetails: List[PurchaseOrderDetailItem]):
        self.orderDate = orderDate
        self.vendor = vendor
        self.employee = employee
        self.status = status
        self.purchaseOrderDetails = purchaseOrderDetails

    def recordPurchaseOrder(self) -> None:
        raise NotImplementedError

    def updatePurchaseOrderStatus(self, status: str) -> None:
        raise NotImplementedError

class Contact:
    def __init__(self, firstName: str, lastName: str, phoneNumbers: List[PhoneNumber], email: str, jobTitle: JobTitle, notes: str):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumbers = phoneNumbers
        self.email = email
        self.jobTitle = jobTitle
        self.notes = notes

    def addContact(self) -> None:
        raise NotImplementedError

class Customer:
    def __init__(self, name: str, phoneNumbers: List[PhoneNumber], addressDetails: str, state: State, zipCode: str, website: str, taxStatus: TaxStatus):
        self.name = name
        self.phoneNumbers = phoneNumbers
        self.addressDetails = addressDetails
        self.state = state
        self.zipCode = zipCode
        self.website = website
        self.taxStatus = taxStatus

    def recordCustomerInformation(self) -> None:
        raise NotImplementedError

class Shippers:
    def __init__(self, name: str, phoneNumbers: List[PhoneNumber], addressDetails: str, state: State, zipCode: str, website: str, taxStatus: TaxStatus):
        self.name = name
        self.phoneNumbers = phoneNumbers
        self.addressDetails = addressDetails
        self.state = state
        self.zipCode = zipCode
        self.website = website
        self.taxStatus = taxStatus

    def recordShipperInformation(self) -> None:
        raise NotImplementedError