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
    transitions: _t.Optional[str] = None
    place: _t.Optional["Place"] = None
    tPArcs: _t.List["TPArc"] = _dc.field(default_factory=list)
    transition: _t.Optional["Transition"] = None
    pTArcs: _t.List["PTArc"] = _dc.field(default_factory=list)


@_dc.dataclass
class Place:
    """Source: -"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: -"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None
    outgoingArcs: _t.Optional[str] = None
    tPArcs: _t.List["TPArc"] = _dc.field(default_factory=list)


@_dc.dataclass
class PTArc:
    """Source: -"""
    srcPlace: _t.Optional[str] = None
    dstNet: _t.Optional[str] = None
    transition: _t.Optional["Transition"] = None


@_dc.dataclass
class TPArc:
    """Source: -"""
    srcTransition: _t.Optional[str] = None
    dstTransition: _t.Optional[str] = None
    transition: _t.Optional["Transition"] = None
