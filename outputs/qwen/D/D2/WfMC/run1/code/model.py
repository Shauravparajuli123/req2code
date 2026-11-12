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
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class WorkflowProcessDefinition:
    """Source: R8, R9, R10"""
    participantSpecification: _t.Optional["ParticipantSpecification"] = None


@_dc.dataclass
class ParticipantSpecification:
    """Source: R15, R16"""
    processDefinition: _t.Optional[str] = None
    processActivity: _t.Optional[str] = None


@_dc.dataclass
class WorkflowProcessActivity:
    """Source: R13, R14, R17, R18"""
    processDefinition: _t.Optional[str] = None
    relevantData: _t.Optional[str] = None
    transitionInformation: _t.Optional["TransitionInformation"] = None
    workflowProcessDefinition: _t.Optional["WorkflowProcessDefinition"] = None


@_dc.dataclass
class TransitionInformation:
    """Source: R20, R21"""
    targetActivity: _t.Optional[str] = None
