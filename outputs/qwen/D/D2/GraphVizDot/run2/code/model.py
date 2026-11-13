"""Code skeleton generated from the shared model of D2/GraphVizDot.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Graph:
    """Source: R3, R9"""
    type: _t.Optional[str] = None
    dimension: _t.Optional[int] = None
    elements: _t.Optional[str] = None
    graphElements: _t.List["GraphElement"] = _dc.field(default_factory=list)
    graphElement: _t.Optional["GraphElement"] = None


@_dc.dataclass
class GraphElement:
    """Source: R2, R4, R10"""
    label: _t.Optional[str] = None
    zIndex: _t.Optional[int] = None
    parentGraph: _t.Optional[str] = None
    graph: _t.Optional["Graph"] = None


@_dc.dataclass
class Node:
    """Source: R5"""
    shape: _t.Optional[str] = None


@_dc.dataclass
class DirectedArc:
    """Source: R6"""
    sourceNode: _t.Optional[str] = None
    targetNode: _t.Optional[str] = None
    shape: _t.Optional[str] = None


@_dc.dataclass
class Constraint:
    """Source: R7"""
    value: _t.Optional[str] = None


@_dc.dataclass
class SubGraph:
    """Source: R8"""
    pass
