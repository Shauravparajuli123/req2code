"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R9, R10"""
    personalInformation: _t.Optional[str] = None
    paymentDetails: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    password: _t.Optional[str] = None
    ticketOrders: _t.Optional[str] = None
    favoritedArtistsAndEvents: _t.Optional[str] = None

    def createPersonalInformation(self) -> None:
        """Realizes UC1 "Save Personal Information" (R1)."""
        raise NotImplementedError

    def createPaymentDetails(self) -> None:
        """Realizes UC2 "Save Payment Details" (R2)."""
        raise NotImplementedError

    def fillOutSurvey(self) -> None:
        """Realizes UC3 "Fill Out Survey" (R3)."""
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

    def seeTicketOrders(self) -> None:
        """Realizes UC8 "See History Of Previous Ticket Orders" (R8)."""
        raise NotImplementedError


@_dc.dataclass
class Visitor:
    """Source: R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R33, R46, R47, R48"""
    eventInformation: _t.Optional[str] = None
    ticket: _t.Optional[str] = None
    paymentMethod: _t.Optional[str] = None
    searchResults: _t.Optional[str] = None
    user: _t.Optional["User"] = None

    def readEventInformation(self) -> None:
        """Realizes UC11 "Read About Event" (R11)."""
        raise NotImplementedError

    def buyTicket(self) -> None:
        """Realizes UC12 "Buy Tickets Directly From Event Page" (R12)."""
        raise NotImplementedError

    def resellTicket(self) -> None:
        """Realizes UC35 "Resell Tickets Directly From Event Page" (R41)."""
        raise NotImplementedError

    def buyTicketAsGuest(self) -> None:
        """Realizes UC14 "Buy Ticket As Guest" (R14)."""
        raise NotImplementedError

    def fillInNameAndEmail(self) -> None:
        """Realizes UC15 "Fill In Name And Email When Buying A Ticket" (R15)."""
        raise NotImplementedError

    def purchaseTicket(self) -> None:
        """Realizes UC17 "Purchase A Ticket" (R19)."""
        raise NotImplementedError

    def buyMultipleTickets(self) -> None:
        """Realizes UC18 "Buy Multiple Tickets In One Purchase" (R20)."""
        raise NotImplementedError

    def seeAvailableSeats(self) -> None:
        """Realizes UC19 "See Available Seats" (R21)."""
        raise NotImplementedError

    def seeSeatsInMap(self) -> None:
        """Realizes UC20 "See Seats In Map" (R22)."""
        raise NotImplementedError

    def seeTypesOfTickets(self) -> None:
        """Realizes UC21 "See Types Of Tickets" (R23)."""
        raise NotImplementedError

    def addTicketsToCart(self) -> None:
        """Realizes UC22 "Add Tickets To Cart" (R24)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC23 "See Order Summary" (R25)."""
        raise NotImplementedError

    def seeListOfPaymentMethods(self) -> None:
        """Realizes UC24 "See List Of Payment Methods" (R26)."""
        raise NotImplementedError

    def clickOnSearchResult(self) -> None:
        """Realizes UC26 "Click On Search Result" (R29)."""
        raise NotImplementedError

    def sortSearchResultsByDate(self) -> None:
        """Realizes UC27 "Sort Search Results By Date" (R31)."""
        raise NotImplementedError

    def filterSearchResultsByPrice(self) -> None:
        """Realizes UC28 "Filter Search Results By Price" (R32)."""
        raise NotImplementedError

    def filterSearchResultsByVenue(self) -> None:
        """Realizes UC29 "Filter Search Results By Venue" (R33)."""
        raise NotImplementedError

    def filterSearchResultsByGenre(self) -> None:
        """Realizes UC30 "Filter Search Results By Genre" (R34)."""
        raise NotImplementedError

    def seeUpcomingEventsInCalendarView(self) -> None:
        """Realizes UC40 "See Upcoming Events In Calendar View" (R46)."""
        raise NotImplementedError

    def seePopularUpcomingEvents(self) -> None:
        """Realizes UC41 "See Popular Upcoming Events" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R11, R12, R13, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45"""
    ticket: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None
    user: _t.Optional["User"] = None

    def sellTicket(self) -> None:
        """Realizes UC13 "Sell Tickets Directly From Event Page" (R13)."""
        raise NotImplementedError

    def uploadDigitalTicket(self) -> None:
        """Realizes UC36 "Upload Digital Ticket" (R42)."""
        raise NotImplementedError

    def setPriceForTicket(self) -> None:
        """Realizes UC37 "Set Price For Ticket" (R43)."""
        raise NotImplementedError

    def addDescriptionOfEvent(self) -> None:
        """Realizes UC38 "Add Description Of Event" (R44)."""
        raise NotImplementedError

    def saveBankAccount(self) -> None:
        """Realizes UC39 "Save Bank Account" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R35, R36, R37, R38, R39, R40"""
    serviceFee: _t.Optional[str] = None
    fraudulentBehavior: _t.Optional[str] = None
    protectUsersFromOnlineFraud: _t.Optional[str] = None
    user: _t.Optional["User"] = None
    reseller: _t.Optional["Reseller"] = None

    def validateTickets(self) -> None:
        """Realizes UC31 "Validate Tickets" (R37)."""
        raise NotImplementedError

    def deductServiceFee(self) -> None:
        """Realizes UC32 "Deduct Service Fee" (R38)."""
        raise NotImplementedError

    def avoidFraudulentBehavior(self) -> None:
        """Realizes UC33 "Avoid Fraudulent Behavior" (R39)."""
        raise NotImplementedError

    def protectUsers(self) -> None:
        """Realizes UC34 "Protect Users From Online Fraud" (R40)."""
        raise NotImplementedError
