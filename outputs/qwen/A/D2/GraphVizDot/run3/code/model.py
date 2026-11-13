"""Code skeleton generated from the shared model of D2/GraphVizDot.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class GraphElement:
    """Source: R2, R4, R10"""
    name: _t.Optional[str] = None
    label: _t.Optional[str] = None
    zIndex: _t.Optional[int] = None
    parentGraph: _t.Optional[str] = None
    nodes: _t.List["Node"] = _dc.field(default_factory=list)
    directedArcs: _t.List["DirectedArc"] = _dc.field(default_factory=list)
    graph: _t.Optional["Graph"] = None

    def createGraphElement(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Node:
    """Source: R5, R1, R9"""
    name: _t.Optional[str] = None
    label: _t.Optional[str] = None
    zIndex: _t.Optional[int] = None
    shape: _t.Optional[str] = None
    parentGraph: _t.Optional[str] = None

    def createNode(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class DirectedArc:
    """Source: R6, R1, R9"""
    name: _t.Optional[str] = None
    label: _t.Optional[str] = None
    zIndex: _t.Optional[int] = None
    sourceNode: _t.Optional[str] = None
    targetNode: _t.Optional[str] = None
    shape: _t.Optional[str] = None
    parentGraph: _t.Optional[str] = None

    def createDirectedArc(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Graph:
    """Source: R3, R9"""
    type: _t.Optional[str] = None
    dimension: _t.Optional[int] = None
    elements: _t.Optional[str] = None
    graphElements: _t.List["GraphElement"] = _dc.field(default_factory=list)
    subGraphs: _t.List["SubGraph"] = _dc.field(default_factory=list)

    def createGraph(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class SubGraph:
    """Source: R8"""
    name: _t.Optional[str] = None
    value: _t.Optional[str] = None

    def createSubGraph(self) -> None:
        """Operation."""
        raise NotImplementedError
