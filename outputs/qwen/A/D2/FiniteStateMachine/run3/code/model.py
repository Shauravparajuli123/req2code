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
class State:
    """Source: -"""
    stateMachine: _t.Optional[str] = None
    associationStateSources: _t.Optional[str] = None


@_dc.dataclass
class StateMachine:
    """Source: R10, R4"""
    rootFolder: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    states: _t.List["State"] = _dc.field(default_factory=list)
    associationState: _t.Optional["AssociationState"] = None


@_dc.dataclass
class RootFolder:
    """Source: R5, R12"""
    name: _t.Optional[str] = None
    rootFolders: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R7, R13"""
    stateMachine: _t.Optional[str] = None
    associationState: _t.Optional[str] = None
    stateMachines: _t.List["StateMachine"] = _dc.field(default_factory=list)


@_dc.dataclass
class AssociationState:
    """Source: R14"""
    transition: _t.Optional[str] = None
    sourceStates: _t.Optional[str] = None
