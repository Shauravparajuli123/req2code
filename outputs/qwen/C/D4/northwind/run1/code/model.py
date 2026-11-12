"""Code skeleton generated from the shared model of D4/northwind.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Company:
    """Source: FR-CM-03"""
    name: _t.Optional[str] = None
    phoneNumber: _t.Optional[str] = None
    addressDetails: _t.Optional[str] = None
    state: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None
    website: _t.Optional[str] = None
    companyType: _t.Optional[str] = None
    taxStatus: _t.Optional[str] = None
    contacts: _t.Optional[str] = None
    contact: _t.Optional["Contact"] = None

    def addContact(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Contact:
    """Source: FR-CM-07"""
    firstName: _t.Optional[str] = None
    lastName: _t.Optional[str] = None
    primaryPhoneNumber: _t.Optional[str] = None
    secondaryPhoneNumber: _t.Optional[str] = None
    emailAddress: _t.Optional[str] = None
    jobTitle: _t.Optional[str] = None
    notes: _t.Optional[str] = None


@_dc.dataclass
class Employee:
    """Source: FR-EM-01"""
    firstName: _t.Optional[str] = None
    lastName: _t.Optional[str] = None
    primaryPhoneNumber: _t.Optional[str] = None
    secondaryPhoneNumber: _t.Optional[str] = None
    jobTitle: _t.Optional[str] = None
    email: _t.Optional[str] = None
    title: _t.Optional[str] = None

    def assignTitle(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Order:
    """Source: FR-SOP-01"""
    customer: _t.Optional[str] = None
    employee: _t.Optional[str] = None
    orderStatus: _t.Optional[str] = None
    shipper: _t.Optional[str] = None
    taxRate: _t.Optional[float] = None
    taxStatus: _t.Optional[str] = None
    invoiceDate: _t.Optional[str] = None
    paymentMethod: _t.Optional[str] = None
    paymentDate: _t.Optional[str] = None
    orderDetails: _t.Optional[str] = None
    orderDetailItem: _t.Optional["OrderDetailItem"] = None

    def addOrderDetail(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class OrderDetailItem:
    """Source: FR-SOP-09"""
    product: _t.Optional[str] = None
    quantity: _t.Optional[int] = None
    unitPrice: _t.Optional[float] = None
    discount: _t.Optional[float] = None
    status: _t.Optional[str] = None

    def updateStatus(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Product:
    """Source: FR-PM-01"""
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


@_dc.dataclass
class PurchaseOrder:
    """Source: FR-POP-01"""
    vendor: _t.Optional[str] = None
    employeeSubmitted: _t.Optional[str] = None
    employeeApproved: _t.Optional[str] = None
    status: _t.Optional[str] = None
    orderDate: _t.Optional[str] = None
    purchaseOrderDetails: _t.Optional[str] = None
    employee: _t.Optional["Employee"] = None
    purchaseOrderDetailItem: _t.Optional["PurchaseOrderDetailItem"] = None

    def addPurchaseOrderDetail(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class PurchaseOrderDetailItem:
    """Source: FR-POP-08"""
    product: _t.Optional[str] = None
    quantity: _t.Optional[int] = None
    unitPrice: _t.Optional[float] = None


@_dc.dataclass
class Customer:
    """Source: FR-SOP-02"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Shipper:
    """Source: FR-SOP-05"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Vendor:
    """Source: FR-POP-02"""
    name: _t.Optional[str] = None


@_dc.dataclass
class PhoneNumber:
    """Source: FR-CM-08, FR-EM-01"""
    number: _t.Optional[str] = None


@_dc.dataclass
class JobTitle:
    """Source: FR-EM-02"""
    title: _t.Optional[str] = None


@_dc.dataclass
class Date:
    """Source: FR-SOP-07, FR-POP-06"""
    date: _t.Optional[str] = None
