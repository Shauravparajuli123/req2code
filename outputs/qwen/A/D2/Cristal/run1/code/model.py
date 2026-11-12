"""Code skeleton generated from the shared model of D2/Cristal.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Condition:
    """Source: R1"""
    pass


@_dc.dataclass
class CompositeParDef:
    """Source: R2"""
    partCompositeMembers: _t.List["PartCompositeMember"] = _dc.field(default_factory=list)


@_dc.dataclass
class ElementaryPartDef:
    """Source: R3"""
    pass


@_dc.dataclass
class ElementaryActDef:
    """Source: R4"""
    pass


@_dc.dataclass
class CompositeActDef:
    """Source: R5"""
    actCompositeMembers: _t.List["ActCompositeMember"] = _dc.field(default_factory=list)


@_dc.dataclass
class ActCompositeMember:
    """Source: R6"""
    pass


@_dc.dataclass
class Cristal:
    """Source: R7, R8, R9, R10, R11, R12, R13, R14, R15, R16"""
    activityDefinitions: _t.Optional[str] = None
    partDefinitions: _t.Optional[str] = None
    partCompositeMembers: _t.Optional[str] = None
    compositeActDefs: _t.Optional[str] = None
    compositeParDefs: _t.Optional[str] = None
    condition: _t.Optional["Condition"] = None
    actCompositeMembers: _t.List["ActCompositeMember"] = _dc.field(default_factory=list)
    elementaryActDefs: _t.List["ElementaryActDef"] = _dc.field(default_factory=list)
    elementaryPartDefs: _t.List["ElementaryPartDef"] = _dc.field(default_factory=list)

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ActivityDefinition:
    """Source: R13, R14"""
    actCompositeMember: _t.Optional[str] = None


@_dc.dataclass
class PartCompositeMember:
    """Source: R9, R10, R11, R16"""
    partDefinition: _t.Optional[str] = None
