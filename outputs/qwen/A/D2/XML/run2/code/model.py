"""Code skeleton generated from the shared model of D2/XML.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: R1"""
    name: _t.Optional[str] = None
    startLine: _t.Optional[int] = None
    endLine: _t.Optional[int] = None
    element: _t.Optional["Element"] = None


@_dc.dataclass
class Element:
    """Source: -"""
    nodes: _t.List["Node"] = _dc.field(default_factory=list)

    def addChildNode(self) -> None:
        """Operation."""
        raise NotImplementedError

    def getParent(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Text:
    """Source: R3"""
    elements: _t.List["Element"] = _dc.field(default_factory=list)


@_dc.dataclass
class Root:
    """Source: R5"""
    elements: _t.List["Element"] = _dc.field(default_factory=list)
