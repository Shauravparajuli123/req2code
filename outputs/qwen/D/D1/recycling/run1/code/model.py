"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R13, R14, R15, R19, R28, R29, R36, R37, R38, R39"""
    email: _t.Optional[str] = None
    password: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    transactionHistory: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def viewPublicInformation(self) -> None:
        """Realizes UC1 "View Public Information" (R2)."""
        raise NotImplementedError

    def enterZipCode(self) -> None:
        """Realizes UC2 "Enter Zip Code And Get List Of Nearby Recycling Facilities" (R3)."""
        raise NotImplementedError

    def getFacilityHours(self) -> None:
        """Realizes UC3 "Get Hours Of Each Recycling Facility" (R4)."""
        raise NotImplementedError

    def selectRecyclableWaste(self) -> None:
        """Realizes UC4 "Select Different Types Of Recyclable Waste" (R6)."""
        raise NotImplementedError

    def addFavoriteFacility(self) -> None:
        """Realizes UC5 "Add Donation Centers As Favorites" (R7)."""
        raise NotImplementedError

    def giveEmailID(self) -> None:
        """Realizes UC6 "Give Email ID" (R8)."""
        raise NotImplementedError

    def viewMapDisplayPublicBins(self) -> None:
        """Realizes UC7 "View Map Display Of Public Recycling Bins" (R9)."""
        raise NotImplementedError

    def viewMapDisplaySpecialWasteSites(self) -> None:
        """Realizes UC8 "View Map Display Of Special Waste Drop Off Sites" (R10)."""
        raise NotImplementedError

    def viewSafeDisposalEvents(self) -> None:
        """Realizes UC9 "View Safe Disposal Events" (R11)."""
        raise NotImplementedError

    def viewUserDocumentation(self) -> None:
        """Realizes UC10 "View User Documentation" (R13)."""
        raise NotImplementedError

    def viewInvalidZipCodeFeedback(self) -> None:
        """Realizes UC11 "Enter Invalid Zip Code" (R14)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC12 "Create An Account" (R15)."""
        raise NotImplementedError

    def viewLocationsOfRecyclingCenters(self) -> None:
        """Realizes UC30 "View Locations Of Recycling Centers On Map" (R36)."""
        raise NotImplementedError

    def uploadWeeksSchedule(self) -> None:
        """Realizes UC31 "Upload Week S Schedule" (R37)."""
        raise NotImplementedError

    def linkEmailAccount(self) -> None:
        """Realizes UC32 "Link Email Account To Profile" (R38)."""
        raise NotImplementedError

    def contactAdministrators(self) -> None:
        """Realizes UC33 "Contact Administrators" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R30, R46, R47"""
    users: _t.List["User"] = _dc.field(default_factory=list)
    recyclingFacility: _t.Optional["RecyclingFacility"] = None
    recyclingFacilityRepresentative: _t.Optional["RecyclingFacilityRepresentative"] = None

    def addRemoveFacilityInfo(self) -> None:
        """Realizes UC13 "Add Or Remove Recycling Facilities Information" (R16)."""
        raise NotImplementedError

    def readUserFeedback(self) -> None:
        """Realizes UC14 "Read Users Feedback And Complaints" (R17)."""
        raise NotImplementedError

    def blockUsersBasedOnIP(self) -> None:
        """Realizes UC15 "Block Specific Users Based On IP Address" (R21)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC16 "View A Dashboard That Monitors Sites Statuses" (R22)."""
        raise NotImplementedError

    def encryptData(self) -> None:
        """Realizes UC17 "Encrypt All Data" (R23)."""
        raise NotImplementedError

    def handleUserActivities(self) -> None:
        """Realizes UC24 "Handle Users Activities" (R30)."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R40, R41, R42, R43, R44, R45"""
    recyclingFacility: _t.Optional["RecyclingFacility"] = None
    admin: _t.Optional["Admin"] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC37 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC38 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC39 "Reply To User Questions" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R25, R32"""
    company: _t.Optional["Company"] = None

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC19 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def accessEmployeeInfo(self) -> None:
        """Realizes UC20 "Access Full Information Of All Employees" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class Developer:
    """Source: R27, R28, R34, R35"""
    company: _t.Optional["Company"] = None

    def accessAPI(self) -> None:
        """Realizes UC21 "Access API From Website" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC28 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendLessons(self) -> None:
        """Realizes UC29 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R31, R33"""
    companyAccountant: _t.Optional["CompanyAccountant"] = None

    def accessWebsite(self) -> None:
        """Realizes UC20 "Access Full Information Of All Employees" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class CompanyAccountant:
    """Source: R33"""

    def viewActivityFees(self) -> None:
        """Realizes UC27 "View All Available Activity Fees" (R33)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R48, R49, R50, R51"""
    facilityInfo: _t.Optional[str] = None
    recyclingFacilityRepresentative: _t.Optional["RecyclingFacilityRepresentative"] = None
    admin: _t.Optional["Admin"] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC42 "Update Information And Type Of Material Accepted" (R49)."""
        raise NotImplementedError

    def viewUserStatsAndSchedules(self) -> None:
        """Realizes UC43 "Access User Stats And Schedules" (R50)."""
        raise NotImplementedError

    def communicateWithSiteAdmin(self) -> None:
        """Realizes UC41 "Communicate Directly With Site Admin" (R50)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacilityRepresentative:
    """Source: R49, R50, R51"""

    def updateFacilityInfo(self) -> None:
        """Realizes UC42 "Update Information And Type Of Material Accepted" (R49)."""
        raise NotImplementedError

    def viewUserStatsAndSchedules(self) -> None:
        """Realizes UC43 "Access User Stats And Schedules" (R50)."""
        raise NotImplementedError

    def communicateWithSiteAdmin(self) -> None:
        """Realizes UC41 "Communicate Directly With Site Admin" (R50)."""
        raise NotImplementedError
