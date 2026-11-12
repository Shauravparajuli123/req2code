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
    value: _t.Optional[str] = None


class MapEntry(_enum.Enum):
    """Source: R11"""
    NAME____KEY____TYPE____STRING____SRC_____R2 = "NAME____KEY____TYPE____STRING____SRC_____R2"
    NAME____VALUE____TYPE____ATTRIBUTE____SRC_____R9 = "NAME____VALUE____TYPE____ATTRIBUTE____SRC_____R9"


@_dc.dataclass
class ListEntry:
    """Source: R12"""
    value: _t.Optional[str] = None
