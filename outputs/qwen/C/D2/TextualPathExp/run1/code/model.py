"""Code skeleton generated from the shared model of D2/TextualPathExp.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Path:
    """Source: -"""
    transitions: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R3, R7"""
    type: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError
