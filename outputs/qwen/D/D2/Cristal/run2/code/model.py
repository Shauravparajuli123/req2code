"""Code skeleton generated from the shared model of D2/Cristal.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Condition:
    """Source: R10"""
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
    activityDefinition: _t.Optional["ActivityDefinition"] = None


@_dc.dataclass
class ActivityDefinition:
    """Source: R13, R14"""
    pass


@_dc.dataclass
class PartCompositeMember:
    """Source: R9, R15, R16"""
    partDefinition: _t.Optional[str] = None
    compositeParDef: _t.Optional[str] = None
    compositeActDef: _t.Optional[str] = None
    activityDefinition: _t.Optional[str] = None

    def addActivityDefinition(self) -> None:
        """Operation."""
        raise NotImplementedError
