"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R15, R19, R28, R29, R39"""
    name: _t.Optional[str] = None
    emailId: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    activity: _t.Optional[str] = None
    stat: _t.Optional[str] = None
    recyclingCenter: _t.Optional["RecyclingCenter"] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R15)."""
        raise NotImplementedError

    def giveEmailId(self) -> None:
        """Realizes UC6 "Give Email Id" (R8)."""
        raise NotImplementedError

    def viewDocumentation(self) -> None:
        """Realizes UC30 "View User Documentation" (R13)."""
        raise NotImplementedError

    def viewErrorLog(self) -> None:
        """Realizes UC31 "View User Error Log" (R41)."""
        raise NotImplementedError


@_dc.dataclass
class Profile:
    """Source: R7"""
    favorites: _t.Optional[str] = None


@_dc.dataclass
class Facility:
    """Source: R3, R4, R5, R6, R10, R11, R36, R48"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None
    openingHours: _t.Optional[str] = None
    location: _t.Optional[str] = None
    materialAccepted: _t.Optional[str] = None
    environmentFriendly: _t.Optional[bool] = None


@_dc.dataclass
class Location:
    """Source: R9, R10, R36"""
    coordinates: _t.Optional[str] = None


@_dc.dataclass
class Material:
    """Source: R6"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Admin:
    """Source: R16, R17, R20, R22, R23, R42, R46, R47"""
    name: _t.Optional[str] = None
    dashboard: _t.Optional[str] = None
    recyclingCenterInformation: _t.Optional["RecyclingCenterInformation"] = None
    user: _t.Optional["User"] = None

    def addFacilityInfo(self) -> None:
        """Realizes UC14 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def removeFacilityInfo(self) -> None:
        """Realizes UC14 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def readFeedback(self) -> None:
        """Realizes UC15 "Read Feedback" (R17)."""
        raise NotImplementedError

    def viewStats(self) -> None:
        """Realizes UC29 "View Stat" (R44)."""
        raise NotImplementedError

    def communicateWithFacility(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Dashboard:
    """Source: R22, R46"""
    usageStats: _t.Optional[str] = None
    locations: _t.Optional[str] = None


@_dc.dataclass
class Executive:
    """Source: R24"""
    name: _t.Optional[str] = None
    company: _t.Optional[str] = None

    def viewCompanyInfo(self) -> None:
        """Realizes UC9 "Have Information" (R29)."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R19, R31"""
    name: _t.Optional[str] = None
    website: _t.Optional[str] = None
    companyAccountant: _t.Optional["CompanyAccountant"] = None


@_dc.dataclass
class CompanyAccountant:
    """Source: R33"""
    name: _t.Optional[str] = None
    website: _t.Optional[str] = None
    recyclingCenterInformation: _t.Optional["RecyclingCenterInformation"] = None

    def viewActivityFees(self) -> None:
        """Realizes UC23 "View Activity Fee" (R33)."""
        raise NotImplementedError


@_dc.dataclass
class Developer:
    """Source: R27, R34, R35"""
    name: _t.Optional[str] = None
    website: _t.Optional[str] = None

    def useBootstrap(self) -> None:
        """Realizes UC22 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendLessons(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingCenter:
    """Source: R16, R40, R42, R43"""
    name: _t.Optional[str] = None
    info: _t.Optional[str] = None
    location: _t.Optional["Location"] = None
    material: _t.Optional["Material"] = None
    recyclingfacilityRepresentative: _t.Optional["RecyclingfacilityRepresentative"] = None

    def addInfo(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updateInfo(self) -> None:
        """Realizes UC20 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingCenterInformation:
    """Source: R16, R40, R42, R43"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None
    recyclingCenter: _t.Optional["RecyclingCenter"] = None


@_dc.dataclass
class RecyclingfacilityRepresentative:
    """Source: R49, R50"""
    name: _t.Optional[str] = None
    facility: _t.Optional[str] = None
    recyclingCenter: _t.Optional["RecyclingCenter"] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC19 "Update Information" (R49)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R44, R45"""
    name: _t.Optional[str] = None
    website: _t.Optional[str] = None

    def replyToUserQuestions(self) -> None:
        """Realizes UC17 "Reply User Question" (R45)."""
        raise NotImplementedError
