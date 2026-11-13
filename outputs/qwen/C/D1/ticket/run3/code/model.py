"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R10, R11, R12, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R39, R40"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    history: _t.Optional[str] = None
    profile: _t.Optional[str] = None
    userProfile: _t.Optional["UserProfile"] = None
    preference: _t.Optional["Preference"] = None

    def saveInformation(self) -> None:
        """Realizes UC1 "Save Information" (R1)."""
        raise NotImplementedError

    def fillInformation(self) -> None:
        """Realizes UC12 "Fill Information" (R16)."""
        raise NotImplementedError

    def fillName(self) -> None:
        """Realizes UC13 "Fill Name" (R15)."""
        raise NotImplementedError

    def fillSurvey(self) -> None:
        """Realizes UC14 "Fill Survey" (R3)."""
        raise NotImplementedError

    def seeContent(self) -> None:
        """Realizes UC2 "See Content" (R4)."""
        raise NotImplementedError

    def seeEvent(self) -> None:
        """Realizes UC3 "See Event" (R11, R19, R46, R47)."""
        raise NotImplementedError

    def purchaseTicket(self) -> None:
        """Realizes UC4 "Purchase Ticket" (R12, R14, R20, R24, R25, R26)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC8 "See Order Summary" (R25)."""
        raise NotImplementedError

    def seeOverview(self) -> None:
        """Realizes UC9 "See Overview" (R9)."""
        raise NotImplementedError

    def seeSeat(self) -> None:
        """Realizes UC10 "See Seat" (R21, R22)."""
        raise NotImplementedError

    def seeType(self) -> None:
        """Realizes UC11 "See Type" (R23)."""
        raise NotImplementedError

    def editInformation(self) -> None:
        """Realizes UC7 "Edit Information" (R7)."""
        raise NotImplementedError

    def seeHistory(self) -> None:
        """Realizes UC5 "See History" (R8)."""
        raise NotImplementedError

    def seePreference(self) -> None:
        """Realizes UC6 "See Preference" (R5)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC32 "Change Password" (R6)."""
        raise NotImplementedError


@_dc.dataclass
class UserProfile:
    """Source: R1, R10, R17"""
    preferences: _t.Optional[str] = None
    favoriteArtists: _t.Optional[str] = None
    favoriteEvents: _t.Optional[str] = None


@_dc.dataclass
class Preference:
    """Source: R3, R5"""
    genre: _t.Optional[str] = None
    eventTypes: _t.Optional[str] = None


@_dc.dataclass
class Address:
    """Source: R1"""
    street: _t.Optional[str] = None
    city: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None


@_dc.dataclass
class Ticket:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26"""
    type: _t.Optional[str] = None
    seat: _t.Optional[str] = None
    price: _t.Optional[float] = None
    event: _t.Optional[str] = None

    def addTicketToCart(self) -> None:
        """Realizes UC4 "Purchase Ticket" (R12, R14, R20, R24, R25, R26)."""
        raise NotImplementedError


@_dc.dataclass
class Seat:
    """Source: R21, R22"""
    row: _t.Optional[int] = None
    column: _t.Optional[int] = None


@_dc.dataclass
class Event:
    """Source: R11, R19, R23, R28, R29, R30, R31, R32, R33, R46, R47, R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None
    artist: _t.Optional[str] = None
    venue: _t.Optional[str] = None
    type: _t.Optional[str] = None
    description: _t.Optional[str] = None
    link: _t.Optional[str] = None
    tickets: _t.List["Ticket"] = _dc.field(default_factory=list)

    def seeEvent(self) -> None:
        """Realizes UC3 "See Event" (R11, R19, R46, R47)."""
        raise NotImplementedError

    def clickEvent(self) -> None:
        """Realizes UC20 "Click Event" (R48)."""
        raise NotImplementedError


@_dc.dataclass
class Link:
    """Source: R50, R51, R52, R53, R54"""
    url: _t.Optional[str] = None


@_dc.dataclass
class Artist:
    """Source: R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    link: _t.Optional[str] = None


@_dc.dataclass
class Visitor:
    """Source: R11, R12, R18, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R33, R46, R47, R48, R53, R54"""
    events: _t.Optional[str] = None

    def seeContent(self) -> None:
        """Realizes UC2 "See Content" (R4)."""
        raise NotImplementedError

    def purchaseTicket(self) -> None:
        """Realizes UC4 "Purchase Ticket" (R12, R14, R20, R24, R25, R26)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC8 "See Order Summary" (R25)."""
        raise NotImplementedError

    def seeOverview(self) -> None:
        """Realizes UC9 "See Overview" (R9)."""
        raise NotImplementedError

    def seeSeat(self) -> None:
        """Realizes UC10 "See Seat" (R21, R22)."""
        raise NotImplementedError

    def seeType(self) -> None:
        """Realizes UC11 "See Type" (R23)."""
        raise NotImplementedError

    def seeEvent(self) -> None:
        """Realizes UC3 "See Event" (R11, R19, R46, R47)."""
        raise NotImplementedError

    def clickEvent(self) -> None:
        """Realizes UC20 "Click Event" (R48)."""
        raise NotImplementedError

    def filterList(self) -> None:
        """Realizes UC15 "Filter List" (R34)."""
        raise NotImplementedError

    def filterSearch(self) -> None:
        """Realizes UC16 "Filter Search" (R32)."""
        raise NotImplementedError

    def filterSearchResult(self) -> None:
        """Realizes UC17 "Filter Search Result" (R33)."""
        raise NotImplementedError

    def sortSearchResult(self) -> None:
        """Realizes UC18 "Sort Search Result" (R31)."""
        raise NotImplementedError

    def landEventPage(self) -> None:
        """Realizes UC19 "Land Event Page" (R29)."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R27, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45"""
    resellers: _t.Optional[str] = None
    minimumResellPrice: _t.Optional[float] = None
    searchEngine: _t.Optional[str] = None

    def haveBuyingProcess(self) -> None:
        """Realizes UC21 "Have Buying Process" (R27)."""
        raise NotImplementedError

    def validateTicket(self) -> None:
        """Realizes UC27 "Validate Ticket" (R37)."""
        raise NotImplementedError

    def avoidBehavior(self) -> None:
        """Realizes UC28 "Avoid Behavior" (R39)."""
        raise NotImplementedError

    def protectUser(self) -> None:
        """Realizes UC29 "Protect User" (R40)."""
        raise NotImplementedError

    def resellTicket(self) -> None:
        """Realizes UC30 "Resell Ticket" (R41)."""
        raise NotImplementedError

    def saveBankAccount(self) -> None:
        """Realizes UC31 "Save Bank Account" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R41, R42, R43, R44, R45"""
    name: _t.Optional[str] = None
    tickets: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None

    def resellTicket(self) -> None:
        """Realizes UC30 "Resell Ticket" (R41)."""
        raise NotImplementedError

    def uploadTicket(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class BankAccount:
    """Source: R45"""
    iban: _t.Optional[str] = None


@_dc.dataclass
class SearchEngine:
    """Source: R30, R31, R32, R33, R36, R37, R38, R39, R40"""
    caseInsensitive: _t.Optional[bool] = None
    punctuationSensitive: _t.Optional[bool] = None
    sortByDate: _t.Optional[bool] = None
    filterByPrice: _t.Optional[bool] = None
    filterByVenue: _t.Optional[bool] = None
    filterByGenre: _t.Optional[bool] = None


@_dc.dataclass
class Venue:
    """Source: R11, R28, R29, R30, R31, R32, R33, R46, R47, R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    map: _t.Optional[str] = None
