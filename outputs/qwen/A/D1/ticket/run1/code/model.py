"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R9, R35, R36, R37, R38, R39, R40"""
    name: _t.Optional[str] = None
    dateOfBirth: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    paymentDetails: _t.Optional[str] = None
    password: _t.Optional[str] = None
    favoriteArtists: _t.Optional[str] = None
    favoriteEvents: _t.Optional[str] = None
    ticketHistory: _t.Optional[str] = None
    profileSurvey: _t.Optional[str] = None
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)

    def createProfile(self) -> None:
        """Realizes UC1 "Create Profile" (R1, R5, R6, R7, R15, R16, R17)."""
        raise NotImplementedError

    def viewPersonalInformation(self) -> None:
        """Realizes UC2 "View Personal Information" (R5, R7, R17)."""
        raise NotImplementedError

    def editPersonalInformation(self) -> None:
        """Realizes UC3 "Edit Personal Information" (R7, R17)."""
        raise NotImplementedError

    def viewTicketHistory(self) -> None:
        """Realizes UC4 "View Ticket History" (R8, R17)."""
        raise NotImplementedError

    def viewUpcomingEvents(self) -> None:
        """Realizes UC5 "View Upcoming Events" (R9, R17)."""
        raise NotImplementedError

    def favoriteEventsOrArtists(self) -> None:
        """Realizes UC6 "Favorite Events Or Artists" (R10, R17, R53)."""
        raise NotImplementedError

    def searchForEvents(self) -> None:
        """Realizes UC7 "Search For Events" (R11, R18, R28, R29, R30, R31, R32, R33, R46, R47, R48, R53)."""
        raise NotImplementedError

    def buyTickets(self) -> None:
        """Realizes UC8 "Buy Tickets" (R12, R18, R19, R20, R21, R22, R23, R24, R25, R26, R17)."""
        raise NotImplementedError

    def resellTickets(self) -> None:
        """Realizes UC9 "Resell Tickets" (R35, R36, R37, R38, R39, R40, R41, R42, R43, R45)."""
        raise NotImplementedError

    def viewEventInformation(self) -> None:
        """Realizes UC10 "View Event Information" (R11, R49, R50, R51, R52, R53, R54)."""
        raise NotImplementedError


@_dc.dataclass
class Event:
    """Source: R19, R20, R21, R22, R23, R24, R25, R26, R46, R47, R48, R52, R53, R54"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None
    location: _t.Optional[str] = None
    artist: _t.Optional[str] = None
    type: _t.Optional[str] = None
    price: _t.Optional[float] = None
    venue: _t.Optional[str] = None
    genre: _t.Optional[str] = None
    ticketType: _t.Optional[str] = None
    seats: _t.Optional[str] = None
    description: _t.Optional[str] = None
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)

    def viewEventInformation(self) -> None:
        """Realizes UC10 "View Event Information" (R11, R49, R50, R51, R52, R53, R54)."""
        raise NotImplementedError

    def searchForEvents(self) -> None:
        """Realizes UC7 "Search For Events" (R11, R18, R28, R29, R30, R31, R32, R33, R46, R47, R48, R53)."""
        raise NotImplementedError

    def buyTickets(self) -> None:
        """Realizes UC8 "Buy Tickets" (R12, R18, R19, R20, R21, R22, R23, R24, R25, R26, R17)."""
        raise NotImplementedError

    def resellTickets(self) -> None:
        """Realizes UC9 "Resell Tickets" (R35, R36, R37, R38, R39, R40, R41, R42, R43, R45)."""
        raise NotImplementedError

    def viewEventPage(self) -> None:
        """Realizes UC10 "View Event Information" (R11, R49, R50, R51, R52, R53, R54)."""
        raise NotImplementedError


@_dc.dataclass
class Ticket:
    """Source: R19, R20, R21, R22, R23, R24, R25, R26, R46, R47, R48, R52, R53, R54"""
    type: _t.Optional[str] = None
    price: _t.Optional[float] = None
    seat: _t.Optional[str] = None
    event: _t.Optional[str] = None

    def addTicketToCart(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewOrderSummary(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewPaymentMethods(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45"""
    name: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)

    def resellTickets(self) -> None:
        """Realizes UC9 "Resell Tickets" (R35, R36, R37, R38, R39, R40, R41, R42, R43, R45)."""
        raise NotImplementedError

    def uploadTicket(self) -> None:
        """Realizes UC9 "Resell Tickets" (R35, R36, R37, R38, R39, R40, R41, R42, R43, R45)."""
        raise NotImplementedError

    def setTicketPrice(self) -> None:
        """Realizes UC9 "Resell Tickets" (R35, R36, R37, R38, R39, R40, R41, R42, R43, R45)."""
        raise NotImplementedError

    def addDescription(self) -> None:
        """Realizes UC9 "Resell Tickets" (R35, R36, R37, R38, R39, R40, R41, R42, R43, R45)."""
        raise NotImplementedError
