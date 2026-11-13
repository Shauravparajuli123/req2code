"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R5, R6, R7, R8, R9, R10, R15, R16, R17, R18, R25, R26, R35, R36, R37, R38, R39, R40, R45, R53"""
    personalInformation: _t.Optional[str] = None
    paymentDetails: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    password: _t.Optional[str] = None
    ticketOrders: _t.Optional[str] = None
    favoriteEventsArtists: _t.Optional[str] = None

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

    def seeTicketOrders(self) -> None:
        """Realizes UC8 "See History Of Previous Ticket Orders" (R8)."""
        raise NotImplementedError

    def seeFavoriteEventsArtists(self) -> None:
        """Realizes UC10 "Find List Of Favorited Artists And Events" (R10)."""
        raise NotImplementedError


@_dc.dataclass
class Visitor:
    """Source: R11, R12, R13, R14, R18, R19, R20, R21, R22, R23, R24, R25, R26, R28, R29, R30, R31, R32, R33, R46, R47, R48"""

    def readAboutEvent(self) -> None:
        """Realizes UC11 "Read About Event" (R11)."""
        raise NotImplementedError

    def buyTicketsDirectly(self) -> None:
        """Realizes UC12 "Buy Tickets Directly From Event Page" (R12)."""
        raise NotImplementedError

    def resellTicketsDirectly(self) -> None:
        """Realizes UC29 "Resell Tickets Directly From Event Page" (R41)."""
        raise NotImplementedError

    def seeAvailableSeats(self) -> None:
        """Realizes UC16 "See Available Seats" (R21)."""
        raise NotImplementedError

    def seeAvailableSeatsMap(self) -> None:
        """Realizes UC17 "See Available Seats In Map" (R22)."""
        raise NotImplementedError

    def seeTypesOfTickets(self) -> None:
        """Realizes UC18 "See Types Of Tickets" (R23)."""
        raise NotImplementedError

    def addTicketsToShoppingCart(self) -> None:
        """Realizes UC19 "Add Tickets To Shopping Cart" (R24)."""
        raise NotImplementedError

    def seeOrderSummary(self) -> None:
        """Realizes UC20 "See Order Summary" (R25)."""
        raise NotImplementedError

    def seeListPaymentMethods(self) -> None:
        """Realizes UC21 "See List Of Payment Methods" (R26)."""
        raise NotImplementedError

    def seeUpcomingEventsCalendar(self) -> None:
        """Realizes UC34 "See Upcoming Events In Calendar View" (R46)."""
        raise NotImplementedError

    def seePopularUpcomingEvents(self) -> None:
        """Realizes UC35 "See Popular Upcoming Events" (R47)."""
        raise NotImplementedError

    def clickOnEventHomepage(self) -> None:
        """Realizes UC36 "Click On Event On Homepage To Be Directed To Event Page" (R48)."""
        raise NotImplementedError


@_dc.dataclass
class Reseller:
    """Source: R11, R12, R13, R11, R12, R13, R21, R22, R23, R24, R25, R26, R41, R42, R43, R44, R45"""

    def uploadDigitalTicket(self) -> None:
        """Realizes UC30 "Upload Digital Ticket From Local Device" (R42)."""
        raise NotImplementedError

    def setAnyPriceAbove5Cents(self) -> None:
        """Realizes UC31 "Set Any Price Above 5 Cents" (R43)."""
        raise NotImplementedError

    def addShortDescriptionEvent(self) -> None:
        """Realizes UC32 "Add Short Description Of Event" (R44)."""
        raise NotImplementedError

    def saveBankAccount(self) -> None:
        """Realizes UC33 "Save Bank Account In User Profile" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Company:
    """Source: R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40"""

    def haveIntuitiveBuyingProcess(self) -> None:
        """Realizes UC22 "Have Overall Buying Process As Intuitive And Quick" (R27)."""
        raise NotImplementedError

    def haveMinimumPriceReselling(self) -> None:
        """Realizes UC23 "Set Minimum Price For Reselling Ticket" (R35)."""
        raise NotImplementedError

    def sellOnlyDigitalTickets(self) -> None:
        """Realizes UC24 "Sell Only Digital Tickets" (R36)."""
        raise NotImplementedError

    def validateTickets(self) -> None:
        """Realizes UC25 "Validate Tickets" (R37)."""
        raise NotImplementedError

    def deductServiceFee(self) -> None:
        """Realizes UC26 "Deduct Service Fee From Total Price" (R38)."""
        raise NotImplementedError

    def avoidFraudulentBehavior(self) -> None:
        """Realizes UC27 "Avoid Fraudulent Behavior" (R39)."""
        raise NotImplementedError

    def protectUsersFromOnlineFraud(self) -> None:
        """Realizes UC28 "Protect Users From Online Fraud" (R40)."""
        raise NotImplementedError
