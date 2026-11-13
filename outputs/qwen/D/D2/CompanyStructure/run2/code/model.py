"""Code skeleton generated from the shared model of D2/CompanyStructure.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Company:
    """Source: R1, R6"""
    name: _t.Optional[str] = None
    backOffice: _t.Optional[str] = None
    stores: _t.Optional[str] = None
    employees: _t.Optional[str] = None
    corporateHQ: _t.Optional["CorporateHQ"] = None

    def createCompany(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CorporateHQ:
    """Source: R2, R8"""
    name: _t.Optional[str] = None
    stores: _t.Optional[str] = None

    def createCorporateHQ(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Store:
    """Source: R3, R10, R11"""
    name: _t.Optional[str] = None
    backOffice: _t.Optional[str] = None
    cashRegisters: _t.Optional[str] = None

    def createStore(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class BackOffice:
    """Source: R4, R5, R10"""
    name: _t.Optional[str] = None


@_dc.dataclass
class CashRegister:
    """Source: R7, R11"""
    name: _t.Optional[str] = None
