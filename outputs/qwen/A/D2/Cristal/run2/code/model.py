"""Code skeleton generated from the shared model of D2/Cristal.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Condition:
    """Source: R10"""
    partCompositeMember: _t.Optional["PartCompositeMember"] = None


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
    """Source: R12, R13"""
    pass


@_dc.dataclass
class PartCompositeMember:
    """Source: R9, R15, R16"""
    pass
