"""Code skeleton generated from the shared model of D2/CDE.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class IumlType:
    """Source: R1"""
    pass


@_dc.dataclass
class IumlClass(IumlType):
    """Source: R3"""
    pass


@_dc.dataclass
class IumlComponent(IumlClass):
    """Source: R4"""
    pass


@_dc.dataclass
class ICdeServer:
    """Source: R5"""
    iCdeComponents: _t.List["ICdeComponent"] = _dc.field(default_factory=list)


@_dc.dataclass
class ICdeComponent:
    """Source: R6"""
    pass


@_dc.dataclass
class ICdeMember:
    """Source: R8"""
    pass


@_dc.dataclass
class ICdeMemberExe:
    """Source: -"""
    executionPerformance: _t.Optional[str] = None
    executionDetails: _t.Optional[str] = None
    iCdeMember: _t.Optional["ICdeMember"] = None
