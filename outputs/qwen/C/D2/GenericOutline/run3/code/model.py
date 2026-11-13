"""Code skeleton generated from the shared model of D2/GenericOutline.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: R3"""
    name: _t.Optional[str] = None
    icon: _t.Optional[str] = None
    maps: _t.Optional[str] = None
    label: _t.Optional["Label"] = None


@_dc.dataclass
class Label:
    """Source: R4"""
    label: _t.Optional[str] = None
    labelSuites: _t.Optional[str] = None


@_dc.dataclass
class LabelSuite:
    """Source: R5"""
    label: _t.Optional["Label"] = None


@_dc.dataclass
class Map:
    """Source: R6"""
    mapString: _t.Optional[str] = None


@_dc.dataclass
class Outline:
    """Source: R2"""
    extension: _t.Optional[str] = None
    nodes: _t.Optional[str] = None
