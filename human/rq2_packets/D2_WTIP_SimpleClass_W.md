# Artefact set D2_WTIP_SimpleClass_W

## Use cases
(none)

## Class diagram
- Game: attributes ['name']; methods ['createGame']

## Python code
```python
"""Code skeleton generated from the shared model of D2/WTIP_SimpleClass.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError

```