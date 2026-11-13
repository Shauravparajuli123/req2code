"""Code skeleton generated from the shared model of D2/TextualPathExp.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class TextualPathExp:
    """Source: R1"""
    path: _t.Optional[str] = None


@_dc.dataclass
class Path:
    """Source: -"""
    transitions: _t.Optional[str] = None
    alternativeTrans: _t.Optional["AlternativeTrans"] = None
    primitiveTranses: _t.List["PrimitiveTrans"] = _dc.field(default_factory=list)


@_dc.dataclass
class Transition:
    """Source: -"""
    pass


@_dc.dataclass
class AlternativeTrans:
    """Source: R8"""
    name: _t.Optional[str] = None
    paths: _t.Optional[str] = None


@_dc.dataclass
class PrimitiveTrans:
    """Source: R5"""
    name: _t.Optional[str] = None
