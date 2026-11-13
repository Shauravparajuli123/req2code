"""Code skeleton generated from the shared model of D2/EAI.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class EAIResource:
    """Source: R5"""
    pass


@_dc.dataclass
class EAIQueue:
    """Source: -"""
    maxLength: _t.Optional[int] = None
    eAIResource: _t.Optional["EAIResource"] = None


@_dc.dataclass
class FCMSource:
    """Source: R1"""
    pass


@_dc.dataclass
class EAISource(FCMSource):
    """Source: R2"""

    def addResource(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class EAISink:
    """Source: R4, R8"""
    resources: _t.Optional[str] = None
    eAIResource: _t.Optional["EAIResource"] = None

    def addResource(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class FCMSink:
    """Source: R3"""
    pass
