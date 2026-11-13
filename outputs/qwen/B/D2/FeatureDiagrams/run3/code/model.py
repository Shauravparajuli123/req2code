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
    reference: _t.Optional[str] = None
    attribute: _t.Optional[str] = None
    attributes: _t.List["Attribute"] = _dc.field(default_factory=list)
    xorgroups: _t.List["Xorgroup"] = _dc.field(default_factory=list)

    def addNode(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addChild(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Attribute:
    """Source: R2, R9"""
    description: _t.Optional[str] = None
    name: _t.Optional[str] = None
    key: _t.Optional[bool] = None


@_dc.dataclass
class Orgroup:
    """Source: R6, R13, R11"""
    preliminary: _t.Optional[bool] = None
    nodes: _t.List["Node"] = _dc.field(default_factory=list)
    xorgroups: _t.List["Xorgroup"] = _dc.field(default_factory=list)

    def addNode(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Xorgroup(Orgroup):
    """Source: R5, R8, R12"""
    preliminary: _t.Optional[bool] = None
    nodes: _t.List["Node"] = _dc.field(default_factory=list)
    orgroups: _t.List["Orgroup"] = _dc.field(default_factory=list)

    def addNode(self) -> None:
        """Operation."""
        raise NotImplementedError
