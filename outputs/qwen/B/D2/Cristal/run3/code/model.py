"""Code skeleton generated from the shared model of D2/Cristal.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Cristal:
    """Source: -"""
    elementaryActDef: _t.Optional[str] = None
    elementaryPartDef: _t.Optional[str] = None
    compositeActDef: _t.Optional[str] = None
    compositeParDef: _t.Optional[str] = None
    condition: _t.Optional[str] = None
    partCompositeMember: _t.Optional["PartCompositeMember"] = None
    compositeParDefs: _t.List["CompositeParDef"] = _dc.field(default_factory=list)

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Condition:
    """Source: R1"""
    pass


@_dc.dataclass
class CompositeParDef:
    """Source: R2"""
    pass


@_dc.dataclass
class CompositeActDef:
    """Source: R5"""
    actCompositeMembers: _t.List["ActCompositeMember"] = _dc.field(default_factory=list)


@_dc.dataclass
class PartDefinitionNode:
    """Source: -"""
    partCompositeMemberNode: _t.Optional[str] = None
    partCompositeMember: _t.Optional["PartCompositeMember"] = None


@_dc.dataclass
class PartCompositeMember:
    """Source: R9, R10, R11, R12, R16"""
    activityDefinition: _t.Optional[str] = None
    actCompositeMember: _t.Optional[str] = None


@_dc.dataclass
class ActCompositeMember:
    """Source: R12, R13, R14"""
    activityDefinition: _t.Optional[str] = None


@_dc.dataclass
class ActivityDefinition:
    """Source: R13, R14"""
    actCompositeMember: _t.Optional[str] = None
