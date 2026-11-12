# Artefact set D2_UIML-3_0_Z

## Use cases
(none)

## Class diagram
- Uiml: attributes ['head', 'interfaces']; methods []
- Header: attributes ['metas']; methods []
- MetaData: attributes ['name']; methods []
- Uiml --association--> Header
- Uiml --association--> MetaData
- MetaData --association--> Uiml

## Python code
```python
"""Code skeleton generated from the shared model of D2/UIML-3_0.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Uiml:
    """Source: R4"""
    head: _t.Optional[str] = None
    interfaces: _t.Optional[str] = None
    header: _t.Optional["Header"] = None
    metaDatas: _t.List["MetaData"] = _dc.field(default_factory=list)


@_dc.dataclass
class Header:
    """Source: R6"""
    metas: _t.Optional[str] = None


@_dc.dataclass
class MetaData:
    """Source: R3"""
    name: _t.Optional[str] = None
    uiml: _t.Optional["Uiml"] = None

```