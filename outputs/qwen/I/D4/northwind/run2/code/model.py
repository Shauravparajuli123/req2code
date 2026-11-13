from typing import List, Optional

class Entity:
    def __init__(self, name: str, phone_number: Optional[str] = None, address: Optional[str] = None, state: Optional[str] = None, zip_code: Optional[str] = None, website: Optional[str] = None, tax_status: Optional[str] = None):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.state = state
        self.zip_code = zip_code
        self.website = website
        self.tax_status = tax_status

class Company(Entity):
    def __init__(self, name: str, phone_number: Optional[str] = None, address: Optional[str] = None, state: Optional[str] = None, zip_code: Optional[str] = None, website: Optional[str] = None, tax_status: Optional[str] = None, company_type: str):
        super().__init__(name, phone_number, address, state, zip_code, website, tax_status)
        self.company_type = company_type
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact):
        raise NotImplementedError

    def remove_contact(self, contact: Contact):
        raise NotImplementedError

    def get_contacts(self) -> List[Contact]:
        raise NotImplementedError

    def assign_tax_status(self, tax_status: str):
        raise NotImplementedError

    def assign_state(self, state: str):
        raise NotImplementedError

    def assign_company_type(self, company_type: str):
        raise NotImplementedError

    def __str__(self):
        return self.name

class Contact:
    def __init__(self, first_name: str, last_name: str, primary_phone: Optional[str] = None, secondary_phone: Optional[str] = None, email: Optional[str] = None, job_title: Optional[str] = None, notes: Optional[str] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.primary_phone = primary_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.job_title = job_title
        self.notes = notes

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'

class Employee(Entity):
    def __init__(self, first_name: str, last_name: str, phone_number: Optional[str] = None, address: Optional[str] = None, state: Optional[str] = None, zip_code: Optional[str] = None, website: Optional[str] = None, tax_status: Optional[str] = None, job_title: str, supervisor: Optional['Employee'] = None):
        super().__init__(first_name, last_name, phone_number, address, state, zip_code, website, tax_status)
        self.job_title = job_title
        self.supervisor = supervisor
        self.employees: List[Employee] = []

    def add_employee(self, employee: 'Employee'):
        raise NotImplementedError

    def remove_employee(self, employee: 'Employee'):
        raise NotImplementedError

    def get_employees(self) -> List['Employee']:
        raise NotImplementedError

    def assign_supervisor(self, supervisor: 'Employee'):
        raise NotImplementedError

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.job_title})'

class CompanyType:
    CUSTOMER = 'Customer'
    VENDOR = 'Vendor'
    SHIPPER = 'Shipper'

class TaxStatus:
    def __init__(self, status: str):
        self.status = status

    def __str__(self):
        return self.status

class State:
    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code

    def __str__(self):
        return self.name

class JobTitle:
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return self.title

class Customer(Company):
    def __init__(self, name: str, phone_number: Optional[str] = None, address: Optional[str] = None, state: Optional[str] = None, zip_code: Optional[str] = None, website: Optional[str] = None, tax_status: Optional[str] = None, company_type: str = CompanyType.CUSTOMER):
        super().__init__(name, phone_number, address, state, zip_code, website, tax_status, company_type)

    def __str__(self):
        return self.name

class Vendor(Company):
    def __init__(self, name: str, phone_number: Optional[str] = None, address: Optional[str] = None, state: Optional[str] = None, zip_code: Optional[str] = None, website: Optional[str] = None, tax_status: Optional[str] = None, company_type: str = CompanyType.VENDOR):
        super().__init__(name, phone_number, address, state, zip_code, website, tax_status, company_type)

    def __str__(self):
        return self.name

class Shipper(Company):
    def __init__(self, name: str, phone_number: Optional[str] = None, address: Optional[str] = None, state: Optional[str] = None, zip_code: Optional[str] = None, website: Optional[str] = None, tax_status: Optional[str] = None, company_type: str = CompanyType.SHIPPER):
        super().__init__(name, phone_number, address, state, zip_code, website, tax_status, company_type)

    def __str__(self):
        return self.name

class Product:
    def __init__(self, code: str, name: str, description: str, unit_cost: float, retail_price: float, inventory_level: int, reorder_level: int, target_level: int, min_reorder_quantity: int, discontinued: bool):
        self.code = code
        self.name = name
        self.description = description
        self.unit_cost = unit_cost
        self.retail_price = retail_price
        self.inventory_level = inventory_level
        self.reorder_level = reorder_level
        self.target_level = target_level
        self.min_reorder_quantity = min_reorder_quantity
        self.discontinued = discontinued

    def __str__(self):
        return self.name

class ProductCategory:
    def __init__(self, name: str, code: str, description: str, image: Optional[str] = None):
        self.name = name
        self.code = code
        self.description = description
        self.image = image

    def __str__(self):
        return self.name

class PurchaseOrder:
    def __init__(self, vendor: Vendor, employee_submitter: Employee, employee_approver: Employee, status: str, order_date: str):
        self.vendor = vendor
        self.employee_submitter = employee_submitter
        self.employee_approver = employee_approver
        self.status = status
        self.order_date = order_date
        self.details: List[PurchaseOrderDetailItem] = []

    def add_detail(self, detail: PurchaseOrderDetailItem):
        raise NotImplementedError

    def remove_detail(self, detail: PurchaseOrderDetailItem):
        raise NotImplementedError

    def get_details(self) -> List[PurchaseOrderDetailItem]:
        raise NotImplementedError

    def __str__(self):
        return f'PO from {self.vendor.name} submitted by {self.employee_submitter.first_name} {self.employee_submitter.last_name} and approved by {self.employee_approver.first_name} {self.employee_approver.last_name} on {self.order_date} '

class PurchaseOrderDetailItem:
    def __init__(self, product: Product, quantity: int, unit_price: float):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f'{self.product.name} x{self.quantity} @ ${self.unit_price} each'

class Order:
    def __init__(self, customer: Customer, employee: Employee, status: str, order_date: str):
        self.customer = customer
        self.employee = employee
        self.status = status
        self.order_date = order_date
        self.details: List[OrderDetailItem] = []

    def add_detail(self, detail: OrderDetailItem):
        raise NotImplementedError

    def remove_detail(self, detail: OrderDetailItem):
        raise NotImplementedError

    def get_details(self) -> List[OrderDetailItem]:
        raise NotImplementedError

    def __str__(self):
        return f'Order for {self.customer.name} processed by {self.employee.first_name} {self.employee.last_name} on {self.order_date} '

class OrderDetailItem:
    def __init__(self, product: Product, quantity: int, unit_price: float, discount: float):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount = discount

    def __str__(self):
        return f'{self.product.name} x{self.quantity} @ ${self.unit_price} each with {self.discount}% discount'

class Record:
    def __init__(self, added_by: Employee, added_date: str, modified_by: Employee, modified_date: str):
        self.added_by = added_by
        self.added_date = added_date
        self.modified_by = modified_by
        self.modified_date = modified_date
