"""Code skeleton generated from the shared model of D2/News.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class News:
    """Source: R1"""
    title: _t.Optional[str] = None
    link: _t.Optional[str] = None
    author: _t.Optional[str] = None

    def publishOn(self) -> None:
        """Operation."""
        raise NotImplementedError
