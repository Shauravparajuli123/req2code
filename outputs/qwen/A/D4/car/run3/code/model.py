"""Code skeleton generated from the shared model of D4/car.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Car:
    """Source: R1"""
    name: _t.Optional[str] = None
    numberPlate: _t.Optional[str] = None
    engine: _t.Optional["Engine"] = None
    seats: _t.List["Seat"] = _dc.field(default_factory=list)
    wheel: _t.Optional["Wheel"] = None

    def createCar(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Make:
    """Source: R2"""
    name: _t.Optional[str] = None
    models: _t.List["Model"] = _dc.field(default_factory=list)


@_dc.dataclass
class Model(Make):
    """Source: R2"""
    name: _t.Optional[str] = None
    make: _t.Optional[str] = None


@_dc.dataclass
class Wheel:
    """Source: R5"""
    diameter: _t.Optional[float] = None


@_dc.dataclass
class Engine:
    """Source: R6"""
    power: _t.Optional[int] = None


@_dc.dataclass
class Seat:
    """Source: R7"""
    size: _t.Optional[int] = None
