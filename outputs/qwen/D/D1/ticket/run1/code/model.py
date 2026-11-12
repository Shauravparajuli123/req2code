"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R9, R10, R35, R36, R43, R45, R50, R51, R53"""
    personalInformation: _t.Optional[str] = None
    paymentDetails: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    password: _t.Optional[str] = None
    ticketOrderHistory: _t.Optional[str] = None
    upcomingEvents: _t.Optional[str] = None
    favoriteArtistsAndEvents: _t.Optional[str] = None

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
        """Realizes UC5 "Edit Preferences" (R5)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC6 "Change Password" (R6)."""
        raise NotImplementedError

    def editPersonalInformation(self) -> None:
        """Realizes UC7 "Edit Personal Information" (R7)."""
        raise NotImplementedError

    def seeTicketOrderHistory(self) -> None:
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
    """Source: R11, R12, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R33, R46, R47, R48"""
    calendarView: _t.Optional["CalendarView"] = None

    def readEventDetails(self) -> None:
        """Realizes UC11 "Read Event Details" (R11)."""
        raise NotImplementedError

    def buyTicketsDirectly(self) -> None:
        """Realizes UC12 "Buy Tickets Directly" (R12)."""
        raise NotImplementedError

    def purchaseTicket(self) -> None:
        """Realizes UC15 "Purchase Ticket" (R18, R19, R20)."""
        raise NotImplementedError

    def searchEvents(self) -> None:
        """Realizes UC16 "Search Events" (R28, R29, R30, R31, R32, R33)."""
        raise NotImplementedError

    def clickEventOnHomepage(self) -> None:
        """Realizes UC23 "Click Event On Homepage" (R48)."""
        raise NotImplementedError

    def seeUpcomingEventsCalendar(self) -> None:
        """Realizes UC21 "See Upcoming Events Calendar" (R46)."""
        raise NotImplementedError

    def seePopularEvents(self) -> None:
        """Realizes UC22 "See Popular Events" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R13, R41, R42, R43, R45"""
    ticket: _t.Optional[str] = None
    serviceFee: _t.Optional[float] = None
    bankAccount: _t.Optional[str] = None

    def resellTicketsDirectly(self) -> None:
        """Realizes UC13 "Resell Tickets Directly" (R11)."""
        raise NotImplementedError

    def uploadTicket(self) -> None:
        """Operation."""
        raise NotImplementedError

    def setPrice(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addDescription(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R27, R37, R38, R39, R40"""
    serviceFee: _t.Optional[float] = None
    fraudDetection: _t.Optional[str] = None

    def validateTickets(self) -> None:
        """Realizes UC17 "Validate Tickets" (R37)."""
        raise NotImplementedError

    def deductServiceFee(self) -> None:
        """Realizes UC18 "Deduct Service Fee" (R38)."""
        raise NotImplementedError


@_dc.dataclass
class Event:
    """Source: R11, R19, R20, R21, R22, R23, R34, R49, R50, R51, R52"""
    artist: _t.Optional[str] = None
    venue: _t.Optional[str] = None
    price: _t.Optional[float] = None
    type: _t.Optional[str] = None
    availability: _t.Optional[str] = None

    def seeEventInformation(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Ticket:
    """Source: R12, R13, R18, R20, R21, R22, R23, R24, R25, R26, R36, R37, R38, R39, R40, R41, R42, R43, R45"""
    price: _t.Optional[float] = None
    availability: _t.Optional[str] = None

    def addTicketToCart(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class PaymentMethod:
    """Source: R26"""
    type: _t.Optional[str] = None


@_dc.dataclass
class SearchResult:
    """Source: R28, R29, R30, R31, R32, R33"""
    event: _t.Optional[str] = None

    def searchEvents(self) -> None:
        """Realizes UC16 "Search Events" (R28, R29, R30, R31, R32, R33)."""
        raise NotImplementedError


@_dc.dataclass
class CalendarView:
    """Source: R46"""

    def seeUpcomingEventsCalendar(self) -> None:
        """Realizes UC21 "See Upcoming Events Calendar" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class SocialMedia:
    """Source: R50, R51, R52"""
    link: _t.Optional[str] = None


@_dc.dataclass
class MusicPlatform:
    """Source: R54"""
    link: _t.Optional[str] = None
