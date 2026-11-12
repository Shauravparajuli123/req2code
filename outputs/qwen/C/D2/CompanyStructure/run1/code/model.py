"""Code skeleton generated from the shared model of D2/CompanyStructure.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CompanyStructureModel:
    """Source: R1"""
    hq: _t.Optional[str] = None
    stores: _t.Optional[str] = None
    backOffices: _t.Optional[str] = None
    cashRegisters: _t.Optional[str] = None

    def createHq(self) -> None:
        """Operation."""
        raise NotImplementedError

    def createStore(self) -> None:
        """Operation."""
        raise NotImplementedError

    def createBackOffice(self) -> None:
        """Operation."""
        raise NotImplementedError

    def createCashRegister(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Hq:
    """Source: R8, R9"""
    name: _t.Optional[str] = None

    def manageStores(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Store:
    """Source: R3, R10"""
    name: _t.Optional[str] = None
    office: _t.Optional["Office"] = None

    def assignBackOffice(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Office:
    """Source: R4"""
    name: _t.Optional[str] = None


@_dc.dataclass
class CashRegister:
    """Source: R7"""
    name: _t.Optional[str] = None
