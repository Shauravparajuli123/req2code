"""Code skeleton generated from the shared model of D2/CompanyStructure.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Company:
    """Source: R1, R8, R9"""
    name: _t.Optional[str] = None
    hq: _t.Optional[str] = None
    stores: _t.Optional[str] = None
    backOffices: _t.Optional[str] = None
    employees: _t.Optional[str] = None
    corporateHQ: _t.Optional["CorporateHQ"] = None

    def createGame(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class CorporateHQ:
    """Source: R8"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Store:
    """Source: R3, R10, R11"""
    name: _t.Optional[str] = None
    backOffice: _t.Optional[str] = None
    cashRegisters: _t.Optional[str] = None
    cashRegister: _t.Optional["CashRegister"] = None


@_dc.dataclass
class BackOffice:
    """Source: R4, R5, R10"""
    name: _t.Optional[str] = None


@_dc.dataclass
class CashRegister:
    """Source: R7, R11"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Employee:
    """Source: R6"""
    name: _t.Optional[str] = None
