"""Code skeleton generated from the shared model of D2/useCase.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Actor:
    """Source: R1, R13"""
    name: _t.Optional[str] = None


@_dc.dataclass
class UseCase:
    """Source: R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12"""
    name: _t.Optional[str] = None
    containers: _t.Optional[str] = None
    actor: _t.Optional["Actor"] = None

    def include(self) -> None:
        """Realizes UC1 "Login" (R1, R2, R9)."""
        raise NotImplementedError

    def extend(self) -> None:
        """Realizes UC1 "Login" (R1, R2, R9)."""
        raise NotImplementedError


@_dc.dataclass
class UseCaseContainer:
    """Source: R12"""
    name: _t.Optional[str] = None
