"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R18, R19, R20, R28, R29, R38, R39"""
    name: _t.Optional[str] = None
    emailId: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    activity: _t.Optional[str] = None
    stat: _t.Optional[str] = None
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)
    recyclingFacilities: _t.List["RecyclingFacility"] = _dc.field(default_factory=list)
    picks: _t.List["Pick"] = _dc.field(default_factory=list)
    materials: _t.List["Material"] = _dc.field(default_factory=list)
    schedules: _t.List["Schedule"] = _dc.field(default_factory=list)

    def clickAddress(self) -> None:
        """Realizes UC1 "Click Address" (R1)."""
        raise NotImplementedError

    def enterZipCode(self) -> None:
        """Realizes UC2 "Enter Zip Code" (R3)."""
        raise NotImplementedError

    def getFeedback(self) -> None:
        """Realizes UC3 "Get Feedback" (R14)."""
        raise NotImplementedError

    def getHour(self) -> None:
        """Realizes UC4 "Get Hour" (R4)."""
        raise NotImplementedError

    def addFavorite(self) -> None:
        """Realizes UC10 "Add Donation Center" (R7)."""
        raise NotImplementedError

    def giveEmailId(self) -> None:
        """Realizes UC6 "Give Email Id" (R8)."""
        raise NotImplementedError

    def viewMapDisplay(self) -> None:
        """Realizes UC22 "View Map Display" (R9, R10)."""
        raise NotImplementedError

    def viewLocation(self) -> None:
        """Realizes UC21 "View Location" (R9, R10)."""
        raise NotImplementedError

    def viewDisposalEvent(self) -> None:
        """Realizes UC19 "View Disposal Event" (R11)."""
        raise NotImplementedError

    def browseList(self) -> None:
        """Realizes UC8 "Browse List" (R48)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC16 "Create Account" (R15)."""
        raise NotImplementedError

    def viewUserDocumentation(self) -> None:
        """Realizes UC24 "View User Documentation" (R13)."""
        raise NotImplementedError

    def viewUserErrorLog(self) -> None:
        """Realizes UC25 "View User Error Log" (R41)."""
        raise NotImplementedError

    def linkEmailAccount(self) -> None:
        """Realizes UC29 "Link Email Account" (R38)."""
        raise NotImplementedError

    def contactAdministrator(self) -> None:
        """Realizes UC15 "Contact Administrator" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R3, R4, R6, R10, R11, R16, R17, R20, R22, R23, R24, R26, R30, R32, R33, R34, R35, R36, R37, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R50, R51"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None
    openingHour: _t.Optional[str] = None
    location: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    material: _t.Optional[str] = None
    hour: _t.Optional["Hour"] = None
    materials: _t.List["Material"] = _dc.field(default_factory=list)
    profile: _t.Optional["Profile"] = None
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)

    def addInformation(self) -> None:
        """Realizes UC11 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def onboardFacility(self) -> None:
        """Realizes UC30 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def communicateSite(self) -> None:
        """Realizes UC14 "Communicate Site" (R51)."""
        raise NotImplementedError

    def communicateFacility(self) -> None:
        """Realizes UC13 "Communicate Facility" (R47)."""
        raise NotImplementedError

    def handleActivity(self) -> None:
        """Realizes UC7 "Handle Activity" (R30)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC18 "View Dashboard" (R22, R46)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Operation."""
        raise NotImplementedError

    def replyUserQuestion(self) -> None:
        """Realizes UC32 "Reply User Question" (R45)."""
        raise NotImplementedError

    def updateInformation(self) -> None:
        """Realizes UC34 "Update Information" (R49)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R24, R26, R30, R32, R34, R41, R46, R47"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None
    recyclingFacilities: _t.List["RecyclingFacility"] = _dc.field(default_factory=list)
    users: _t.List["User"] = _dc.field(default_factory=list)

    def addRecyclingCenterInformation(self) -> None:
        """Realizes UC11 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def readFeedback(self) -> None:
        """Realizes UC31 "Read Feedback" (R17)."""
        raise NotImplementedError

    def handleActivity(self) -> None:
        """Realizes UC7 "Handle Activity" (R30)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC18 "View Dashboard" (R22, R46)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Operation."""
        raise NotImplementedError

    def replyUserQuestion(self) -> None:
        """Realizes UC32 "Reply User Question" (R45)."""
        raise NotImplementedError

    def blockUser(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewUserErrorLog(self) -> None:
        """Realizes UC25 "View User Error Log" (R41)."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R41, R44, R45, R46, R47"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def updateRecyclingCenterInformation(self) -> None:
        """Realizes UC35 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Operation."""
        raise NotImplementedError

    def replyUserQuestion(self) -> None:
        """Realizes UC32 "Reply User Question" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingfacilityRepresentative:
    """Source: R49, R50, R51"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None
    schedule: _t.Optional["Schedule"] = None
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)
    profile: _t.Optional["Profile"] = None
    material: _t.Optional["Material"] = None
    users: _t.List["User"] = _dc.field(default_factory=list)

    def updateInformation(self) -> None:
        """Realizes UC34 "Update Information" (R49)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Profile:
    """Source: R7, R38"""
    favorites: _t.Optional[str] = None


class Pick(_enum.Enum):
    """Source: R16"""
    RECYCLINGCENTER = "RECYCLINGCENTER"
    DONATIONCENTER = "DONATIONCENTER"


@_dc.dataclass
class Material:
    """Source: R6, R16, R20, R22, R24, R30, R33, R36, R37, R40, R42, R43, R44, R45, R46, R47, R48"""
    type: _t.Optional[str] = None


@_dc.dataclass
class Schedule:
    """Source: R37, R39, R40, R42, R43, R44, R45, R46, R47, R48"""
    week: _t.Optional[str] = None


@_dc.dataclass
class Location:
    """Source: R9, R10, R11, R16, R20, R22, R24, R30, R33, R36, R37, R40, R42, R43, R44, R45, R46, R47, R48"""
    coordinates: _t.Optional[str] = None


@_dc.dataclass
class Feedback:
    """Source: R14, R17, R41"""
    message: _t.Optional[str] = None


@_dc.dataclass
class Hour:
    """Source: R4, R10, R11, R16, R20, R22, R24, R30, R33, R36, R37, R40, R42, R43, R44, R45, R46, R47, R48"""
    time: _t.Optional[str] = None


@_dc.dataclass
class Notification:
    """Source: R8, R21, R22, R23, R24, R26, R30, R32, R34, R41, R46, R47"""
    message: _t.Optional[str] = None


@_dc.dataclass
class CompanyAccountant:
    """Source: R24, R33"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def viewActivityFee(self) -> None:
        """Realizes UC17 "View Activity Fee" (R33)."""
        raise NotImplementedError


@_dc.dataclass
class Executive:
    """Source: R24"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def viewActivityFee(self) -> None:
        """Realizes UC17 "View Activity Fee" (R33)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R25, R26, R32"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC27 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def viewEmployeeInfo(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Developer:
    """Source: R27, R34, R35"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def accessApi(self) -> None:
        """Realizes UC26 "Access Api" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC37 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendUxLesson(self) -> None:
        """Realizes UC38 "Attend Ux Lesson" (R35)."""
        raise NotImplementedError
