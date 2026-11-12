"""Code skeleton generated from the shared model of D2/Contact.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Contact:
    """Source: R1"""
    name: _t.Optional[str] = None
    phoneNumbers: _t.List["PhoneNumber"] = _dc.field(default_factory=list)


@_dc.dataclass
class PhoneNumber:
    """Source: -"""
    number: _t.Optional[str] = None
    type: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError
