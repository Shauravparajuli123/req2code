"""Code skeleton generated from the shared model of D2/DXF.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Mesh:
    """Source: R2, R4"""
    name: _t.Optional[str] = None
    points: _t.Optional[str] = None
    point: _t.Optional["Point"] = None

    def addPoint(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Point:
    """Source: R3, R6"""
    name: _t.Optional[str] = None
    x: _t.Optional[float] = None
    z: _t.Optional[float] = None
    mesh: _t.Optional[str] = None

    def setMesh(self) -> None:
        """Operation."""
        raise NotImplementedError
