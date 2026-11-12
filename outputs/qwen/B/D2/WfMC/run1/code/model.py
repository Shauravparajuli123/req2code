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
class WorkflowProcessDefinition:
    """Source: R8, R9, R10"""
    workflowParticipants: _t.Optional[str] = None
    workflowApplicationDeclarations: _t.Optional[str] = None
    transitionDefinitions: _t.Optional[str] = None
    participantSpecification: _t.Optional["ParticipantSpecification"] = None
    transitionInformations: _t.List["TransitionInformation"] = _dc.field(default_factory=list)


@_dc.dataclass
class ParticipantSpecification:
    """Source: R15"""
    processDefinition: _t.Optional[str] = None


@_dc.dataclass
class WorkflowApplicationDeclaration:
    """Source: R11"""
    relevantData: _t.Optional[str] = None


@_dc.dataclass
class TransitionInformation:
    """Source: R20, R21"""
    targetProcessActivity: _t.Optional[str] = None
    workflowProcessActivity: _t.Optional["WorkflowProcessActivity"] = None


@_dc.dataclass
class WorkflowProcessActivity:
    """Source: R13, R16, R17, R18"""
    processDefinition: _t.Optional[str] = None
    relevantData: _t.Optional[str] = None


@_dc.dataclass
class ProcessDefinition:
    """Source: R10, R17"""
    pass


@_dc.dataclass
class WfMc:
    """Source: R4"""
    pass
