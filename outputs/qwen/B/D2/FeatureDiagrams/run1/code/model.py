"""Code skeleton generated from the shared model of D2/FeatureDiagrams.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: R1, R7, R9, R10, R11, R12, R13"""
    description: _t.Optional[str] = None
    reference: _t.Optional[str] = None
    attributes: _t.Optional[str] = None
    xorGroups: _t.Optional[str] = None
    orGroups: _t.Optional[str] = None
    xORGroups: _t.List["XORGroup"] = _dc.field(default_factory=list)
    oRGroups: _t.List["ORGroup"] = _dc.field(default_factory=list)

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


@_dc.dataclass
class XORGroup:
    """Source: R5, R8, R12"""
    preliminary: _t.Optional[bool] = None
    node: _t.Optional["Node"] = None


@_dc.dataclass
class ORGroup:
    """Source: R6, R11, R13"""
    preliminary: _t.Optional[bool] = None
    node: _t.Optional["Node"] = None
