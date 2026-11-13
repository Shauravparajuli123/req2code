"""Code skeleton generated from the shared model of D1/recycling.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R2, R14, R15, R17, R19, R29, R39"""
    email: _t.Optional[str] = None
    favorites: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None
    admin: _t.Optional["Admin"] = None

    def viewPublicInformation(self) -> None:
        """Realizes UC1 "View Public Information" (R2)."""
        raise NotImplementedError

    def getNearbyFacilities(self) -> None:
        """Realizes UC2 "Enter Zip Code And Get Nearby Facilities" (R3)."""
        raise NotImplementedError

    def getFacilityHours(self) -> None:
        """Realizes UC3 "Get Facility Hours" (R4)."""
        raise NotImplementedError

    def selectRecyclableWasteTypes(self) -> None:
        """Realizes UC5 "Select Recyclable Waste Types" (R6)."""
        raise NotImplementedError

    def addFavorite(self) -> None:
        """Realizes UC6 "Add Favorites" (R7)."""
        raise NotImplementedError

    def viewEmailFeedback(self) -> None:
        """Realizes UC12 "View Feedback For Invalid Zip Code" (R14)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC13 "Create Account" (R15)."""
        raise NotImplementedError

    def viewDocumentation(self) -> None:
        """Realizes UC11 "View User Documentation" (R13)."""
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

    def viewSafeDisposalEvents(self) -> None:
        """Realizes UC10 "View Safe Disposal Events" (R11)."""
        raise NotImplementedError

    def viewMapOfRecyclingBins(self) -> None:
        """Realizes UC8 "View Map Of Recycling Bins" (R9)."""
        raise NotImplementedError

    def viewMapOfSpecialWasteSites(self) -> None:
        """Realizes UC9 "View Map Of Special Waste Sites" (R10)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R16, R17, R21, R22, R23, R31, R41, R46, R47"""
    blockedUsers: _t.Optional[str] = None
    siteStatus: _t.Optional[str] = None
    recyclingFacility: _t.Optional["RecyclingFacility"] = None
    user: _t.Optional["User"] = None

    def addOrRemoveFacilityInfo(self) -> None:
        """Realizes UC14 "Add Or Remove Recycling Facilities Information" (R16)."""
        raise NotImplementedError

    def readFeedbackAndComplaints(self) -> None:
        """Realizes UC15 "Read User Feedback And Complaints" (R17)."""
        raise NotImplementedError

    def blockUser(self) -> None:
        """Realizes UC16 "Block Specific Users" (R21)."""
        raise NotImplementedError

    def viewSiteStatusDashboard(self) -> None:
        """Realizes UC17 "View Site Status Dashboard" (R22)."""
        raise NotImplementedError

    def encryptData(self) -> None:
        """Realizes UC18 "Encrypt Data" (R23)."""
        raise NotImplementedError

    def viewUserErrorLogs(self) -> None:
        """Realizes UC30 "View User Error Logs" (R41)."""
        raise NotImplementedError

    def onboardFacility(self) -> None:
        """Realizes UC31 "Onboard Recycling Centers" (R42)."""
        raise NotImplementedError

    def viewUsageStatsAndLocations(self) -> None:
        """Realizes UC35 "View Usage Stats And Locations" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class Superuser:
    """Source: R43, R44, R45"""
    recyclingFacility: _t.Optional["RecyclingFacility"] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC32 "Update Recycling Center Information" (R43)."""
        raise NotImplementedError

    def viewUserStats(self) -> None:
        """Realizes UC33 "View User Stats" (R44)."""
        raise NotImplementedError

    def replyToUserQuestions(self) -> None:
        """Realizes UC34 "Reply To User Questions" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class RecyclingFacility:
    """Source: R48, R49, R50, R51"""
    facilityInfo: _t.Optional[str] = None
    materialTypes: _t.Optional[str] = None

    def updateFacilityInfo(self) -> None:
        """Realizes UC37 "Update Information And Material Types" (R49)."""
        raise NotImplementedError

    def viewUserStatsAndSchedules(self) -> None:
        """Realizes UC38 "Access User Stats And Schedules" (R50)."""
        raise NotImplementedError


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError
