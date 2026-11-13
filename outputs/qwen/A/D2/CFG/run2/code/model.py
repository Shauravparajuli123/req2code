"""Code skeleton generated from the shared model of D2/CFG.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: R1, R2"""
    name: _t.Optional[str] = None

    def setInNode(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ConditionalNode(Node):
    """Source: R3, R7"""
    trueConditionNode: _t.Optional[str] = None
    node: _t.Optional["Node"] = None


@_dc.dataclass
class AbstractNode:
    """Source: R1, R5"""
    expression: _t.Optional[str] = None

    def setExpression(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Expression:
    """Source: R4"""
    name: _t.Optional[str] = None
