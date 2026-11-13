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
class StateMachine:
    """Source: -"""
    name: _t.Optional[str] = None
    rootFolder: _t.Optional[str] = None
    transitions: _t.List["Transition"] = _dc.field(default_factory=list)

    def addTransition(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RootFolder:
    """Source: R5, R12"""
    name: _t.Optional[str] = None
    subFolders: _t.Optional[str] = None


@_dc.dataclass
class State:
    """Source: R8, R9"""
    stateMachine: _t.Optional[str] = None
    associationStateSources: _t.Optional[str] = None


@_dc.dataclass
class AssociationState(State):
    """Source: R13, R14"""
    transition: _t.Optional[str] = None
    sourceStates: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R7, R11"""
    stateMachine: _t.Optional[str] = None
    states: _t.Optional[str] = None
