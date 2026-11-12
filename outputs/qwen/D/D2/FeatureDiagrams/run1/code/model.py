"""Code skeleton generated from the shared model of D2/FeatureDiagrams.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: R1, R7, R9, R10, R12, R13"""
    description: _t.Optional[str] = None
    object_: _t.Optional[str] = None
    attribute: _t.Optional[str] = None
    xORGroup: _t.Optional[str] = None
    oRGroup: _t.Optional[str] = None
    node: _t.Optional[str] = None
    attributes: _t.List["Attribute"] = _dc.field(default_factory=list)

    def addAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addXORGroup(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addORGroup(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Attribute:
    """Source: R2, R9"""
    description: _t.Optional[str] = None
    name: _t.Optional[str] = None
    key: _t.Optional[bool] = None
    node: _t.Optional[str] = None

    def createAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class XORGroup:
    """Source: R5, R8"""
    preliminary: _t.Optional[bool] = None

    def addNode(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ORGroup:
    """Source: R6, R11"""
    preliminary: _t.Optional[bool] = None

    def addNode(self) -> None:
        """Operation."""
        raise NotImplementedError
