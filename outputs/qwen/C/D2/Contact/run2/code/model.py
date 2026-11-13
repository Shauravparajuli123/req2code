"""Code skeleton generated from the shared model of D2/Contact.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Contact:
    """Source: R1"""
    name: _t.Optional[str] = None
    landLine: _t.Optional["LandLine"] = None


@_dc.dataclass
class Phone:
    """Source: R2, R3"""
    number: _t.Optional[str] = None


@_dc.dataclass
class LandLine:
    """Source: R5"""
    number: _t.Optional[str] = None


@_dc.dataclass
class CellPhone:
    """Source: R6"""
    number: _t.Optional[str] = None
