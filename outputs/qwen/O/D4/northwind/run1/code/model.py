from enum import Enum

class PhoneNumber:
    def __init__(self, number):
        self.number = number

class State:
    def __init__(self, name):
        self.name = name

class UnitPrice:
    def __init__(self, value):
        self.value = value

class Quantity:
    def __init__(self, value):
        self.value = value

class OrderStatus(Enum):
    Pending = 'Pending'
    Processed = 'Processed'
    Shipped = 'Shipped'
    Cancelled = 'Cancelled'

class PurchaseOrderStatus(Enum):
    Pending = 'Pending'
    Approved = 'Approved'
    Rejected = 'Rejected'
    Completed = 'Completed'

class CompanyType(Enum):
    Customer = 'Customer'
    Vendor = 'Vendor'
    Shipper = 'Shipper'

class TaxStatus(Enum):
    Exempt = 'Exempt'
    Non_Exempt = 'Non-Exempt'

class Company:
    def __init__(self, name, phone_number, address_details, state, zip_code, website, company_type, tax_status):
        self.name = name
        self.phone_number = phone_number
        self.address_details = address_details
        self.state = state
        self.zip_code = zip_code
        self.website = website
        self.company_type = company_type
        self.tax_status = tax_status
        self.contacts = []

def add_contact(self, contact):
    self.contacts.append(contact)

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
    def __init__(self, name, phone_number, address_details, state, zip_code, website, company_type, tax_status):
        super().__init__(name, phone_number, address_details, state, zip_code, website, company_type, tax_status)

class Employee:
    def __init__(self, first_name, last_name, primary_phone_number, secondary_phone_number, job_title, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.primary_phone_number = primary_phone_number
        self.secondary_phone_number = secondary_phone_number
        self.job_title = job_title
        self.email_address = email_address
    def assign_privileges(self, privileges):
        raise NotImplementedError

class JobTitle:
    def __init__(self, title):
        self.title = title

class Order:
    def __init__(self, date, customer, employee, status):
        self.date = date
        self.customer = customer
        self.employee = employee
        self.status = status
    def add_order_detail(self, order_detail):
        raise NotImplementedError

class OrderDetailItem:
    def __init__(self, product, quantity, unit_price, discount):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount = discount
    def set_status(self, status):
        raise NotImplementedError

class Product:
    def __init__(self, code, name, description, unit_cost, retail_price, category, inventory_level, reorder_level, target_level, min_reorder_quantity, discontinued):
        self.code = code
        self.name = name
        self.description = description
        self.unit_cost = unit_cost
        self.retail_price = retail_price
        self.category = category
        self.inventory_level = inventory_level
        self.reorder_level = reorder_level
        self.target_level = target_level
        self.min_reorder_quantity = min_reorder_quantity
        self.discontinued = discontinued
    def add_to_inventory(self, quantity):
        raise NotImplementedError
    def remove_from_inventory(self, quantity):
        raise NotImplementedError

class PurchaseOrder:
    def __init__(self, date, vendor, employee_submitted, employee_approved, status):
        self.date = date
        self.vendor = vendor
        self.employee_submitted = employee_submitted
        self.employee_approved = employee_approved
        self.status = status
    def add_purchase_order_detail(self, purchase_order_detail):
        raise NotImplementedError

class PurchaseOrderDetailItem:
    def __init__(self, product, quantity, unit_price):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price