"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R10, R50, R51, R53"""
    name: _t.Optional[str] = None
    dateOfBirth: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    paymentDetails: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    favoriteArtists: _t.Optional[str] = None
    favoriteEvents: _t.Optional[str] = None

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

    def editPersonalInformation(self) -> None:
        """Realizes UC5 "Edit Personal Information" (R7)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC6 "Change Password" (R6)."""
        raise NotImplementedError

    def seeTicketOrderHistory(self) -> None:
        """Realizes UC7 "See Ticket Order History" (R8)."""
        raise NotImplementedError

    def seeUpcomingEvents(self) -> None:
        """Realizes UC8 "See Upcoming Events" (R9)."""
        raise NotImplementedError

    def favoriteArtistsAndEvents(self) -> None:
        """Realizes UC9 "Favorite Artists And Events" (R10)."""
        raise NotImplementedError


@_dc.dataclass
class Visitor:
    """Source: R11, R12, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R33, R46, R47, R48"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None
    event: _t.Optional["Event"] = None

    def readAboutEvent(self) -> None:
        """Realizes UC10 "Read About Event" (R11)."""
        raise NotImplementedError

    def buyTicketsDirectly(self) -> None:
        """Realizes UC11 "Buy Tickets Directly" (R12)."""
        raise NotImplementedError

    def purchaseTicket(self) -> None:
        """Realizes UC14 "Purchase Ticket" (R18, R19, R20, R21, R22, R23, R24, R25, R26)."""
        raise NotImplementedError

    def searchEvents(self) -> None:
        """Realizes UC15 "Search Events" (R28, R29, R30, R31, R32, R33, R34)."""
        raise NotImplementedError

    def clickOnEvent(self) -> None:
        """Realizes UC22 "Click On Event" (R48)."""
        raise NotImplementedError

    def findEventInformation(self) -> None:
        """Realizes UC23 "Find Event Information" (R49, R50, R51, R52)."""
        raise NotImplementedError

    def seeUpcomingEventsCalendar(self) -> None:
        """Realizes UC20 "See Upcoming Events Calendar" (R46)."""
        raise NotImplementedError

    def seePopularEvents(self) -> None:
        """Realizes UC21 "See Popular Events" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R13, R41, R42, R43, R44, R45"""
    bankAccount: _t.Optional[str] = None
    event: _t.Optional["Event"] = None

    def resellTicket(self) -> None:
        """Realizes UC19 "Resell Ticket" (R42, R43, R45)."""
        raise NotImplementedError

    def uploadDigitalTicket(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R27, R35, R36, R37, R38, R39, R40"""
    event: _t.Optional["Event"] = None

    def validateTickets(self) -> None:
        """Realizes UC16 "Validate Tickets" (R37)."""
        raise NotImplementedError

    def deductServiceFee(self) -> None:
        """Realizes UC17 "Deduct Service Fee" (R38)."""
        raise NotImplementedError

    def avoidFraud(self) -> None:
        """Realizes UC18 "Avoid Fraud" (R39, R40)."""
        raise NotImplementedError


@_dc.dataclass
class Event:
    """Source: R11, R19, R21, R22, R23, R24, R25, R26, R34, R49, R52, R54"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None
    artist: _t.Optional[str] = None
    venue: _t.Optional[str] = None
    genre: _t.Optional[str] = None
    price: _t.Optional[float] = None
    seats: _t.Optional[str] = None
    description: _t.Optional[str] = None
    linkToMusicPlatforms: _t.Optional[str] = None

    def seeAvailableSeats(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeTypesOfTickets(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTicketToShoppingCart(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seePaymentMethods(self) -> None:
        """Operation."""
        raise NotImplementedError
