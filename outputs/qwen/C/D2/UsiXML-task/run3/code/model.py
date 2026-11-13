"""Code skeleton generated from the shared model of D2/UsiXML-task.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: -"""
    identifier: _t.Optional[str] = None
    category: _t.Optional[str] = None
    taskType: _t.Optional[str] = None
    importance: _t.Optional[int] = None
    complexityLevel: _t.Optional[int] = None
    centrality: _t.Optional[int] = None
    tasks: _t.List["Task"] = _dc.field(default_factory=list)


@_dc.dataclass
class Task:
    """Source: R6, R7, R8, R9, R10"""
    node: _t.Optional["Node"] = None

    def createTask(self) -> None:
        """Operation."""
        raise NotImplementedError

    def decomposeTask(self) -> None:
        """Operation."""
        raise NotImplementedError

    def associateExpression(self) -> None:
        """Operation."""
        raise NotImplementedError

    def associateOperator(self) -> None:
        """Operation."""
        raise NotImplementedError

    def actOnTask(self) -> None:
        """Operation."""
        raise NotImplementedError
