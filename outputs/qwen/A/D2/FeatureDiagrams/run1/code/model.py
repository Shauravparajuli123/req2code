"""Code skeleton generated from the shared model of D2/FeatureDiagrams.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: R7, R9, R10, R11"""
    description: _t.Optional[str] = None
    object_: _t.Optional[str] = None
    attribute: _t.Optional[str] = None
    xorGroup: _t.Optional[str] = None
    orGroup: _t.Optional[str] = None
    nodes: _t.Optional[str] = None
    attributes: _t.List["Attribute"] = _dc.field(default_factory=list)
    xORGroups: _t.List["XORGroup"] = _dc.field(default_factory=list)
    oRGroups: _t.List["ORGroup"] = _dc.field(default_factory=list)

    def addAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addXorGroup(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addOrGroup(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addChild(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Attribute:
    """Source: R2"""
    description: _t.Optional[str] = None
    name: _t.Optional[str] = None
    key: _t.Optional[bool] = None


@_dc.dataclass
class XORGroup(Node):
    """Source: R5, R8, R12"""
    preliminary: _t.Optional[bool] = None


@_dc.dataclass
class ORGroup(Node):
    """Source: R6, R13"""
    preliminary: _t.Optional[bool] = None
