"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R10, R15, R16, R17, R28, R33, R49, R53"""
    name: _t.Optional[str] = None
    dateOfBirth: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    personalInfo: _t.Optional[str] = None
    paymentDetails: _t.Optional[str] = None
    favoriteArtists: _t.Optional[str] = None
    favoriteEvents: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def savePersonalInformation(self) -> None:
        """Realizes UC1 "Save Personal Information" (R1)."""
        raise NotImplementedError

    def savePaymentDetails(self) -> None:
        """Realizes UC2 "Save Payment Details" (R2)."""
        raise NotImplementedError

    def fillOutSurvey(self) -> None:
        """Realizes UC3 "Fill Out Survey" (R3)."""
        raise NotImplementedError

    def seePersonalizedContent(self) -> None:
        """Realizes UC4 "See Personalized Content" (R4)."""
        raise NotImplementedError

    def editPreferences(self) -> None:
        """Realizes UC7 "See And Edit Preferences" (R5)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC6 "Change Password" (R6)."""
        raise NotImplementedError

    def editPersonalInformation(self) -> None:
        """Realizes UC5 "Edit Personal Information" (R7)."""
        raise NotImplementedError

    def seeOrderHistory(self) -> None:
        """Realizes UC8 "See Ticket Order History" (R8)."""
        raise NotImplementedError

    def seeUpcomingEvents(self) -> None:
        """Realizes UC9 "See Upcoming Events" (R9)."""
        raise NotImplementedError

    def findFavoriteArtistsAndEvents(self) -> None:
        """Realizes UC10 "Find Favorite Artists And Events" (R10)."""
        raise NotImplementedError


@_dc.dataclass
class Visitor:
    """Source: R11, R12, R18, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R34, R46, R47, R48"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None

    def readAboutEvent(self) -> None:
        """Realizes UC11 "Read About Event" (R11)."""
        raise NotImplementedError

    def buyTicketsDirectly(self) -> None:
        """Realizes UC12 "Buy Tickets Directly" (R12)."""
        raise NotImplementedError

    def seeAvailableTickets(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeSeatMap(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeTicketTypes(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTicketsToCart(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchEvents(self) -> None:
        """Realizes UC21 "Find Information About Event" (R49)."""
        raise NotImplementedError

    def clickOnEvent(self) -> None:
        """Realizes UC20 "Click On Event On Homepage" (R48)."""
        raise NotImplementedError

    def sortSearchResultsByDate(self) -> None:
        """Operation."""
        raise NotImplementedError

    def filterSearchByPrice(self) -> None:
        """Operation."""
        raise NotImplementedError

    def filterSearchByVenue(self) -> None:
        """Operation."""
        raise NotImplementedError

    def filterSearchByGenre(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeCalendarView(self) -> None:
        """Realizes UC18 "See Calendar View Of Events" (R46)."""
        raise NotImplementedError

    def seePopularEvents(self) -> None:
        """Realizes UC19 "See Popular Events" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R13, R35, R36, R37, R38, R39, R40, R41, R42, R43, R45"""
    name: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None

    def resellTicketsDirectly(self) -> None:
        """Realizes UC13 "Resell Tickets Directly" (R41)."""
        raise NotImplementedError

    def uploadDigitalTicket(self) -> None:
        """Realizes UC14 "Upload Digital Ticket" (R42)."""
        raise NotImplementedError

    def setTicketPrice(self) -> None:
        """Realizes UC15 "Set Ticket Price" (R43)."""
        raise NotImplementedError

    def addTicketDescription(self) -> None:
        """Realizes UC16 "Add Ticket Description" (R44)."""
        raise NotImplementedError

    def saveBankAccount(self) -> None:
        """Realizes UC17 "Save Bank Account" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Artist:
    """Source: R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    website: _t.Optional[str] = None
    socialMedia: _t.Optional[str] = None
    description: _t.Optional[str] = None
    musicPlatforms: _t.Optional[str] = None

    def findInformationAboutEvent(self) -> None:
        """Realizes UC21 "Find Information About Event" (R49)."""
        raise NotImplementedError

    def linkToWebsite(self) -> None:
        """Realizes UC22 "Link To Website" (R50)."""
        raise NotImplementedError

    def linkToSocialMedia(self) -> None:
        """Realizes UC23 "Link To Social Media" (R51)."""
        raise NotImplementedError

    def descriptionOfArtistAndEvent(self) -> None:
        """Realizes UC24 "Description Of Artist And Event" (R52)."""
        raise NotImplementedError

    def favoriteEventsOrArtists(self) -> None:
        """Realizes UC25 "Favorite Events Or Artists" (R53)."""
        raise NotImplementedError

    def linkToMusicPlatforms(self) -> None:
        """Realizes UC26 "Link To Music Platforms" (R54)."""
        raise NotImplementedError
