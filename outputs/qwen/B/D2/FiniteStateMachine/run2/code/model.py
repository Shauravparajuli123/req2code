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
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RootFolder:
    """Source: R5, R10, R12"""
    name: _t.Optional[str] = None


@_dc.dataclass
class StateMachine:
    """Source: R4, R8, R10, R11"""
    rootFolder: _t.Optional[str] = None


@_dc.dataclass
class State:
    """Source: R3, R8, R9"""
    stateMachine: _t.Optional[str] = None
    associationStateSources: _t.Optional[str] = None


@_dc.dataclass
class AssociationState:
    """Source: R13, R14"""
    transition: _t.Optional[str] = None
    sourceStates: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R7, R13"""
    stateMachine: _t.Optional[str] = None
    stateMachines: _t.List["StateMachine"] = _dc.field(default_factory=list)
