"""Code skeleton generated from the shared model of D2/EclipseLaunchConfigurations.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Attribute:
    """Source: R2"""
    key: _t.Optional[str] = None
    stringAttribute: _t.Optional["StringAttribute"] = None
    booleanAttribute: _t.Optional["BooleanAttribute"] = None


@_dc.dataclass
class StringAttribute:
    """Source: R3"""
    value: _t.Optional[str] = None
    attribute: _t.Optional["Attribute"] = None


@_dc.dataclass
class BooleanAttribute:
    """Source: R4"""
    value: _t.Optional[bool] = None
    attribute: _t.Optional["Attribute"] = None


@_dc.dataclass
class MapAttribute:
    """Source: R5"""
    entries: _t.Optional[str] = None
    attribute: _t.Optional["Attribute"] = None
    mapEntries: _t.List["MapEntry"] = _dc.field(default_factory=list)


@_dc.dataclass
class MapEntry:
    """Source: R11"""
    key: _t.Optional[str] = None
    value: _t.Optional[str] = None
    mapAttribute: _t.Optional["MapAttribute"] = None
    stringAttribute: _t.Optional["StringAttribute"] = None


@_dc.dataclass
class ListAttribute:
    """Source: R7"""
    entries: _t.Optional[str] = None
    attribute: _t.Optional["Attribute"] = None
    listEntries: _t.List["ListEntry"] = _dc.field(default_factory=list)


@_dc.dataclass
class ListEntry:
    """Source: R13"""
    value: _t.Optional[str] = None
    listAttribute: _t.Optional["ListAttribute"] = None
    stringAttribute: _t.Optional["StringAttribute"] = None


@_dc.dataclass
class LaunchConfiguration:
    """Source: R9"""
    attributes: _t.Optional[str] = None

    def addAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError
