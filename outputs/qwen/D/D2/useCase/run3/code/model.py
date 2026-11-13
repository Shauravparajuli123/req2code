"""Code skeleton generated from the shared model of D2/useCase.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1"""

    def login(self) -> None:
        """Realizes UC1 "Login" (R1)."""
        raise NotImplementedError

    def logout(self) -> None:
        """Realizes UC2 "Logout" (R1)."""
        raise NotImplementedError
