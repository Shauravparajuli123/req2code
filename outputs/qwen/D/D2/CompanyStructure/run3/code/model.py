"""Code skeleton generated from the shared model of D2/CompanyStructure.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Company:
    """Source: R1, R6"""
    corporateHQ: _t.Optional[str] = None
    stores: _t.Optional[str] = None
    backOffices: _t.Optional[str] = None
    backOffice: _t.Optional["BackOffice"] = None


@_dc.dataclass
class CorporateHQ:
    """Source: R8, R9"""
    managedStores: _t.Optional[str] = None
    stores: _t.List["Store"] = _dc.field(default_factory=list)


@_dc.dataclass
class Store:
    """Source: R3, R10, R11"""
    backOffice: _t.Optional[str] = None
    cashRegisters: _t.Optional[str] = None


@_dc.dataclass
class BackOffice:
    """Source: R4, R5, R10"""
    pass


@_dc.dataclass
class CashRegister:
    """Source: R7, R11"""
    pass
