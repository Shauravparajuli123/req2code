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
    identifierBag: _t.Optional[str] = None
    contacts: _t.List["Contact"] = _dc.field(default_factory=list)

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
    identifiers: _t.Optional[str] = None


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
    businessTemplate: _t.Optional[str] = None

    def addBusinessTemplate(self) -> None:
        """Operation."""
        raise NotImplementedError


class Identifier(_enum.Enum):
    """Source: -"""
    STRING = "STRING"


class BusinessContactType(_enum.Enum):
    """Source: -"""
    STRING = "STRING"
