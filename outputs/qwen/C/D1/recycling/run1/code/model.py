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
    recyclingfacility: _t.Optional["Recyclingfacility"] = None
    location: _t.Optional["Location"] = None

    def createAccount(self) -> None:
        """Operation."""
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
    favoriteFacilities: _t.Optional[str] = None


@_dc.dataclass
class Facility:
    """Source: R2, R3, R4, R6, R10, R11, R36, R48"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None
    openingHours: _t.Optional[str] = None
    location: _t.Optional[str] = None
    specialWasteDropOff: _t.Optional[bool] = None
    safeDisposalEvents: _t.Optional[str] = None


@_dc.dataclass
class Location:
    """Source: R9, R10, R36"""
    coordinates: _t.Optional[str] = None


@_dc.dataclass
class Event:
    """Source: R11"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None


@_dc.dataclass
class Admin:
    """Source: R16, R17, R22, R25, R42, R46"""
    dashboard: _t.Optional[str] = None
    blockedUsers: _t.Optional[str] = None
    recyclingCenters: _t.List["RecyclingCenter"] = _dc.field(default_factory=list)
    users: _t.List["User"] = _dc.field(default_factory=list)

    def addFacilityInfo(self) -> None:
        """Realizes UC14 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def removeFacilityInfo(self) -> None:
        """Realizes UC14 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def readFeedback(self) -> None:
        """Realizes UC15 "Read Feedback" (R17)."""
        raise NotImplementedError

    def handleActivity(self) -> None:
        """Realizes UC7 "Handle Activity" (R30)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC24 "View Dashboard" (R46)."""
        raise NotImplementedError

    def communicateWithFacility(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Dashboard:
    """Source: R22, R46"""
    facilities: _t.Optional[str] = None
    userStats: _t.Optional[str] = None


@_dc.dataclass
class Executive:
    """Source: R24"""
    companyPerformance: _t.Optional[str] = None


@_dc.dataclass
class CompanyAccountant:
    """Source: R33"""
    activityFees: _t.Optional[str] = None
    activityFee: _t.Optional["ActivityFee"] = None


@_dc.dataclass
class ActivityFee:
    """Source: R33"""
    name: _t.Optional[str] = None
    amount: _t.Optional[float] = None


@_dc.dataclass
class RecyclingCenter:
    """Source: R16, R40, R42, R43, R44, R46"""
    name: _t.Optional[str] = None
    facilities: _t.Optional[str] = None
    materialAccepted: _t.Optional[str] = None

    def addFacilityInfo(self) -> None:
        """Realizes UC14 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def updateInfo(self) -> None:
        """Realizes UC20 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Material:
    """Source: R6, R43, R44, R46"""
    name: _t.Optional[str] = None


@_dc.dataclass
class RecyclingfacilityRepresentative:
    """Source: R49, R50"""
    facility: _t.Optional[str] = None
    stats: _t.Optional[str] = None

    def updateInfo(self) -> None:
        """Realizes UC19 "Update Information" (R49)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R45, R44"""
    recyclingCenters: _t.List["RecyclingCenter"] = _dc.field(default_factory=list)

    def replyToUserQuestions(self) -> None:
        """Realizes UC17 "Reply User Question" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Recyclingfacility:
    """Source: R51"""
    name: _t.Optional[str] = None
    facilities: _t.Optional[str] = None
    recyclingfacilityRepresentative: _t.Optional["RecyclingfacilityRepresentative"] = None

    def communicateWithAdmin(self) -> None:
        """Operation."""
        raise NotImplementedError
