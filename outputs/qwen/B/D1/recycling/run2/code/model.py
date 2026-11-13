"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R8, R19, R29, R36, R37, R38, R39"""
    name: _t.Optional[str] = None
    emailId: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    activity: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None
    userStats: _t.Optional["UserStats"] = None

    def giveEmailId(self) -> None:
        """Realizes UC6 "Give Email Id" (R8)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC7 "Create Account" (R15)."""
        raise NotImplementedError

    def browseList(self) -> None:
        """Realizes UC14 "Browse List" (R48)."""
        raise NotImplementedError

    def viewLocation(self) -> None:
        """Realizes UC15 "View Location" (R9, R10)."""
        raise NotImplementedError

    def viewMapDisplay(self) -> None:
        """Realizes UC16 "View Map Display" (R9, R10)."""
        raise NotImplementedError

    def viewDisposalEvent(self) -> None:
        """Realizes UC17 "View Disposal Event" (R11)."""
        raise NotImplementedError

    def viewUserDocumentation(self) -> None:
        """Realizes UC18 "View User Documentation" (R13)."""
        raise NotImplementedError

    def contactAdministrator(self) -> None:
        """Realizes UC25 "Contact Administrator" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class Profile:
    """Source: R7, R36"""
    favorites: _t.Optional[str] = None
    activityHistory: _t.Optional[str] = None


@_dc.dataclass
class Facility:
    """Source: R3, R4, R5, R6, R9, R10, R11, R36"""
    type: _t.Optional[str] = None
    openingHours: _t.Optional[str] = None
    location: _t.Optional[str] = None
    recyclingCenterInformation: _t.Optional[str] = None


@_dc.dataclass
class RecyclingCenterInformation:
    """Source: R16, R40, R42, R43, R44, R46, R47, R49, R50, R51"""
    materialAccepted: _t.Optional[str] = None
    stats: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    contactInfo: _t.Optional[str] = None

    def addRecyclingCenterInformation(self) -> None:
        """Realizes UC12 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def onboardRecyclingCenter(self) -> None:
        """Realizes UC31 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC28 "Reply User Question" (R45)."""
        raise NotImplementedError

    def communicateWithFacility(self) -> None:
        """Realizes UC23 "Communicate Facility" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R16, R40, R42, R43, R44, R46, R47, R49, R50, R51"""
    materialAccepted: _t.Optional[str] = None
    stats: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    contactInfo: _t.Optional[str] = None
    recyclingCenterInformation: _t.Optional["RecyclingCenterInformation"] = None
    material: _t.Optional["Material"] = None

    def addRecyclingCenterInformation(self) -> None:
        """Realizes UC12 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def onboardRecyclingCenter(self) -> None:
        """Realizes UC31 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC28 "Reply User Question" (R45)."""
        raise NotImplementedError

    def communicateWithFacility(self) -> None:
        """Realizes UC23 "Communicate Facility" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingfacilityRepresentative:
    """Source: R49, R50, R51"""
    materialAccepted: _t.Optional[str] = None
    stats: _t.Optional[str] = None
    schedule: _t.Optional[str] = None

    def updateInformation(self) -> None:
        """Realizes UC29 "Update Information" (R49)."""
        raise NotImplementedError

    def communicateWithSiteAdmin(self) -> None:
        """Realizes UC24 "Communicate Site" (R51)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R21, R22, R23, R32, R41, R46, R47"""
    dashboard: _t.Optional[str] = None
    userErrorLog: _t.Optional["UserErrorLog"] = None

    def blockUser(self) -> None:
        """Realizes UC26 "Block User" (R21)."""
        raise NotImplementedError

    def viewUserErrorLog(self) -> None:
        """Realizes UC22 "View User Error Log" (R41)."""
        raise NotImplementedError

    def communicateWithFacility(self) -> None:
        """Realizes UC23 "Communicate Facility" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class Dashboard:
    """Source: R22, R46"""
    usageStats: _t.Optional[str] = None
    locations: _t.Optional[str] = None


@_dc.dataclass
class CompanyAccountant:
    """Source: R33"""
    activityFees: _t.Optional[str] = None


@_dc.dataclass
class ActivityFee:
    """Source: R33"""
    amount: _t.Optional[float] = None
    description: _t.Optional[str] = None


@_dc.dataclass
class Developer:
    """Source: R27, R34, R35"""
    apiAccess: _t.Optional[bool] = None
    uiDesign: _t.Optional[bool] = None
    uxLessons: _t.Optional[bool] = None


@_dc.dataclass
class Executive:
    """Source: R24"""
    companyPerformance: _t.Optional[str] = None


@_dc.dataclass
class Company:
    """Source: R31"""
    website: _t.Optional[str] = None
    companyAccountant: _t.Optional["CompanyAccountant"] = None


@_dc.dataclass
class Location:
    """Source: R9, R10, R11, R36"""
    coordinates: _t.Optional[str] = None


@_dc.dataclass
class Material:
    """Source: R6, R49, R50"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R50"""
    pass


@_dc.dataclass
class UserStats:
    """Source: R44"""
    pass


@_dc.dataclass
class UserErrorLog:
    """Source: R41"""
    pass
