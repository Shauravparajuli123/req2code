"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R9, R10, R16, R17, R28, R39, R40"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    history: _t.Optional[str] = None
    favoriteEvents: _t.Optional[str] = None
    password: _t.Optional[str] = None
    preference: _t.Optional["Preference"] = None
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)

    def saveInformation(self) -> None:
        """Realizes UC1 "Save Information" (R1)."""
        raise NotImplementedError

    def editInformation(self) -> None:
        """Realizes UC2 "Edit Information" (R7)."""
        raise NotImplementedError

    def seePreference(self) -> None:
        """Realizes UC3 "See Preference" (R5)."""
        raise NotImplementedError

    def seeHistory(self) -> None:
        """Realizes UC5 "See History" (R8)."""
        raise NotImplementedError

    def seeOverview(self) -> None:
        """Realizes UC6 "See Overview" (R9)."""
        raise NotImplementedError

    def seeFavoriteEvents(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC37 "Change Password" (R6)."""
        raise NotImplementedError


@_dc.dataclass
class Visitor:
    """Source: R11, R12, R13, R14, R18, R19, R20, R21, R22, R23, R24, R25, R26, R29, R30, R31, R32, R33, R34, R46, R47, R48"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None
    tickets: _t.Optional[str] = None

    def readEvent(self) -> None:
        """Realizes UC9 "Read Event" (R11)."""
        raise NotImplementedError

    def purchaseTicket(self) -> None:
        """Realizes UC8 "Purchase Ticket" (R12, R14, R20, R24, R25, R26)."""
        raise NotImplementedError

    def seeAvailableSeats(self) -> None:
        """Realizes UC25 "See Seat" (R21, R22)."""
        raise NotImplementedError

    def seeTicketTypes(self) -> None:
        """Realizes UC26 "See Type" (R23)."""
        raise NotImplementedError

    def addTicketToCart(self) -> None:
        """Realizes UC24 "Add Ticket" (R24)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC27 "See Order Summary" (R25)."""
        raise NotImplementedError

    def seePaymentMethods(self) -> None:
        """Realizes UC28 "See List" (R26)."""
        raise NotImplementedError

    def searchEvents(self) -> None:
        """Realizes UC32 "Find List" (R10)."""
        raise NotImplementedError

    def filterSearchResults(self) -> None:
        """Realizes UC12 "Filter Search" (R32, R33, R34)."""
        raise NotImplementedError

    def sortSearchResults(self) -> None:
        """Realizes UC14 "Sort Search Result" (R31)."""
        raise NotImplementedError

    def seeUpcomingEvents(self) -> None:
        """Operation."""
        raise NotImplementedError

    def clickEvent(self) -> None:
        """Realizes UC11 "Click Event" (R48)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R11, R12, R13, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45"""
    bankAccount: _t.Optional[str] = None
    tickets: _t.Optional[str] = None

    def resellTicket(self) -> None:
        """Realizes UC22 "Resell Ticket" (R41)."""
        raise NotImplementedError

    def uploadTicket(self) -> None:
        """Operation."""
        raise NotImplementedError

    def setTicketPrice(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addDescription(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R27, R38, R39, R40"""
    resellers: _t.List["Reseller"] = _dc.field(default_factory=list)
    events: _t.List["Event"] = _dc.field(default_factory=list)

    def deductServiceFee(self) -> None:
        """Realizes UC18 "Deduct Service Fee" (R38)."""
        raise NotImplementedError

    def avoidBehavior(self) -> None:
        """Realizes UC16 "Avoid Behavior" (R39)."""
        raise NotImplementedError

    def protectUser(self) -> None:
        """Realizes UC17 "Protect User" (R40)."""
        raise NotImplementedError


@_dc.dataclass
class Artist:
    """Source: R49, R50, R51, R52, R53, R54"""
    linkToWebsite: _t.Optional[str] = None
    linkToSocialMedia: _t.Optional[str] = None
    description: _t.Optional[str] = None

    def findInformation(self) -> None:
        """Realizes UC31 "Find Information" (R49)."""
        raise NotImplementedError

    def seeEventPage(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Event:
    """Source: R11, R12, R13, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R33, R34, R46, R47, R48"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None
    artist: _t.Optional[str] = None
    venue: _t.Optional[str] = None
    type: _t.Optional[str] = None
    description: _t.Optional[str] = None
    price: _t.Optional[float] = None
    tickets: _t.Optional[str] = None

    def seeEventPage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeDescription(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeType(self) -> None:
        """Realizes UC26 "See Type" (R23)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC27 "See Order Summary" (R25)."""
        raise NotImplementedError

    def seePaymentMethods(self) -> None:
        """Realizes UC28 "See List" (R26)."""
        raise NotImplementedError

    def searchEvents(self) -> None:
        """Realizes UC32 "Find List" (R10)."""
        raise NotImplementedError

    def filterSearchResults(self) -> None:
        """Realizes UC12 "Filter Search" (R32, R33, R34)."""
        raise NotImplementedError

    def sortSearchResults(self) -> None:
        """Realizes UC14 "Sort Search Result" (R31)."""
        raise NotImplementedError

    def seeUpcomingEvents(self) -> None:
        """Operation."""
        raise NotImplementedError

    def clickEvent(self) -> None:
        """Realizes UC11 "Click Event" (R48)."""
        raise NotImplementedError


@_dc.dataclass
class Ticket:
    """Source: R12, R13, R19, R20, R21, R22, R23, R24, R25, R26, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45"""
    type: _t.Optional[str] = None
    price: _t.Optional[float] = None
    reseller: _t.Optional[str] = None
    valid: _t.Optional[bool] = None

    def validateTicket(self) -> None:
        """Realizes UC19 "Validate Ticket" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Address:
    """Source: R1"""
    street: _t.Optional[str] = None
    city: _t.Optional[str] = None
    state: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None


@_dc.dataclass
class Preference:
    """Source: R3, R5"""
    genre: _t.Optional[str] = None
    eventTypes: _t.Optional[str] = None


@_dc.dataclass
class BankAccount:
    """Source: R45"""
    iban: _t.Optional[str] = None


@_dc.dataclass
class Link:
    """Source: R50, R51, R53, R54"""
    url: _t.Optional[str] = None


@_dc.dataclass
class Venue:
    """Source: R11, R28, R48"""
    name: _t.Optional[str] = None
    map: _t.Optional[str] = None
