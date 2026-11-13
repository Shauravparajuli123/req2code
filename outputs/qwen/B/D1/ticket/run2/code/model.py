"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R10, R49, R53"""
    name: _t.Optional[str] = None
    dateOfBirth: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None
    favoriteEvents: _t.Optional[str] = None
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

    def changePassword(self) -> None:
        """Realizes UC31 "Change Password" (R6)."""
        raise NotImplementedError

    def favoriteEvent(self) -> None:
        """Realizes UC32 "Favorite Event" (R53)."""
        raise NotImplementedError


@_dc.dataclass
class Visitor:
    """Source: R11, R12, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R33, R46, R47, R48"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None
    searchResults: _t.Optional[str] = None
    events: _t.List["Event"] = _dc.field(default_factory=list)
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)
    seats: _t.List["Seat"] = _dc.field(default_factory=list)

    def readEvent(self) -> None:
        """Realizes UC9 "Read Event" (R11)."""
        raise NotImplementedError

    def purchaseTicket(self) -> None:
        """Realizes UC8 "Purchase Ticket" (R12, R14, R18, R20, R21, R22, R23, R24, R25)."""
        raise NotImplementedError

    def seeAvailableSeats(self) -> None:
        """Realizes UC29 "See Seat" (R21, R22)."""
        raise NotImplementedError

    def seeTicketTypes(self) -> None:
        """Realizes UC30 "See Type" (R23)."""
        raise NotImplementedError

    def addTicketToCart(self) -> None:
        """Realizes UC27 "Add Ticket" (R24)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC28 "See Order Summary" (R25)."""
        raise NotImplementedError

    def sortSearchResults(self) -> None:
        """Realizes UC15 "Sort Search Result" (R31)."""
        raise NotImplementedError

    def filterSearchResults(self) -> None:
        """Realizes UC13 "Filter Search" (R32)."""
        raise NotImplementedError

    def filterSearchResultsByVenue(self) -> None:
        """Realizes UC14 "Filter Search Result" (R33)."""
        raise NotImplementedError

    def filterSearchResultsByGenre(self) -> None:
        """Realizes UC14 "Filter Search Result" (R33)."""
        raise NotImplementedError

    def seeUpcomingEvents(self) -> None:
        """Realizes UC6 "See Overview" (R9)."""
        raise NotImplementedError

    def seePopularEvents(self) -> None:
        """Realizes UC6 "See Overview" (R9)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R31, R34, R35, R36, R37, R38, R39, R41, R42, R43, R44, R45"""
    bankAccount: _t.Optional[str] = None
    ticket: _t.Optional[str] = None
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)

    def resellTicket(self) -> None:
        """Realizes UC25 "Resell Ticket" (R41)."""
        raise NotImplementedError

    def saveBankAccount(self) -> None:
        """Realizes UC26 "Save Bank Account" (R45)."""
        raise NotImplementedError

    def uploadTicket(self) -> None:
        """Operation."""
        raise NotImplementedError

    def setTicketPrice(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addDescription(self) -> None:
        """Realizes UC17 "Have Description" (R52)."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R27, R35, R38, R39, R40"""

    def validateTicket(self) -> None:
        """Realizes UC21 "Validate Ticket" (R37)."""
        raise NotImplementedError

    def deductServiceFee(self) -> None:
        """Realizes UC22 "Deduct Service Fee" (R38)."""
        raise NotImplementedError

    def avoidBehavior(self) -> None:
        """Realizes UC23 "Avoid Behavior" (R39)."""
        raise NotImplementedError

    def protectUser(self) -> None:
        """Realizes UC24 "Protect User" (R40)."""
        raise NotImplementedError


@_dc.dataclass
class Event:
    """Source: R11, R19, R21, R22, R23, R29, R33, R34, R49, R50, R51, R52, R54"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None
    artist: _t.Optional[str] = None
    venue: _t.Optional[str] = None
    type: _t.Optional[str] = None
    description: _t.Optional[str] = None
    linkToMusicPlatforms: _t.Optional[str] = None

    def seeEvent(self) -> None:
        """Realizes UC9 "Read Event" (R11)."""
        raise NotImplementedError

    def seeSeats(self) -> None:
        """Realizes UC29 "See Seat" (R21, R22)."""
        raise NotImplementedError

    def seeTypes(self) -> None:
        """Realizes UC30 "See Type" (R23)."""
        raise NotImplementedError


@_dc.dataclass
class Ticket:
    """Source: R12, R18, R19, R20, R24, R25, R36, R37, R38, R41, R42, R43"""
    type: _t.Optional[str] = None
    price: _t.Optional[float] = None
    reseller: _t.Optional[str] = None

    def purchaseTicket(self) -> None:
        """Realizes UC8 "Purchase Ticket" (R12, R14, R18, R20, R21, R22, R23, R24, R25)."""
        raise NotImplementedError

    def seeTicketTypes(self) -> None:
        """Realizes UC30 "See Type" (R23)."""
        raise NotImplementedError

    def addTicketToCart(self) -> None:
        """Realizes UC27 "Add Ticket" (R24)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC28 "See Order Summary" (R25)."""
        raise NotImplementedError


@_dc.dataclass
class Address:
    """Source: R1"""
    pass


@_dc.dataclass
class Preference:
    """Source: R3, R5"""
    pass


@_dc.dataclass
class BankAccount:
    """Source: R45"""
    pass


@_dc.dataclass
class SearchResult:
    """Source: R28, R29, R30, R31, R32, R33, R34"""
    pass


@_dc.dataclass
class Seat:
    """Source: R21, R22"""
    pass


@_dc.dataclass
class Venue:
    """Source: R11, R22"""
    pass
