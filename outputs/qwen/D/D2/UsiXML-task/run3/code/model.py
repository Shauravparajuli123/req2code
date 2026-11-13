"""Code skeleton generated from the shared model of D2/UsiXML-task.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class TaskNode:
    """Source: R1"""
    identifier: _t.Optional[str] = None
    category: _t.Optional[str] = None
    taskType: _t.Optional[str] = None
    importance: _t.Optional[int] = None
    complexityLevel: _t.Optional[int] = None
    centrality: _t.Optional[int] = None
    task: _t.Optional["Task"] = None

    def createTaskNode(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class Task:
    """Source: R6, R7, R8, R9, R10"""
    expression: _t.Optional[str] = None
    operator: _t.Optional[str] = None

    def associateOperator(self) -> None:
        """Operation."""
        raise NotImplementedError

    def associateExpression(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Expression:
    """Source: R2, R3, R4"""
    operator: _t.Optional["Operator"] = None


@_dc.dataclass
class Operator:
    """Source: R3, R4, R9, R10"""

    def operateOnTask(self) -> None:
        """Operation."""
        raise NotImplementedError
