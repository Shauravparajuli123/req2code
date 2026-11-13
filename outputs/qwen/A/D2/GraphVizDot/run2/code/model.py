"""Code skeleton generated from the shared model of D2/GraphVizDot.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Graph:
    """Source: R3"""
    type: _t.Optional[str] = None
    dimension: _t.Optional[int] = None
    elements: _t.Optional[str] = None
    graphElements: _t.List["GraphElement"] = _dc.field(default_factory=list)
    subGraphs: _t.List["SubGraph"] = _dc.field(default_factory=list)


@_dc.dataclass
class GraphElement:
    """Source: R4"""
    label: _t.Optional[str] = None
    zIndex: _t.Optional[int] = None
    parentGraph: _t.Optional[str] = None
    nodes: _t.List["Node"] = _dc.field(default_factory=list)
    directedArcs: _t.List["DirectedArc"] = _dc.field(default_factory=list)
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
