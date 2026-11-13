"""Code skeleton generated from the shared model of D2/UDDI_meta-model_fragment.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Model:
    """Source: R6, R10"""
    overviewDocuments: _t.Optional[str] = None


@_dc.dataclass
class BusinessEntity(Model):
    """Source: R4, R9"""
    identifiers: _t.Optional[str] = None
    businessContacts: _t.Optional[str] = None
    services: _t.Optional[str] = None
    businessContact: _t.Optional["BusinessContact"] = None


@_dc.dataclass
class IdentifierBag:
    """Source: R5"""
    identifiers: _t.Optional[str] = None


@_dc.dataclass
class BusinessContact:
    """Source: R2"""
    contact: _t.Optional[str] = None


@_dc.dataclass
class Service:
    """Source: R3"""
    service: _t.Optional[str] = None


@_dc.dataclass
class OverviewDocument:
    """Source: R7"""
    document: _t.Optional[str] = None


@_dc.dataclass
class BusinessTemplate:
    """Source: R1"""
    template: _t.Optional[str] = None
