"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R2, R14, R15, R17, R19, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51"""
    email: _t.Optional[str] = None
    favorites: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    password: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def viewPublicInformation(self) -> None:
        """Realizes UC1 "View Public Information" (R2)."""
        raise NotImplementedError

    def getNearbyFacilities(self) -> None:
        """Realizes UC2 "Enter Zip Code And Get Nearby Facilities" (R3)."""
        raise NotImplementedError

    def getFacilityHours(self) -> None:
        """Realizes UC3 "Get Hours Of Facilities" (R4)."""
        raise NotImplementedError

    def selectRecyclableWasteTypes(self) -> None:
        """Realizes UC5 "Select Recyclable Waste Types" (R6)."""
        raise NotImplementedError

    def addFavorite(self) -> None:
        """Realizes UC6 "Add Favorites" (R7)."""
        raise NotImplementedError

    def giveFeedback(self) -> None:
        """Realizes UC12 "View Feedback For Invalid Zip Code" (R14)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC13 "Create Account" (R15)."""
        raise NotImplementedError

    def blockUser(self) -> None:
        """Realizes UC16 "Block Specific Users" (R21)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC17 "View Dashboard" (R22)."""
        raise NotImplementedError

    def encryptData(self) -> None:
        """Realizes UC18 "Encrypt Data" (R23)."""
        raise NotImplementedError

    def accessData(self) -> None:
        """Realizes UC19 "Access Data Related To Company" (R24)."""
        raise NotImplementedError

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC20 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def accessEmployeeInformation(self) -> None:
        """Realizes UC21 "Access Full Employee Information" (R26)."""
        raise NotImplementedError

    def accessAPI(self) -> None:
        """Realizes UC22 "Access API" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC23 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendLessons(self) -> None:
        """Realizes UC24 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError

    def viewRecyclingCenterLocations(self) -> None:
        """Realizes UC25 "View Recycling Center Locations" (R36)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC26 "Upload Weekly Schedule" (R37)."""
        raise NotImplementedError

    def linkEmailAccount(self) -> None:
        """Realizes UC27 "Link Email Account" (R38)."""
        raise NotImplementedError

    def contactAdmins(self) -> None:
        """Realizes UC28 "Contact Administrators" (R39)."""
        raise NotImplementedError

    def addFacilityInfo(self) -> None:
        """Realizes UC29 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def viewErrorLogs(self) -> None:
        """Realizes UC30 "View User Error Logs" (R41)."""
        raise NotImplementedError

    def onboardFacility(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def updateFacilityInfo(self) -> None:
        """Realizes UC32 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError

    def communicateWithFacilities(self) -> None:
        """Realizes UC35 "Communicate With Facilities" (R47)."""
        raise NotImplementedError

    def viewFacilityStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51"""
    recyclingFacility: _t.Optional["RecyclingFacility"] = None
    users: _t.List["User"] = _dc.field(default_factory=list)

    def addRemoveFacilityInfo(self) -> None:
        """Realizes UC14 "Add Or Remove Recycling Facilities Information" (R16)."""
        raise NotImplementedError

    def readFeedbackComplaints(self) -> None:
        """Realizes UC15 "Read Users Feedback And Complaints" (R17)."""
        raise NotImplementedError

    def blockUser(self) -> None:
        """Realizes UC16 "Block Specific Users" (R21)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC17 "View Dashboard" (R22)."""
        raise NotImplementedError

    def encryptData(self) -> None:
        """Realizes UC18 "Encrypt Data" (R23)."""
        raise NotImplementedError

    def accessData(self) -> None:
        """Realizes UC19 "Access Data Related To Company" (R24)."""
        raise NotImplementedError

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC20 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def accessEmployeeInformation(self) -> None:
        """Realizes UC21 "Access Full Employee Information" (R26)."""
        raise NotImplementedError

    def accessAPI(self) -> None:
        """Realizes UC22 "Access API" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC23 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendLessons(self) -> None:
        """Realizes UC24 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError

    def viewRecyclingCenterLocations(self) -> None:
        """Realizes UC25 "View Recycling Center Locations" (R36)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC26 "Upload Weekly Schedule" (R37)."""
        raise NotImplementedError

    def linkEmailAccount(self) -> None:
        """Realizes UC27 "Link Email Account" (R38)."""
        raise NotImplementedError

    def contactAdmins(self) -> None:
        """Realizes UC28 "Contact Administrators" (R39)."""
        raise NotImplementedError

    def addFacilityInfo(self) -> None:
        """Realizes UC29 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def viewErrorLogs(self) -> None:
        """Realizes UC30 "View User Error Logs" (R41)."""
        raise NotImplementedError

    def onboardFacility(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def updateFacilityInfo(self) -> None:
        """Realizes UC32 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError

    def communicateWithFacilities(self) -> None:
        """Realizes UC35 "Communicate With Facilities" (R47)."""
        raise NotImplementedError

    def viewFacilityStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Executive:
    """Source: R24"""

    def accessData(self) -> None:
        """Realizes UC19 "Access Data Related To Company" (R24)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R25, R26"""
    admin: _t.Optional["Admin"] = None

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC20 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def accessEmployeeInformation(self) -> None:
        """Realizes UC21 "Access Full Employee Information" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class HREmployee:
    """Source: R26"""
    employee: _t.Optional["Employee"] = None

    def accessEmployeeInformation(self) -> None:
        """Realizes UC21 "Access Full Employee Information" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class Developer:
    """Source: R27, R28, R29, R34, R35"""
    admin: _t.Optional["Admin"] = None

    def accessAPI(self) -> None:
        """Realizes UC22 "Access API" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC23 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendLessons(self) -> None:
        """Realizes UC24 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R36, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51"""
    facilityName: _t.Optional[str] = None
    facilityType: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    email: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def viewRecyclingCenterLocations(self) -> None:
        """Realizes UC25 "View Recycling Center Locations" (R36)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC26 "Upload Weekly Schedule" (R37)."""
        raise NotImplementedError

    def linkEmailAccount(self) -> None:
        """Realizes UC27 "Link Email Account" (R38)."""
        raise NotImplementedError

    def contactAdmins(self) -> None:
        """Realizes UC28 "Contact Administrators" (R39)."""
        raise NotImplementedError

    def addFacilityInfo(self) -> None:
        """Realizes UC29 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def viewErrorLogs(self) -> None:
        """Realizes UC30 "View User Error Logs" (R41)."""
        raise NotImplementedError

    def onboardFacility(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def updateFacilityInfo(self) -> None:
        """Realizes UC32 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError

    def communicateWithFacilities(self) -> None:
        """Realizes UC35 "Communicate With Facilities" (R47)."""
        raise NotImplementedError

    def viewFacilityStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacilityRepresentative:
    """Source: R49, R50, R51"""
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC36 "Update Information And Types Of Material" (R49)."""
        raise NotImplementedError

    def viewFacilityStats(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R44, R45, R46, R47, R48, R49, R50, R51"""
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def viewUserStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError

    def communicateWithFacilities(self) -> None:
        """Realizes UC35 "Communicate With Facilities" (R47)."""
        raise NotImplementedError

    def viewFacilityStats(self) -> None:
        """Operation."""
        raise NotImplementedError
