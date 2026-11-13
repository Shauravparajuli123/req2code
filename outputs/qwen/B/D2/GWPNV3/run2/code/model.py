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
    place: _t.Optional["Place"] = None
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
class Transition:
    """Source: -"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None
    outgoingArcs: _t.Optional[str] = None


@_dc.dataclass
class TpaArc:
    """Source: -"""
    src: _t.Optional[str] = None
    dst: _t.Optional[str] = None
