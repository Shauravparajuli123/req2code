"""Code skeleton generated from the shared model of D2/GWPNV3.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Net:
    """Source: -"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    arcs: _t.Optional[str] = None
    tPArcs: _t.List["TPArc"] = _dc.field(default_factory=list)
    transition: _t.Optional["Transition"] = None


@_dc.dataclass
class Place:
    """Source: -"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None


@_dc.dataclass
class Arc:
    """Source: -"""
    src: _t.Optional[str] = None
    dst: _t.Optional[str] = None


@_dc.dataclass
class PTArc(Arc):
    """Source: R5"""
    name: _t.Optional[str] = None
    src: _t.Optional[str] = None
    dst: _t.Optional[str] = None


@_dc.dataclass
class TPArc(Arc):
    """Source: R6"""
    name: _t.Optional[str] = None
    src: _t.Optional[str] = None
    dst: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: -"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None
    outgoingArcs: _t.Optional[str] = None


@_dc.dataclass
class Model:
    """Source: R3"""
    name: _t.Optional[str] = None
    nets: _t.Optional[str] = None
