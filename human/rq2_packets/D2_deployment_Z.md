# Artefact set D2_deployment_Z

## Use cases
(none)

## Class diagram
- Node: attributes ['name']; methods []
- CommunicationLink: attributes ['name', 'sourceNode']; methods []
- Deployment: attributes ['nodes', 'executionEnvironment']; methods []
- Nodes: attributes ['hierarchy']; methods []
- ExecutionEnvironment: attributes []; methods []
- Specification: attributes []; methods ['addNode']
- Deployment --association--> CommunicationLink
- Specification --association--> Node

## Python code
```python
"""Code skeleton generated from the shared model of D2/deployment.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Node:
    """Source: R1"""
    name: _t.Optional[str] = None


@_dc.dataclass
class CommunicationLink:
    """Source: R5, R8"""
    name: _t.Optional[str] = None
    sourceNode: _t.Optional[str] = None


@_dc.dataclass
class Deployment:
    """Source: R6, R7"""
    nodes: _t.Optional[str] = None
    executionEnvironment: _t.Optional[str] = None
    communicationLink: _t.Optional["CommunicationLink"] = None


@_dc.dataclass
class Nodes:
    """Source: R6, R7"""
    hierarchy: _t.Optional[str] = None


@_dc.dataclass
class ExecutionEnvironment:
    """Source: R3"""
    pass


@_dc.dataclass
class Specification:
    """Source: R4, R7"""
    node: _t.Optional["Node"] = None

    def addNode(self) -> None:
        """Operation."""
        raise NotImplementedError

```