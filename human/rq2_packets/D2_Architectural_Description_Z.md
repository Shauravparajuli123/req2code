# Artefact set D2_Architectural_Description_Z

## Use cases
(none)

## Class diagram
- ArchitectureDescription: attributes []; methods ['selectView', 'selectViewPoint', 'defineMainView']
- ArchitectureView: attributes []; methods ['conformToViewPoint', 'projectOntoMainView']
- MainView: attributes []; methods ['defineViewPoint']
- ArchitectureDescription --association--> ArchitectureView
- MainView --association--> ArchitectureView

## Python code
```python
"""Code skeleton generated from the shared model of D2/Architectural_Description.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class ArchitectureDescription:
    """Source: R7, R8, R9, R10, R11"""
    architectureViews: _t.List["ArchitectureView"] = _dc.field(default_factory=list)

    def selectView(self) -> None:
        """Operation."""
        raise NotImplementedError

    def selectViewPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def defineMainView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ArchitectureView:
    """Source: R7, R8, R9, R12"""

    def conformToViewPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def projectOntoMainView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class MainView:
    """Source: R11, R12"""
    architectureView: _t.Optional["ArchitectureView"] = None

    def defineViewPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

```