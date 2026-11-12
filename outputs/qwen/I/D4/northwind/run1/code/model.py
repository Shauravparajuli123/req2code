from enum import Enum
from typing import List

class Privilege(Enum):
    Read = 'Read'
    Write = 'Write'
    Admin = 'Admin'

class TaxStatus(Enum):
    Exempt = 'Exempt'
    Non_Exempt = 'Non-Exempt'

class PhoneNumber:
    def __init__(self, number: str):
        self.number = number

class State:
    def __init__(self, name: str):
        self.name = name

class Company:
    def __init__(self, name: str, phone_number: PhoneNumber, address_details: str, state: State, zip_code: str, website: str, company_type: str, tax_status: TaxStatus):
        self.name = name
        self.phone_number = phone_number
        self.address_details = address_details
        self.state = state
        self.zip_code = zip_code
        self.website = website
        self.company_type = company_type
        self.tax_status = tax_status
        self.contacts: List[Contact] = []
        self.orders: List[Order] = []
        self.purchase_orders: List[PurchaseOrder] = []

class Contact:
    def __init__(self, first_name: str, last_name: str, primary_phone_number: PhoneNumber, secondary_phone_number: PhoneNumber, email_address: str, job_title: JobTitle, notes: str):
        self.first_name = first_name
        self.last_name = last_name
        self.primary_phone_number = primary_phone_number
        self.secondary_phone_number = secondary_phone_number
        self.email_address = email_address
        self.job_title = job_title
        self.notes = notes

class Employee:
    def __init__(self, first_name: str, last_name: str, primary_phone_number: PhoneNumber, secondary_phone_number: PhoneNumber, job_title: JobTitle, privileges: List[Privilege], supervisor: 'Employee', reports: List['Employee']):
        self.first_name = first_name
        self.last_name = last_name
        self.primary_phone_number = primary_phone_number
        self.secondary_phone_number = secondary_phone_number
        self.job_title = job_title
        self.privileges = privileges
        self.supervisor = supervisor
        self.reports = reports

class JobTitle:
    def __init__(self, title: str):
        self.title = title

class Order:
    def __init__(self, date: str, customer: Customer, employee: Employee, status: str):
        self.date = date
        self.customer = customer
        self.employee = employee
        self.status = status
        self.details: List[OrderDetailItem] = []

class OrderDetailItem:
    def __init__(self, product: Product, quantity: int, unit_price: float, discount: float, status: str):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount = discount
        self.status = status

class Product:
    def __init__(self, code: str, name: str, description: str, unit_cost: float, retail_price: float, category: str, discontinued: bool):
        self.code = code
        self.name = name
        self.description = description
        self.unit_cost = unit_cost
        self.retail_price = retail_price
        self.category = category
        self.discontinued = discontinued

class PurchaseOrder:
    def __init__(self, date: str, vendor: Company, employee_submitted: Employee, employee_approved: Employee, status: str):
        self.date = date
        self.vendor = vendor
        self.employee_submitted = employee_submitted
        self.employee_approved = employee_approved
        self.status = status
        self.details: List[PurchaseOrderDetailItem] = []

class PurchaseOrderDetailItem:
    def __init__(self, product: Product, quantity: int, unit_price: float):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price

class Record:
    def __init__(self, added_by: Employee, added_date: str, last_modified_by: Employee, last_modified_date: str):
        self.added_by = added_by
        self.added_date = added_date
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date