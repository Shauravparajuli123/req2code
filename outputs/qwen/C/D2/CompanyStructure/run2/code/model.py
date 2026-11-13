"""Code skeleton generated from the shared model of D2/CompanyStructure.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CompanyStructureModel:
    """Source: R1"""
    company: _t.Optional["Company"] = None
    hq: _t.Optional["Hq"] = None
    stores: _t.List["Store"] = _dc.field(default_factory=list)
    cashRegisters: _t.List["CashRegister"] = _dc.field(default_factory=list)


@_dc.dataclass
class Company:
    """Source: R1, R8, R9, R10"""
    hq: _t.Optional[str] = None
    stores: _t.Optional[str] = None
    backOffice: _t.Optional[str] = None

    def addStore(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addBackOffice(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Hq:
    """Source: R8, R9"""
    pass


@_dc.dataclass
class Store:
    """Source: R3, R9, R10, R11"""
    backOffice: _t.Optional[str] = None
    office: _t.Optional["Office"] = None
    cashRegisters: _t.List["CashRegister"] = _dc.field(default_factory=list)

    def addCashRegister(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Office:
    """Source: R4, R10"""
    pass


@_dc.dataclass
class CashRegister:
    """Source: R7, R11"""
    pass
