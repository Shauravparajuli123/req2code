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
    engine: _t.Optional["Engine"] = None
    seats: _t.List["Seat"] = _dc.field(default_factory=list)
    wheel: _t.Optional["Wheel"] = None


@_dc.dataclass
class Make:
    """Source: R4"""
    name: _t.Optional[str] = None
    model: _t.Optional["Model"] = None


@_dc.dataclass
class Model:
    """Source: R4"""
    name: _t.Optional[str] = None
    make: _t.Optional["Make"] = None
    car: _t.Optional["Car"] = None


@_dc.dataclass
class Engine:
    """Source: R6"""
    power: _t.Optional[int] = None


@_dc.dataclass
class Seat:
    """Source: R7"""
    size: _t.Optional[int] = None


@_dc.dataclass
class Wheel:
    """Source: R5"""
    diameter: _t.Optional[float] = None
