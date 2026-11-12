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


@_dc.dataclass
class Element:
    """Source: -"""
    nodes: _t.List["Node"] = _dc.field(default_factory=list)
    attributeNodes: _t.List["AttributeNode"] = _dc.field(default_factory=list)

    def addChild(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AttributeNode:
    """Source: R2"""
    name: _t.Optional[str] = None

    def createAttributeNode(self) -> None:
        """Operation."""
        raise NotImplementedError
