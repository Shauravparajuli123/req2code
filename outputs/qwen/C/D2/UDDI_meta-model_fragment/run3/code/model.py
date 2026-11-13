"""Code skeleton generated from the shared model of D2/UDDI_meta-model_fragment.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class BusinessEntity:
    """Source: R4, R9"""
    businessContact: _t.Optional[str] = None
    identifiers: _t.Optional[str] = None
    contact: _t.Optional["Contact"] = None
    identifierBag: _t.Optional["IdentifierBag"] = None

    def addBusinessContact(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Contact:
    """Source: R2"""
    pass


@_dc.dataclass
class IdentifierBag:
    """Source: -"""
    pass


@_dc.dataclass
class Model:
    """Source: R6, R10"""
    overviewDocuments: _t.Optional[str] = None
    overviewDocument: _t.Optional["OverviewDocument"] = None

    def addOverviewDocument(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class OverviewDocument:
    """Source: R7"""
    pass


@_dc.dataclass
class PifModel(Contact):
    """Source: R1"""
    businessTemplates: _t.Optional[str] = None

    def addBusinessTemplate(self) -> None:
        """Operation."""
        raise NotImplementedError


class BusinessTemplate(_enum.Enum):
    """Source: R1"""
    BUSINESS_TEMPLATE = "BUSINESS_TEMPLATE"
