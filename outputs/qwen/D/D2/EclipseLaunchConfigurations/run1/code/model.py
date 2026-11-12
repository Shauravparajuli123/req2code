"""Code skeleton generated from the shared model of D2/EclipseLaunchConfigurations.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class LaunchConfiguration:
    """Source: R9"""
    attributes: _t.Optional[str] = None


@_dc.dataclass
class Attribute:
    """Source: R2"""
    key: _t.Optional[str] = None


@_dc.dataclass
class StringAttribute:
    """Source: R3"""
    stringValue: _t.Optional[str] = None


@_dc.dataclass
class BooleanAttribute:
    """Source: R4"""
    booleanValue: _t.Optional[bool] = None


@_dc.dataclass
class MapAttribute:
    """Source: R5, R10"""
    mapEntries: _t.Optional[str] = None


@_dc.dataclass
class MapEntry:
    """Source: R11"""
    pass


@_dc.dataclass
class ListAttribute:
    """Source: R7, R12"""
    listEntries: _t.Optional[str] = None


@_dc.dataclass
class ListEntry:
    """Source: R8, R13"""
    pass
