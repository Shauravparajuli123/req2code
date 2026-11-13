"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R19, R20, R36, R37, R38, R39"""
    email: _t.Optional[str] = None
    password: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    transactionHistory: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def viewPublicInformation(self) -> None:
        """Realizes UC2 "View Public Information" (R2)."""
        raise NotImplementedError

    def enterZipCode(self) -> None:
        """Realizes UC3 "Enter Zip Code And Get List Of Nearby Recycling Facilities" (R3)."""
        raise NotImplementedError

    def getFacilityHours(self) -> None:
        """Realizes UC4 "Get Hours Of Each Recycling Facility" (R4)."""
        raise NotImplementedError

    def selectWasteTypes(self) -> None:
        """Realizes UC5 "Select Different Types Of Recyclable Waste" (R6)."""
        raise NotImplementedError

    def addFavoriteFacility(self) -> None:
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

    def choosePickUpTime(self) -> None:
        """Realizes UC11 "Choose Flexible Pick Up Time" (R5, R12)."""
        raise NotImplementedError

    def viewUserDocumentation(self) -> None:
        """Realizes UC12 "View User Documentation" (R13)."""
        raise NotImplementedError

    def viewInvalidZipCodeFeedback(self) -> None:
        """Realizes UC13 "Enter Invalid Zip Code" (R14)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC14 "Create An Account" (R15)."""
        raise NotImplementedError

    def viewAllLocationsOfRecyclingCenters(self) -> None:
        """Realizes UC25 "View All Locations Of Recycling Centers On A Map" (R36)."""
        raise NotImplementedError

    def uploadWeeksSchedule(self) -> None:
        """Realizes UC26 "Upload Week S Schedule" (R37)."""
        raise NotImplementedError

    def linkEmailAccountToProfile(self) -> None:
        """Realizes UC27 "Link Email Account To Profile" (R38)."""
        raise NotImplementedError

    def contactAdministrators(self) -> None:
        """Realizes UC28 "Contact Administrators" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R31, R34, R41, R46, R47"""
    errorLogs: _t.Optional[str] = None
    dashboard: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def addRemoveFacilityInfo(self) -> None:
        """Realizes UC15 "Add Or Remove Recycling Facilities Information" (R16)."""
        raise NotImplementedError

    def readFeedbackComplaints(self) -> None:
        """Realizes UC16 "Read Users Feedback And Complaints" (R17)."""
        raise NotImplementedError

    def blockUsersBasedOnIP(self) -> None:
        """Realizes UC17 "Block Specific Users Based On IP Address" (R21)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC18 "View A Dashboard That Monitors All The Sites Statuses" (R22)."""
        raise NotImplementedError

    def viewEncryptedData(self) -> None:
        """Realizes UC19 "View All Data Encrypted" (R23)."""
        raise NotImplementedError

    def addRecyclingCenterInfo(self) -> None:
        """Realizes UC29 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def viewUserErrorLogs(self) -> None:
        """Realizes UC30 "View User Error Logs" (R41)."""
        raise NotImplementedError

    def onboardRecyclingCenters(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def communicateWithFacilities(self) -> None:
        """Realizes UC35 "Communicate Directly With Facilities" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R30, R42, R43, R44, R45"""
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def handleUserActivities(self) -> None:
        """Operation."""
        raise NotImplementedError

    def onboardRecyclingCenters(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def updateRecyclingCenterInfo(self) -> None:
        """Realizes UC32 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUsersStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R25, R26"""

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC21 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def accessEmployeeInfo(self) -> None:
        """Realizes UC22 "Access Full Information Of All Employees" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class Developer:
    """Source: R19, R27, R28, R34, R35"""

    def accessWebsiteAPI(self) -> None:
        """Realizes UC21 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC23 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendUIUXLessons(self) -> None:
        """Realizes UC24 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class CompanyAccountant:
    """Source: R33"""

    def viewActivityFees(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacilityRepresentative:
    """Source: R40, R48, R49, R50"""
    facilityInformation: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC37 "Update Information And Type Of Material Accepted" (R49)."""
        raise NotImplementedError

    def viewUserStatsAndSchedules(self) -> None:
        """Operation."""
        raise NotImplementedError

    def communicateWithSiteAdmin(self) -> None:
        """Realizes UC39 "Communicate Directly With Site Admin" (R51)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R51"""

    def communicateWithSiteAdmin(self) -> None:
        """Realizes UC39 "Communicate Directly With Site Admin" (R51)."""
        raise NotImplementedError
