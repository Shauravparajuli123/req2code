"""Code skeleton generated from the shared model of D2/TroposIntegratingActorConcept.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Agent:
    """Source: R2"""
    position: _t.Optional[str] = None

    def occupyPosition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Position:
    """Source: R3, R5"""
    role: _t.Optional[str] = None
    roles: _t.List["Role"] = _dc.field(default_factory=list)


class Role(_enum.Enum):
    """Source: R6"""
    CLASS = "CLASS"
    AGENT = "AGENT"
