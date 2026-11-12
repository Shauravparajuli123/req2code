# Artefact set D2_DXF_X

## Use cases
(none)

## Class diagram
- Mesh: attributes ['name', 'points']; methods []
- Point: attributes ['name', 'coordinatesX', 'coordinatesZ', 'mesh']; methods []
- Mesh --association--> Point

## Python code
```python
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


@_dc.dataclass
class Point:
    """Source: R3, R5, R6"""
    name: _t.Optional[str] = None
    coordinatesX: _t.Optional[float] = None
    coordinatesZ: _t.Optional[float] = None
    mesh: _t.Optional[str] = None

```