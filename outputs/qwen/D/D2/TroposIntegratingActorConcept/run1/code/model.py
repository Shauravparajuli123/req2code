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
    """Source: R3"""
    role: _t.Optional[str] = None


class Role(_enum.Enum):
    """Source: R6"""
    CLASS_AND_ATTRIBUTE = "CLASS_AND_ATTRIBUTE"


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError
