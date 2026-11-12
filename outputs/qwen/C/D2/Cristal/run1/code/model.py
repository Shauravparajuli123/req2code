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
    activityDefinitions: _t.Optional[str] = None
    partCompositeMember: _t.Optional["PartCompositeMember"] = None
    compositeParDefs: _t.List["CompositeParDef"] = _dc.field(default_factory=list)
    compositeActDefs: _t.List["CompositeActDef"] = _dc.field(default_factory=list)

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
class ElementaryActDef:
    """Source: R4"""
    pass


@_dc.dataclass
class ElementaryPartDef:
    """Source: R3"""
    pass


@_dc.dataclass
class CompositeActDef:
    """Source: R5"""
    actCompositeMembers: _t.Optional[str] = None


@_dc.dataclass
class ActCompositeMember:
    """Source: R6"""
    activityDefinitions: _t.Optional[str] = None


@_dc.dataclass
class ActivityDefinition:
    """Source: R14"""
    actCompositeMember: _t.Optional[str] = None


@_dc.dataclass
class PartCompositeMember:
    """Source: R9"""
    partDefinition: _t.Optional[str] = None


@_dc.dataclass
class PartDefinitionNode:
    """Source: R16"""
    partCompositeMember: _t.Optional[str] = None
