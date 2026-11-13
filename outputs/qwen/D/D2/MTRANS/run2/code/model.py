"""Code skeleton generated from the shared model of D2/MTRANS.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class MTRANSModel:
    """Source: R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17"""
    modules: _t.Optional[str] = None
    rules: _t.Optional[str] = None
    inheritances: _t.Optional[str] = None
    expressions: _t.Optional[str] = None
    sections: _t.Optional[str] = None
    variables: _t.Optional[str] = None

    def addModule(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addRule(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addInheritance(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addExpression(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addSection(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addVariable(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Module:
    """Source: R3, R10, R11, R12, R13"""
    name: _t.Optional[str] = None
    rules: _t.List["Rule"] = _dc.field(default_factory=list)

    def createModule(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Rule:
    """Source: R4, R11, R12, R13, R14, R15"""
    moduleName: _t.Optional[str] = None
    abstract_: _t.Optional[bool] = None
    name: _t.Optional[str] = None
    sections: _t.Optional[str] = None
    inheritances: _t.Optional[str] = None
    source: _t.Optional[str] = None
    variables: _t.List["Variable"] = _dc.field(default_factory=list)
    module: _t.Optional["Module"] = None

    def addSection(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addInheritance(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Inheritance:
    """Source: R5, R15, R16"""
    ruleName: _t.Optional[str] = None
    rule: _t.Optional[str] = None

    def createInheritance(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Expression:
    """Source: R6, R18, R19"""
    instruction: _t.Optional[str] = None
    inheritance: _t.Optional["Inheritance"] = None

    def createExpression(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Section:
    """Source: R7, R20"""
    kind: _t.Optional[str] = None

    def addSection(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Instruction:
    """Source: R19, R21"""
    expression: _t.Optional["Expression"] = None

    def createInstruction(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Variable:
    """Source: R22"""
    ruleName: _t.Optional[str] = None

    def addVariable(self) -> None:
        """Operation."""
        raise NotImplementedError
