"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R18, R28, R29"""
    email: _t.Optional[str] = None
    password: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    account: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def clickOnAddress(self) -> None:
        """Realizes UC1 "Click On The Address" (R1)."""
        raise NotImplementedError

    def viewPublicInformation(self) -> None:
        """Realizes UC2 "View Public Information" (R2)."""
        raise NotImplementedError

    def enterZipCode(self) -> None:
        """Realizes UC3 "Enter Zip Code And Get List Of Nearby Recycling Facilities" (R3)."""
        raise NotImplementedError

    def getFacilityHours(self) -> None:
        """Realizes UC4 "Get Hours Of Each Recycling Facility" (R4)."""
        raise NotImplementedError

    def selectRecyclableWaste(self) -> None:
        """Realizes UC5 "Select Different Types Of Recyclable Waste" (R6)."""
        raise NotImplementedError

    def addFavoriteDonationCenter(self) -> None:
        """Realizes UC6 "Add Donation Centers As Favorites" (R7)."""
        raise NotImplementedError

    def giveEmailID(self) -> None:
        """Realizes UC7 "Give Email ID" (R8)."""
        raise NotImplementedError

    def viewMapDisplayPublicBins(self) -> None:
        """Realizes UC8 "View Map Display Of Public Recycling Bins" (R9)."""
        raise NotImplementedError

    def viewMapDisplaySpecialWasteSites(self) -> None:
        """Realizes UC9 "View Map Display Of Special Waste Drop Off Sites" (R10)."""
        raise NotImplementedError

    def viewSafeDisposalEvents(self) -> None:
        """Realizes UC10 "View Safe Disposal Events" (R11)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC13 "Create An Account" (R15)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R30, R46, R47"""
    users: _t.List["User"] = _dc.field(default_factory=list)

    def addRemoveRecyclingFacilities(self) -> None:
        """Realizes UC14 "Add Or Remove Recycling Facilities Information" (R16)."""
        raise NotImplementedError

    def readUserFeedback(self) -> None:
        """Realizes UC15 "Read Users Feedback And Complaints" (R17)."""
        raise NotImplementedError

    def blockUsersBasedOnIP(self) -> None:
        """Realizes UC16 "Block Specific Users Based On IP Address" (R21)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC17 "View A Dashboard That Monitors Sites Statuses" (R22)."""
        raise NotImplementedError

    def encryptData(self) -> None:
        """Realizes UC18 "Encrypt All Data" (R23)."""
        raise NotImplementedError

    def handleUserActivities(self) -> None:
        """Realizes UC25 "Handle Users Activities" (R30)."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R40, R44, R45"""
    admins: _t.List["Admin"] = _dc.field(default_factory=list)

    def updateRecyclingCenterInfo(self) -> None:
        """Realizes UC38 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC39 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC40 "Reply To User Questions" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R25, R32"""
    company: _t.Optional["Company"] = None

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC20 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def getQuickNotifications(self) -> None:
        """Realizes UC27 "Get Quick Notifications" (R32)."""
        raise NotImplementedError


@_dc.dataclass
class Developer:
    """Source: R27, R28, R34, R35"""
    company: _t.Optional["Company"] = None

    def accessAPI(self) -> None:
        """Realizes UC22 "Access API From Website" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC29 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendUIUXLessons(self) -> None:
        """Realizes UC30 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R31"""

    def accessWebsite(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CompanyAccountant:
    """Source: R33"""
    company: _t.Optional["Company"] = None

    def viewActivityFees(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacilityRepresentative:
    """Source: R49, R50"""
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC43 "Update Information And Type Of Material Accepted" (R49)."""
        raise NotImplementedError

    def viewUserStatsAndSchedules(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R48, R51"""
    information: _t.Optional[str] = None

    def communicateWithSiteAdmin(self) -> None:
        """Realizes UC45 "Communicate Directly With Site Admin" (R51)."""
        raise NotImplementedError
