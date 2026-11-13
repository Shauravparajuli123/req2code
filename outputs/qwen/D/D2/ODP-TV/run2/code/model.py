"""Code skeleton generated from the shared model of D2/ODP-TV.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class TechnologyObject:
    """Source: R1, R5, R8"""
    pass


@_dc.dataclass
class ImplementableStandard(TechnologyObject):
    """Source: R4, R8"""
    pass


@_dc.dataclass
class Implementation:
    """Source: R2, R6"""
    pass


@_dc.dataclass
class IXIT(Implementation):
    """Source: R3, R7"""
    pass
