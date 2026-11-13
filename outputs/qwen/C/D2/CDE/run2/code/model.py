"""Code skeleton generated from the shared model of D2/CDE.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class IumlType:
    """Source: R1"""
    iUmlMembers: _t.List["IUmlMember"] = _dc.field(default_factory=list)


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
    iCdeComponent: _t.Optional["ICdeComponent"] = None

    def implementComponent(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ICdeComponent:
    """Source: R6"""
    iCdeMembers: _t.List["ICdeMember"] = _dc.field(default_factory=list)


@_dc.dataclass
class ICdeMember:
    """Source: R8"""
    executionPerformance: _t.Optional[str] = None
    executionDetails: _t.Optional[str] = None


@_dc.dataclass
class IcdeComponentSpec:
    """Source: R2"""
    pass


@_dc.dataclass
class IUmlMember:
    """Source: R7"""
    pass
