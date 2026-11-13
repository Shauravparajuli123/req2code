"""Code skeleton generated from the shared model of D4/airlines.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Airline:
    """Source: R2"""
    name: _t.Optional[str] = None
    airport: _t.Optional["Airport"] = None
    operatingCost: _t.Optional["OperatingCost"] = None

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
    """Source: R1"""
    code: _t.Optional[str] = None
    city: _t.Optional[str] = None


@_dc.dataclass
class OperatingCost:
    """Source: R5"""
    cost: _t.Optional[float] = None
