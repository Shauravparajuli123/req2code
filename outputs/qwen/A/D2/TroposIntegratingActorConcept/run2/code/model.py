"""Code skeleton generated from the shared model of D2/TroposIntegratingActorConcept.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Agent:
    """Source: R2, R5"""
    position: _t.Optional[str] = None
    role: _t.Optional[str] = None

    def occupyPosition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Position:
    """Source: R3, R5"""
    roles: _t.List["Role"] = _dc.field(default_factory=list)


@_dc.dataclass
class Role:
    """Source: R4, R6"""
    pass
