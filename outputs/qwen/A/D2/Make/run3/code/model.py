"""Code skeleton generated from the shared model of D2/Make.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Makefile:
    """Source: R2, R10, R11"""
    name: _t.Optional[str] = None
    comments: _t.Optional[str] = None
    rules: _t.Optional[str] = None
    fileDependencies: _t.List["FileDependency"] = _dc.field(default_factory=list)
    comment: _t.Optional["Comment"] = None
    ruleDep: _t.Optional["RuleDep"] = None


@_dc.dataclass
class Rule:
    """Source: R3, R11, R12"""
    name: _t.Optional[str] = None
    shellLines: _t.Optional[str] = None
    dependencies: _t.Optional[str] = None
    ruleDeps: _t.List["RuleDep"] = _dc.field(default_factory=list)


@_dc.dataclass
class Comment:
    """Source: R6, R10"""
    text: _t.Optional[str] = None


@_dc.dataclass
class ShellLine:
    """Source: R5, R12"""
    command: _t.Optional[str] = None
    rules: _t.List["Rule"] = _dc.field(default_factory=list)


@_dc.dataclass
class RuleDep:
    """Source: R7, R11"""
    rule: _t.Optional[str] = None
    dependency: _t.Optional[str] = None


@_dc.dataclass
class FileDependency:
    """Source: R9"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Macro:
    """Source: R4"""
    value: _t.Optional[str] = None
