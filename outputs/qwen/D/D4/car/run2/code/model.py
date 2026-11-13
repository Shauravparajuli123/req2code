"""Code skeleton generated from the shared model of D4/car.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Car:
    """Source: R1"""
    numberPlate: _t.Optional[str] = None
    wheel: _t.Optional["Wheel"] = None
    engine: _t.Optional["Engine"] = None
    seats: _t.List["Seat"] = _dc.field(default_factory=list)
    make: _t.Optional["Make"] = None


@_dc.dataclass
class Wheel:
    """Source: -"""
    diameter: _t.Optional[float] = None

    def createWheel(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Engine:
    """Source: -"""
    power: _t.Optional[int] = None

    def createEngine(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Seat:
    """Source: -"""
    size: _t.Optional[int] = None

    def createSeat(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Make:
    """Source: R2"""
    name: _t.Optional[str] = None

    def createMake(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Model:
    """Source: R2"""
    name: _t.Optional[str] = None
    make: _t.Optional["Make"] = None

    def createModel(self) -> None:
        """Operation."""
        raise NotImplementedError
