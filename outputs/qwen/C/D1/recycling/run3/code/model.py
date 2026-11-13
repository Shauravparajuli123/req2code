"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R15, R17, R19, R28, R39, R48, R50"""
    name: _t.Optional[str] = None
    emailId: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    activity: _t.Optional[str] = None
    stat: _t.Optional[str] = None
    recyclingCenter: _t.Optional["RecyclingCenter"] = None
    notification: _t.Optional["Notification"] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R15)."""
        raise NotImplementedError

    def giveEmailId(self) -> None:
        """Realizes UC6 "Give Email Id" (R8)."""
        raise NotImplementedError

    def viewDocumentation(self) -> None:
        """Realizes UC34 "View User Documentation" (R13)."""
        raise NotImplementedError

    def viewFeedback(self) -> None:
        """Realizes UC3 "Get Feedback" (R14)."""
        raise NotImplementedError

    def viewPick(self) -> None:
        """Realizes UC42 "Have Pick" (R5)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC30 "View Information" (R2)."""
        raise NotImplementedError

    def viewLocation(self) -> None:
        """Realizes UC31 "View Location" (R9, R10)."""
        raise NotImplementedError

    def viewMapDisplay(self) -> None:
        """Realizes UC32 "View Map Display" (R9, R10)."""
        raise NotImplementedError

    def viewDisposalEvent(self) -> None:
        """Realizes UC29 "View Disposal Event" (R11)."""
        raise NotImplementedError

    def contactAdministrator(self) -> None:
        """Realizes UC14 "Contact Administrator" (R39)."""
        raise NotImplementedError

    def browseList(self) -> None:
        """Realizes UC8 "Browse List" (R48)."""
        raise NotImplementedError

    def checkTransactionHistory(self) -> None:
        """Realizes UC9 "Check Transaction History" (R18)."""
        raise NotImplementedError

    def receiveReward(self) -> None:
        """Realizes UC44 "Receive Reward" (R28)."""
        raise NotImplementedError

    def viewUserErrorLog(self) -> None:
        """Realizes UC35 "View User Error Log" (R41)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R40, R41, R42, R46, R47"""
    data: _t.Optional[str] = None
    dashboard: _t.Optional[str] = None
    recyclingCenterInformation: _t.Optional["RecyclingCenterInformation"] = None
    users: _t.List["User"] = _dc.field(default_factory=list)

    def addRecyclingCenterInformation(self) -> None:
        """Realizes UC16 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def readFeedback(self) -> None:
        """Realizes UC19 "Read Feedback" (R17)."""
        raise NotImplementedError

    def blockUser(self) -> None:
        """Realizes UC36 "Block User" (R21)."""
        raise NotImplementedError

    def onboardRecyclingCenter(self) -> None:
        """Realizes UC18 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def viewUserErrorLogs(self) -> None:
        """Realizes UC35 "View User Error Log" (R41)."""
        raise NotImplementedError

    def communicateFacility(self) -> None:
        """Realizes UC12 "Communicate Facility" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R16, R49, R51"""
    name: _t.Optional[str] = None
    material: _t.Optional[str] = None

    def updateInformation(self) -> None:
        """Realizes UC23 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def communicateSite(self) -> None:
        """Realizes UC13 "Communicate Site" (R51)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingCenterInformation:
    """Source: R16, R40, R43"""
    name: _t.Optional[str] = None
    material: _t.Optional[str] = None

    def addInformation(self) -> None:
        """Realizes UC16 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingCenter:
    """Source: R16, R49, R50"""
    name: _t.Optional[str] = None
    material: _t.Optional[str] = None

    def updateInformation(self) -> None:
        """Realizes UC23 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError


@_dc.dataclass
class Profile:
    """Source: R7, R19"""
    favorites: _t.Optional[str] = None


@_dc.dataclass
class Dashboard:
    """Source: R22, R46"""
    usageStats: _t.Optional[str] = None
    locations: _t.Optional[str] = None


@_dc.dataclass
class Material:
    """Source: R49, R50"""
    type: _t.Optional[str] = None


@_dc.dataclass
class Location:
    """Source: R46"""
    name: _t.Optional[str] = None
    material: _t.Optional[str] = None


@_dc.dataclass
class Schedule:
    """Source: R37"""
    weekSchedule: _t.Optional[str] = None


@_dc.dataclass
class Feedback:
    """Source: R14, R17"""
    message: _t.Optional[str] = None


@_dc.dataclass
class Notification:
    """Source: R8, R32"""
    message: _t.Optional[str] = None


@_dc.dataclass
class CompanyAccountant:
    """Source: R33"""
    activityFees: _t.Optional[str] = None


@_dc.dataclass
class Developer:
    """Source: R27, R34, R35"""
    apiAccess: _t.Optional[bool] = None


@_dc.dataclass
class Executive:
    """Source: R24"""
    companyPerformance: _t.Optional[str] = None


@_dc.dataclass
class Employee:
    """Source: R25, R26"""
    employeeInfo: _t.Optional[str] = None
    work: _t.Optional["Work"] = None


@_dc.dataclass
class Facility:
    """Source: R16, R49, R51"""
    name: _t.Optional[str] = None
    material: _t.Optional[str] = None


@_dc.dataclass
class Work:
    """Source: R25"""
    routePlanning: _t.Optional[str] = None


@_dc.dataclass
class ZipCode:
    """Source: R14, R13, R17"""
    code: _t.Optional[str] = None
