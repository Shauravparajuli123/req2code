# Artefact set D2_EAI_Z

## Use cases
(none)

## Class diagram
- EAIResource: attributes []; methods []
- EAIQueue: attributes ['maxLength']; methods []
- EAISource: attributes ['resources']; methods ['createGame']
- EAISink: attributes ['resources']; methods ['createGame']
- FCMSource: attributes []; methods ['createGame']
- FCMSink: attributes []; methods ['createGame']
- FCMSource --association--> EAIResource
- EAISource --association--> EAIResource
- EAISink --association--> EAIResource
- EAISink --association--> FCMSink

## Python code
```python
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


@_dc.dataclass
class EAISource:
    """Source: R2"""
    resources: _t.Optional[str] = None
    eAIResource: _t.Optional["EAIResource"] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class FCMSink:
    """Source: R3"""

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class EAISink(FCMSink):
    """Source: R4"""
    resources: _t.Optional[str] = None
    eAIResource: _t.Optional["EAIResource"] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class FCMSource(EAIResource):
    """Source: R1"""

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError

```