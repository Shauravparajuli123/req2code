"""Code skeleton generated from the shared model of D2/WfMC.
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
class ProcessDefinition:
    """Source: R15, R17"""
    pass


@_dc.dataclass
class ProcessActivity:
    """Source: R13, R16, R18"""
    processDefinition: _t.Optional["ProcessDefinition"] = None


@_dc.dataclass
class TransitionInformation:
    """Source: R20, R21"""
    workflowProcessActivity: _t.Optional[str] = None


@_dc.dataclass
class WorkflowProcessDefinition:
    """Source: R7, R8, R9"""
    processDefinitions: _t.Optional[str] = None
    workflowApplicationDeclarations: _t.Optional[str] = None
    transitionDefinitions: _t.Optional[str] = None
    processDefinition: _t.Optional["ProcessDefinition"] = None
    transitionInformations: _t.List["TransitionInformation"] = _dc.field(default_factory=list)
