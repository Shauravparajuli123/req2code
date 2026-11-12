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

    def createNode(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class ConditionalNode:
    """Source: R3, R7"""
    trueConditionNode: _t.Optional[str] = None
    node: _t.Optional["Node"] = None


@_dc.dataclass
class Expression:
    """Source: R5"""
    name: _t.Optional[str] = None
