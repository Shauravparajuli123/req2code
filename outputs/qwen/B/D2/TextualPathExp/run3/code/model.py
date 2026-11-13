"""Code skeleton generated from the shared model of D2/TextualPathExp.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Path:
    """Source: R6"""
    transitions: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R7"""
    type: _t.Optional[str] = None


@_dc.dataclass
class AlternativeTrans:
    """Source: R8"""
    name: _t.Optional[str] = None
    paths: _t.List["Path"] = _dc.field(default_factory=list)

    def addPath(self) -> None:
        """Operation."""
        raise NotImplementedError
