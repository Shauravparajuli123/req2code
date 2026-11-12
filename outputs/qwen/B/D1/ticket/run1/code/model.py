"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R9, R40, R43"""
    name: _t.Optional[str] = None
    dateOfBirth: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None
    favoriteEvents: _t.Optional[str] = None
    history: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    userProfile: _t.Optional["UserProfile"] = None
    preference: _t.Optional["Preference"] = None

    def createUser(self) -> None:
        """Operation."""
        raise NotImplementedError

    def saveInformation(self) -> None:
        """Realizes UC1 "Save Information" (R1)."""
        raise NotImplementedError

    def editInformation(self) -> None:
        """Realizes UC2 "Edit Information" (R7)."""
        raise NotImplementedError

    def seePreference(self) -> None:
        """Realizes UC3 "See Preference" (R5)."""
        raise NotImplementedError

    def seeContent(self) -> None:
        """Realizes UC4 "See Content" (R4)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC31 "Change Password" (R6)."""
        raise NotImplementedError

    def favoriteEvent(self) -> None:
        """Realizes UC32 "Favorite Event" (R53)."""
        raise NotImplementedError


@_dc.dataclass
class UserProfile:
    """Source: R1, R3, R5, R43"""
    preferences: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None

    def saveProfile(self) -> None:
        """Realizes UC1 "Save Information" (R1)."""
        raise NotImplementedError

    def editProfile(self) -> None:
        """Realizes UC2 "Edit Information" (R7)."""
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
    musicGenre: _t.Optional[str] = None
    eventTypes: _t.Optional[str] = None
    lastUpdated: _t.Optional[str] = None


@_dc.dataclass
class BankAccount:
    """Source: R42, R45"""
    iban: _t.Optional[str] = None


@_dc.dataclass
class Event:
    """Source: R11, R19, R23, R28, R30, R31, R32, R33, R46, R47, R49, R52"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None
    artist: _t.Optional[str] = None
    venue: _t.Optional[str] = None
    description: _t.Optional[str] = None
    type: _t.Optional[str] = None
    price: _t.Optional[float] = None
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)

    def seeEvent(self) -> None:
        """Realizes UC7 "See Event" (R11, R19, R46, R47)."""
        raise NotImplementedError

    def seeOverview(self) -> None:
        """Realizes UC6 "See Overview" (R9)."""
        raise NotImplementedError

    def seeSeat(self) -> None:
        """Realizes UC29 "See Seat" (R21, R22)."""
        raise NotImplementedError

    def seeType(self) -> None:
        """Realizes UC30 "See Type" (R23)."""
        raise NotImplementedError


@_dc.dataclass
class Venue:
    """Source: R11, R28, R30, R31, R32, R33, R46, R47"""
    name: _t.Optional[str] = None
    map: _t.Optional[str] = None


@_dc.dataclass
class Ticket:
    """Source: R12, R14, R18, R20, R24, R25, R26, R34, R35, R36, R37, R38, R39, R41, R42, R43, R44, R48, R50, R51, R53"""
    event: _t.Optional[str] = None
    type: _t.Optional[str] = None
    price: _t.Optional[float] = None
    seat: _t.Optional[str] = None

    def purchaseTicket(self) -> None:
        """Realizes UC8 "Purchase Ticket" (R12, R14, R20, R24, R25, R26)."""
        raise NotImplementedError

    def addTicket(self) -> None:
        """Realizes UC28 "Add Ticket" (R24)."""
        raise NotImplementedError

    def seeSeat(self) -> None:
        """Realizes UC29 "See Seat" (R21, R22)."""
        raise NotImplementedError

    def seeType(self) -> None:
        """Realizes UC30 "See Type" (R23)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Seat:
    """Source: R21, R22, R28, R30, R31, R32, R33, R46, R47, R52"""
    row: _t.Optional[int] = None
    column: _t.Optional[int] = None


@_dc.dataclass
class Company:
    """Source: R27, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45"""
    reseller: _t.Optional[str] = None
    serviceFee: _t.Optional[float] = None
    resellers: _t.List["Reseller"] = _dc.field(default_factory=list)


@_dc.dataclass
class Reseller:
    """Source: R41, R42, R43, R44, R45"""
    name: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None
    events: _t.List["Event"] = _dc.field(default_factory=list)

    def resellTicket(self) -> None:
        """Realizes UC26 "Resell Ticket" (R41)."""
        raise NotImplementedError

    def uploadTicket(self) -> None:
        """Operation."""
        raise NotImplementedError
