"""Code skeleton generated from the shared model of D2/JavaSource.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class MethodDefinition:
    """Source: R5, R9"""
    method: _t.Optional[str] = None


@_dc.dataclass
class Class:
    """Source: R3, R6, R7"""
    name: _t.Optional[str] = None
    methodDefinitions: _t.List["MethodDefinition"] = _dc.field(default_factory=list)

    def invokeMethod(self) -> None:
        """Realizes UC2 "Invoke A Method" (R9)."""
        raise NotImplementedError
