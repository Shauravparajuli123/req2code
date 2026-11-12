"""Code skeleton generated from the shared model of D4/airlines.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Airline:
    """Source: R2, R4"""
    name: _t.Optional[str] = None
    operationDetails: _t.Optional[str] = None
    operationDetailses: _t.List["OperationDetails"] = _dc.field(default_factory=list)
    airports: _t.List["Airport"] = _dc.field(default_factory=list)

    def startOperation(self) -> None:
        """Operation."""
        raise NotImplementedError

    def stopOperation(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updateOperatingCost(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Airport:
    """Source: R2"""
    code: _t.Optional[str] = None
    city: _t.Optional[str] = None


@_dc.dataclass
class OperationDetails:
    """Source: R3, R4"""
    operatingCost: _t.Optional[float] = None
    airport: _t.Optional["Airport"] = None
