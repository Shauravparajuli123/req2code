"""Code skeleton generated from the shared model of D2/UDDI_meta-model_fragment.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class IdentifierBag:
    """Source: R5"""
    identifiers: _t.Optional[str] = None


@_dc.dataclass
class BusinessEntity:
    """Source: R9"""
    identifiers: _t.Optional[str] = None
    businessContacts: _t.Optional[str] = None
    identifierBag: _t.Optional["IdentifierBag"] = None
    businessTemplates: _t.List["BusinessTemplate"] = _dc.field(default_factory=list)
    services: _t.List["Service"] = _dc.field(default_factory=list)

    def addBusinessContact(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class BusinessTemplate:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createTemplate(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Service:
    """Source: R3"""
    serviceDescription: _t.Optional[str] = None


@_dc.dataclass
class BusinessEntityModel:
    """Source: R4"""
    businessEntities: _t.Optional[str] = None
    model: _t.Optional["Model"] = None

    def addBusinessEntity(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Model:
    """Source: R10"""
    overviewDocuments: _t.Optional[str] = None

    def addOverviewDocument(self) -> None:
        """Operation."""
        raise NotImplementedError
