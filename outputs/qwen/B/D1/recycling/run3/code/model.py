"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R18, R19, R20, R28, R29"""
    profile: _t.Optional[str] = None
    email: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None
    favoriteRecyclingCenters: _t.Optional[str] = None
    transactionHistory: _t.Optional[str] = None
    uiExperience: _t.Optional[str] = None
    deviceAccess: _t.Optional[bool] = None
    reward: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None

    def enterZipCode(self) -> None:
        """Realizes UC2 "Enter Zip Code" (R3)."""
        raise NotImplementedError

    def getRecyclingFacilityHours(self) -> None:
        """Realizes UC3 "Get Hours" (R4)."""
        raise NotImplementedError

    def choosePick(self) -> None:
        """Realizes UC5 "Choose Pick" (R5)."""
        raise NotImplementedError

    def viewUserDocumentation(self) -> None:
        """Realizes UC17 "View User Documentation" (R13)."""
        raise NotImplementedError

    def viewMapDisplay(self) -> None:
        """Realizes UC19 "View Map Display" (R9, R10)."""
        raise NotImplementedError

    def viewDisposalEvent(self) -> None:
        """Realizes UC20 "View Disposal Event" (R11)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC21 "View Information" (R2)."""
        raise NotImplementedError

    def viewActivityFee(self) -> None:
        """Realizes UC22 "View Activity Fee" (R33)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC23 "View Dashboard" (R22)."""
        raise NotImplementedError

    def viewStat(self) -> None:
        """Realizes UC24 "View Stat" (R44)."""
        raise NotImplementedError

    def browseList(self) -> None:
        """Realizes UC12 "Browse List" (R48)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC13 "Upload Schedule" (R37)."""
        raise NotImplementedError

    def linkEmailAccount(self) -> None:
        """Realizes UC14 "Link Email Account" (R38)."""
        raise NotImplementedError

    def contactAdministrator(self) -> None:
        """Realizes UC15 "Contact Administrator" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R25, R26, R40, R41, R42, R43, R44, R47, R48, R49, R50, R51"""
    dataAccess: _t.Optional[bool] = None
    dashboard: _t.Optional[str] = None
    userActivity: _t.Optional[str] = None
    facilityInformation: _t.Optional[str] = None
    userStats: _t.Optional[str] = None

    def addRecyclingCenterInformation(self) -> None:
        """Realizes UC10 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def readFeedback(self) -> None:
        """Realizes UC28 "Read Feedback" (R17)."""
        raise NotImplementedError

    def blockUser(self) -> None:
        """Realizes UC27 "Block User" (R21)."""
        raise NotImplementedError

    def viewUserErrorLog(self) -> None:
        """Realizes UC41 "View User Error Log" (R41)."""
        raise NotImplementedError

    def onboardRecyclingCenter(self) -> None:
        """Realizes UC11 "Onboard Recycling Center" (R42)."""
        raise NotImplementedError

    def handleActivity(self) -> None:
        """Realizes UC16 "Handle Activity" (R30)."""
        raise NotImplementedError

    def communicateFacility(self) -> None:
        """Realizes UC25 "Communicate Facility" (R47)."""
        raise NotImplementedError

    def communicateSite(self) -> None:
        """Realizes UC26 "Communicate Site" (R51)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC24 "View Stat" (R44)."""
        raise NotImplementedError

    def viewFacilityInformation(self) -> None:
        """Realizes UC21 "View Information" (R2)."""
        raise NotImplementedError

    def viewUserActivity(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingCenter:
    """Source: R9, R10, R11, R48"""
    name: _t.Optional[str] = None
    openingHours: _t.Optional[str] = None
    location: _t.Optional[str] = None
    specialWasteDropOff: _t.Optional[bool] = None
    safeDisposalEvents: _t.Optional[str] = None

    def getHours(self) -> None:
        """Realizes UC3 "Get Hours" (R4)."""
        raise NotImplementedError

    def viewMapDisplay(self) -> None:
        """Realizes UC19 "View Map Display" (R9, R10)."""
        raise NotImplementedError

    def viewDisposalEvent(self) -> None:
        """Realizes UC20 "View Disposal Event" (R11)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R49, R50, R51"""
    name: _t.Optional[str] = None
    acceptedMaterials: _t.Optional[str] = None
    userStats: _t.Optional[str] = None
    schedule: _t.Optional[str] = None

    def updateInformation(self) -> None:
        """Realizes UC29 "Update Information" (R49)."""
        raise NotImplementedError

    def communicateAdmin(self) -> None:
        """Realizes UC26 "Communicate Site" (R51)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC24 "View Stat" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingfacilityRepresentative:
    """Source: R49, R50"""
    name: _t.Optional[str] = None
    acceptedMaterials: _t.Optional[str] = None
    userStats: _t.Optional[str] = None

    def updateInformation(self) -> None:
        """Realizes UC29 "Update Information" (R49)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC24 "View Stat" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Profile:
    """Source: R7"""
    favoriteRecyclingCenters: _t.Optional[str] = None


@_dc.dataclass
class Transaction:
    """Source: R18"""
    pass


@_dc.dataclass
class Hour:
    """Source: R9, R10, R11, R48"""
    pass


@_dc.dataclass
class DisposalEvent:
    """Source: R11"""
    pass


@_dc.dataclass
class Location:
    """Source: R9, R10, R11, R48"""
    pass


@_dc.dataclass
class Material:
    """Source: R49, R50, R51"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R51"""
    pass


@_dc.dataclass
class UserActivity:
    """Source: R41"""
    pass


@_dc.dataclass
class UserStat:
    """Source: R44"""
    pass


@_dc.dataclass
class Dashboard:
    """Source: R22, R47"""
    pass
