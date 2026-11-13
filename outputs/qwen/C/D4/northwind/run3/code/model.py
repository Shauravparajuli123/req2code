"""Code skeleton generated from the shared model of D4/northwind.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Company:
    """Source: FR-CM-01, FR-CM-02, FR-CM-03, FR-CM-04, FR-CM-05, FR-CM-06, FR-CM-07"""
    name: _t.Optional[str] = None
    phoneNumber: _t.Optional[str] = None
    address: _t.Optional[str] = None
    state: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None
    website: _t.Optional[str] = None
    companyType: _t.Optional[str] = None
    taxStatus: _t.Optional[str] = None
    contacts: _t.Optional[str] = None
    contact: _t.Optional["Contact"] = None


@_dc.dataclass
class Contact:
    """Source: FR-CM-07"""
    firstName: _t.Optional[str] = None
    lastName: _t.Optional[str] = None
    primaryPhoneNumber: _t.Optional[str] = None
    secondaryPhoneNumber: _t.Optional[str] = None
    email: _t.Optional[str] = None
    jobTitle: _t.Optional[str] = None
    notes: _t.Optional[str] = None


@_dc.dataclass
class Customer:
    """Source: FR-CM-01"""
    pass


@_dc.dataclass
class Employee:
    """Source: FR-EM-01, FR-EM-02, FR-EM-03, FR-EM-04, FR-EM-05"""
    firstName: _t.Optional[str] = None
    lastName: _t.Optional[str] = None
    primaryPhoneNumber: _t.Optional[str] = None
    secondaryPhoneNumber: _t.Optional[str] = None
    jobTitle: _t.Optional[str] = None
    email: _t.Optional[str] = None

    def assignTitle(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Order:
    """Source: FR-SOP-01, FR-SOP-02, FR-SOP-03, FR-SOP-04, FR-SOP-05, FR-SOP-06, FR-SOP-07, FR-SOP-08, FR-SOP-09, FR-SOP-10"""
    orderDate: _t.Optional[str] = None
    customer: _t.Optional[str] = None
    employee: _t.Optional[str] = None
    status: _t.Optional[str] = None
    shipper: _t.Optional[str] = None
    taxRate: _t.Optional[float] = None
    taxStatus: _t.Optional[str] = None
    invoiceDate: _t.Optional[str] = None
    paymentMethod: _t.Optional[str] = None
    paymentDate: _t.Optional[str] = None
    orderDetails: _t.Optional[str] = None
    orderStatus: _t.Optional["OrderStatus"] = None
    shippers: _t.Optional["Shippers"] = None
    orderDetailItem: _t.Optional["OrderDetailItem"] = None

    def addOrderDetail(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class OrderDetailItem:
    """Source: FR-SOP-09, FR-SOP-10"""
    product: _t.Optional[str] = None
    quantity: _t.Optional[int] = None
    unitPrice: _t.Optional[float] = None
    discount: _t.Optional[float] = None
    status: _t.Optional[str] = None


@_dc.dataclass
class Product:
    """Source: FR-PM-01, FR-PM-02, FR-PM-03, FR-PM-04, FR-PM-05, FR-PM-06"""
    code: _t.Optional[str] = None
    name: _t.Optional[str] = None
    description: _t.Optional[str] = None
    unitCost: _t.Optional[float] = None
    retailPrice: _t.Optional[float] = None
    category: _t.Optional[str] = None
    inventoryLevel: _t.Optional[int] = None
    reorderLevel: _t.Optional[int] = None
    targetLevel: _t.Optional[int] = None
    minReorderQuantity: _t.Optional[int] = None
    discontinued: _t.Optional[bool] = None
    productCategory: _t.Optional["ProductCategory"] = None


@_dc.dataclass
class PurchaseOrder:
    """Source: FR-POP-01, FR-POP-02, FR-POP-03, FR-POP-04, FR-POP-05, FR-POP-06, FR-POP-07, FR-POP-08"""
    orderDate: _t.Optional[str] = None
    vendor: _t.Optional[str] = None
    employee: _t.Optional[str] = None
    approver: _t.Optional[str] = None
    status: _t.Optional[str] = None
    purchaseOrderStatus: _t.Optional["PurchaseOrderStatus"] = None
    purchaseOrderDetailItem: _t.Optional["PurchaseOrderDetailItem"] = None


@_dc.dataclass
class PurchaseOrderDetailItem:
    """Source: FR-POP-07, FR-POP-08"""
    product: _t.Optional[str] = None
    quantity: _t.Optional[int] = None
    unitPrice: _t.Optional[float] = None


@_dc.dataclass
class PhoneNumber:
    """Source: FR-CM-03"""
    number: _t.Optional[str] = None


@_dc.dataclass
class ProductCategory:
    """Source: FR-PM-06"""
    name: _t.Optional[str] = None
    code: _t.Optional[str] = None
    description: _t.Optional[str] = None
    image: _t.Optional[str] = None


@_dc.dataclass
class Shippers:
    """Source: FR-CM-01"""
    pass


@_dc.dataclass
class State:
    """Source: FR-CM-05"""
    pass


class TaxStatus(_enum.Enum):
    """Source: FR-CM-06"""
    TAXSTATUSENUM = "TAXSTATUSENUM"


class CompanyType(_enum.Enum):
    """Source: FR-CM-04"""
    CUSTOMER = "CUSTOMER"
    VENDOR = "VENDOR"
    SHIPPER = "SHIPPER"


class OrderStatus(_enum.Enum):
    """Source: FR-SOP-04"""
    ORDERSTATUSENUM = "ORDERSTATUSENUM"


class PurchaseOrderStatus(_enum.Enum):
    """Source: FR-POP-05"""
    PURCHASEORDERSTATUSENUM = "PURCHASEORDERSTATUSENUM"


class OrderDetailStatus(_enum.Enum):
    """Source: FR-SOP-10"""
    ORDERDETAILSTATUSENUM = "ORDERDETAILSTATUSENUM"
