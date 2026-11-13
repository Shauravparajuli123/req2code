"""Code skeleton generated from the shared model of D2/MTRANS.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Module:
    """Source: R3, R10, R11, R12, R13"""
    name: _t.Optional[str] = None
    rules: _t.Optional[str] = None


@_dc.dataclass
class Rule:
    """Source: R4, R12, R13, R14, R15"""
    name: _t.Optional[str] = None
    abstract_: _t.Optional[bool] = None
    sections: _t.Optional[str] = None
    source: _t.Optional[str] = None
    inheritances: _t.Optional[str] = None
    variables: _t.List["Variable"] = _dc.field(default_factory=list)

    def addSection(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Section:
    """Source: R7, R20"""
    kind: _t.Optional[str] = None


@_dc.dataclass
class Inheritance:
    """Source: R5, R16, R17"""
    rule: _t.Optional[str] = None


@_dc.dataclass
class MetaClass:
    """Source: R1, R2, R13"""
    pass


@_dc.dataclass
class Expression:
    """Source: R18, R19"""
    instruction: _t.Optional[str] = None


@_dc.dataclass
class Instruction:
    """Source: R19"""
    expression: _t.Optional["Expression"] = None


@_dc.dataclass
class Variable:
    """Source: R22"""
    rule: _t.Optional[str] = None


class InheritedRule(_enum.Enum):
    """Source: R18"""
    INHERITEDRULE = "INHERITEDRULE"
