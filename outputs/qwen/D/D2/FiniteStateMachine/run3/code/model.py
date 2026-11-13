"""Code skeleton generated from the shared model of D2/FiniteStateMachine.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class State:
    """Source: -"""
    associationStates: _t.List["AssociationState"] = _dc.field(default_factory=list)


@_dc.dataclass
class StateMachine:
    """Source: -"""
    rootFolder: _t.Optional["RootFolder"] = None


@_dc.dataclass
class RootFolder:
    """Source: R5, R10, R12"""
    name: _t.Optional[str] = None


@_dc.dataclass
class AssociationState:
    """Source: R13, R14"""
    states: _t.List["State"] = _dc.field(default_factory=list)
