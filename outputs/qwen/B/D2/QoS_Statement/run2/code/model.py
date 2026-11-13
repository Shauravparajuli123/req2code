"""Code skeleton generated from the shared model of D2/QoS_Statement.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class QoSStatement:
    """Source: R7, R8"""
    compoundQoSStatements: _t.List["CompoundQoSStatement"] = _dc.field(default_factory=list)


@_dc.dataclass
class SingleQoSStatement(QoSStatement):
    """Source: R9"""
    qosConstraint: _t.Optional[str] = None
    qoSConstraint: _t.Optional["QoSConstraint"] = None


@_dc.dataclass
class CompoundQoSStatement(QoSStatement):
    """Source: R3, R10"""
    qosStatements: _t.Optional[str] = None


@_dc.dataclass
class QoSConstraint:
    """Source: R5, R11"""
    qualificationKind: _t.Optional[str] = None


class QualificationKind(_enum.Enum):
    """Source: R11"""
    VALUE = "VALUE"
