"""Code skeleton generated from the shared model of D2/WfMC.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class WorkflowProcessDefinition:
    """Source: R8, R15"""
    name: _t.Optional[str] = None
    participantSpecifications: _t.Optional[str] = None
    transitionInformation: _t.Optional["TransitionInformation"] = None

    def addSpecification(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Specification:
    """Source: R4, R15"""
    processDefinition: _t.Optional[str] = None


@_dc.dataclass
class ProcessDefinition:
    """Source: R5, R6, R7, R17"""
    name: _t.Optional[str] = None
    processActivities: _t.Optional[str] = None

    def addProcessActivity(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ProcessActivity:
    """Source: R13, R16, R17, R18, R19"""
    name: _t.Optional[str] = None
    processDefinition: _t.Optional[str] = None
    relevantData: _t.Optional[str] = None

    def addRelevantData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class TransitionInformation:
    """Source: R20, R21"""
    targetProcessActivity: _t.Optional[str] = None

    def setTargetProcessActivity(self) -> None:
        """Operation."""
        raise NotImplementedError
