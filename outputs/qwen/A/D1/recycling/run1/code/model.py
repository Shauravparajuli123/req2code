"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R2, R14, R15, R17, R19, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R39, R41, R42, R43, R44, R45, R46, R47, R48"""
    email: _t.Optional[str] = None
    favorites: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None
    password: _t.Optional[str] = None
    feedback: _t.Optional[str] = None
    device: _t.Optional[str] = None
    activityLogs: _t.Optional[str] = None
    stats: _t.Optional[str] = None
    schedules: _t.Optional[str] = None
    environmentFriendly: _t.Optional[bool] = None
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

    def giveEmailID(self) -> None:
        """Realizes UC7 "Enter Email ID" (R8)."""
        raise NotImplementedError

    def viewMapOfRecyclingBins(self) -> None:
        """Realizes UC8 "View Map Of Recycling Bins" (R9)."""
        raise NotImplementedError

    def viewMapOfSpecialWasteSites(self) -> None:
        """Realizes UC9 "View Map Of Special Waste Sites" (R10)."""
        raise NotImplementedError

    def viewSafeDisposalEvents(self) -> None:
        """Realizes UC10 "View Safe Disposal Events" (R11)."""
        raise NotImplementedError

    def viewUserDocumentation(self) -> None:
        """Realizes UC11 "View User Documentation" (R13)."""
        raise NotImplementedError

    def viewFeedbackForInvalidZipCode(self) -> None:
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

    def accessDataRelatedToCompany(self) -> None:
        """Realizes UC19 "Access Data Related To Company" (R24)."""
        raise NotImplementedError

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC20 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def accessFullEmployeeInformation(self) -> None:
        """Realizes UC21 "Access Full Employee Information" (R26)."""
        raise NotImplementedError

    def accessAPI(self) -> None:
        """Realizes UC22 "Access API" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC23 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendUIUXLessons(self) -> None:
        """Realizes UC24 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError

    def viewRecyclingCenterLocations(self) -> None:
        """Realizes UC25 "View Recycling Center Locations" (R36)."""
        raise NotImplementedError

    def uploadWeeklySchedule(self) -> None:
        """Realizes UC26 "Upload Weekly Schedule" (R37)."""
        raise NotImplementedError

    def linkEmailAccount(self) -> None:
        """Realizes UC27 "Link Email Account" (R38)."""
        raise NotImplementedError

    def contactAdministrators(self) -> None:
        """Realizes UC28 "Contact Administrators" (R39)."""
        raise NotImplementedError

    def addRecyclingCenterInformation(self) -> None:
        """Realizes UC29 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def viewUserErrorLogs(self) -> None:
        """Realizes UC30 "View User Error Logs" (R41)."""
        raise NotImplementedError

    def onboardRecyclingCenters(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def updateRecyclingCenterInformation(self) -> None:
        """Realizes UC32 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUsersStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError

    def communicateWithFacilities(self) -> None:
        """Realizes UC35 "Communicate With Facilities" (R47)."""
        raise NotImplementedError

    def viewEnvironmentFriendlyFacilities(self) -> None:
        """Realizes UC36 "View Environment Friendly Facilities" (R48)."""
        raise NotImplementedError

    def updateInformationAndMaterialTypes(self) -> None:
        """Realizes UC37 "Update Information And Material Types" (R49)."""
        raise NotImplementedError

    def accessUserStatsAndSchedules(self) -> None:
        """Realizes UC38 "Access User Stats And Schedules" (R50)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R41, R42, R46, R47"""
    blockedUsers: _t.Optional[str] = None
    userFeedback: _t.Optional[str] = None
    dashboardStats: _t.Optional[str] = None
    encryptionKey: _t.Optional[str] = None
    recyclingFacilities: _t.List["RecyclingFacility"] = _dc.field(default_factory=list)
    users: _t.List["User"] = _dc.field(default_factory=list)

    def addOrRemoveFacilityInfo(self) -> None:
        """Realizes UC14 "Add Or Remove Recycling Facilities Information" (R16)."""
        raise NotImplementedError

    def readUserFeedbackAndComplaints(self) -> None:
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


@_dc.dataclass
class Executive:
    """Source: R24"""
    companyStats: _t.Optional[str] = None

    def accessDataRelatedToCompany(self) -> None:
        """Realizes UC19 "Access Data Related To Company" (R24)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R25, R26"""
    device: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def accessRoutePlanningSystem(self) -> None:
        """Realizes UC20 "Access Route Planning System" (R25)."""
        raise NotImplementedError

    def accessFullEmployeeInformation(self) -> None:
        """Realizes UC21 "Access Full Employee Information" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class HREmployee:
    """Source: R26"""
    employeeStats: _t.Optional[str] = None

    def accessFullEmployeeInformation(self) -> None:
        """Realizes UC21 "Access Full Employee Information" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class Developer:
    """Source: R27, R28, R34, R35"""
    apiAccess: _t.Optional[bool] = None
    uiUXLessons: _t.Optional[bool] = None

    def accessAPI(self) -> None:
        """Realizes UC22 "Access API" (R27)."""
        raise NotImplementedError

    def useBootstrap(self) -> None:
        """Realizes UC23 "Use Bootstrap" (R34)."""
        raise NotImplementedError

    def attendUIUXLessons(self) -> None:
        """Realizes UC24 "Attend UI UX Lessons" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R43, R44, R45"""
    userStats: _t.Optional[str] = None
    recyclingFacilities: _t.List["RecyclingFacility"] = _dc.field(default_factory=list)

    def updateRecyclingCenterInformation(self) -> None:
        """Realizes UC32 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUsersStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R40, R42, R46, R47, R48, R49, R50, R51"""
    facilityInfo: _t.Optional[str] = None
    environmentFriendly: _t.Optional[bool] = None
    stats: _t.Optional[str] = None
    materialTypes: _t.Optional[str] = None

    def addRecyclingCenterInformation(self) -> None:
        """Realizes UC29 "Add Recycling Center Information" (R40)."""
        raise NotImplementedError

    def viewUserErrorLogs(self) -> None:
        """Realizes UC30 "View User Error Logs" (R41)."""
        raise NotImplementedError

    def onboardRecyclingCenters(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def updateInformationAndMaterialTypes(self) -> None:
        """Realizes UC37 "Update Information And Material Types" (R49)."""
        raise NotImplementedError

    def viewUsersStats(self) -> None:
        """Realizes UC33 "View Users Stats" (R44)."""
        raise NotImplementedError

    def communicateWithSiteAdmin(self) -> None:
        """Realizes UC39 "Communicate With Site Admin" (R51)."""
        raise NotImplementedError
