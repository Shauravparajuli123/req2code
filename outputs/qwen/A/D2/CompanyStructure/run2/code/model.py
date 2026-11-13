"""Code skeleton generated from the shared model of D2/CompanyStructure.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Company:
    """Source: R1"""
    name: _t.Optional[str] = None
    corporateHQ: _t.Optional["CorporateHQ"] = None
    stores: _t.List["Store"] = _dc.field(default_factory=list)
    backOffice: _t.Optional["BackOffice"] = None

    def createCompany(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CorporateHQ(Company):
    """Source: R8"""
    name: _t.Optional[str] = None

    def createCorporateHQ(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Store(Company):
    """Source: R3"""
    name: _t.Optional[str] = None
    backOffice: _t.Optional["BackOffice"] = None
    cashRegisters: _t.List["CashRegister"] = _dc.field(default_factory=list)

    def createStore(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class BackOffice(Store):
    """Source: R4"""
    name: _t.Optional[str] = None

    def createBackOffice(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CashRegister(Store):
    """Source: R7"""
    name: _t.Optional[str] = None

    def createCashRegister(self) -> None:
        """Operation."""
        raise NotImplementedError
