"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59, R60, R61, R62, R63"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscription: _t.Optional[str] = None
    previousInformation: _t.Optional[str] = None
    familyMembership: _t.Optional[bool] = None
    notificationMethod: _t.Optional[str] = None
    checkInStatus: _t.Optional[bool] = None
    lesson: _t.Optional["Lesson"] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R1)."""
        raise NotImplementedError

    def addPersonalInformation(self) -> None:
        """Realizes UC2 "Add Personal Information" (R2)."""
        raise NotImplementedError

    def addBankingDetail(self) -> None:
        """Realizes UC3 "Add Banking Detail" (R3)."""
        raise NotImplementedError

    def chooseMembershipType(self) -> None:
        """Realizes UC4 "Choose Membership Type" (R4)."""
        raise NotImplementedError

    def extendSubscription(self) -> None:
        """Realizes UC5 "Extend Subscription" (R5)."""
        raise NotImplementedError

    def knowSubscription(self) -> None:
        """Realizes UC6 "Know Subscription" (R6)."""
        raise NotImplementedError

    def usePreviousInformation(self) -> None:
        """Realizes UC7 "Use Previous Information" (R7)."""
        raise NotImplementedError

    def unsubscribe(self) -> None:
        """Realizes UC8 "Unsubscribe" (R8)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC9 "Reset Password" (R9)."""
        raise NotImplementedError

    def changeDetail(self) -> None:
        """Realizes UC10 "Change Detail" (R10)."""
        raise NotImplementedError

    def updatePaymentInformation(self) -> None:
        """Realizes UC11 "Update Payment Information" (R11)."""
        raise NotImplementedError

    def seeOverview(self) -> None:
        """Realizes UC14 "See Overview" (R15)."""
        raise NotImplementedError

    def seeRecord(self) -> None:
        """Realizes UC15 "See Record" (R17)."""
        raise NotImplementedError

    def seeFutureLessons(self) -> None:
        """Realizes UC16 "See Future Lessons" (R16)."""
        raise NotImplementedError

    def callGym(self) -> None:
        """Realizes UC17 "Call Gym" (R18, R19, R21)."""
        raise NotImplementedError

    def bookSpot(self) -> None:
        """Realizes UC18 "Book Spot" (R23)."""
        raise NotImplementedError

    def seeAvailableSpots(self) -> None:
        """Realizes UC19 "See Available Spots" (R24)."""
        raise NotImplementedError

    def seeRoom(self) -> None:
        """Realizes UC20 "See Room" (R25)."""
        raise NotImplementedError

    def seeMembership(self) -> None:
        """Realizes UC42 "See Membership" (R12)."""
        raise NotImplementedError

    def seeInformation(self) -> None:
        """Realizes UC43 "See Information" (R59, R60)."""
        raise NotImplementedError

    def seeNotification(self) -> None:
        """Realizes UC44 "See Notification" (R51, R52, R53, R54)."""
        raise NotImplementedError

    def confirmBooking(self) -> None:
        """Realizes UC45 "Confirm Booking" (R56)."""
        raise NotImplementedError

    def notifySession(self) -> None:
        """Realizes UC46 "Notify Session" (R42)."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37"""
    name: _t.Optional[str] = None
    lesson: _t.Optional[str] = None

    def addLesson(self) -> None:
        """Realizes UC21 "Add Lesson" (R26)."""
        raise NotImplementedError

    def setTime(self) -> None:
        """Realizes UC22 "Set Time" (R27)."""
        raise NotImplementedError

    def setDescription(self) -> None:
        """Realizes UC23 "Set Description" (R28)."""
        raise NotImplementedError

    def setRoom(self) -> None:
        """Realizes UC24 "Set Room" (R29)."""
        raise NotImplementedError

    def setNumber(self) -> None:
        """Realizes UC25 "Set Number" (R31)."""
        raise NotImplementedError

    def setType(self) -> None:
        """Realizes UC26 "Set Type" (R30)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC27 "Edit Lesson" (R33, R38)."""
        raise NotImplementedError

    def editTime(self) -> None:
        """Realizes UC28 "Edit Time" (R34)."""
        raise NotImplementedError

    def editRoom(self) -> None:
        """Realizes UC29 "Edit Room" (R35)."""
        raise NotImplementedError

    def editDescription(self) -> None:
        """Realizes UC30 "Edit Description" (R36)."""
        raise NotImplementedError

    def editNumber(self) -> None:
        """Realizes UC31 "Edit Number" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    name: _t.Optional[str] = None
    trainer: _t.Optional["Trainer"] = None
    customer: _t.Optional["Customer"] = None

    def editLesson(self) -> None:
        """Realizes UC27 "Edit Lesson" (R33, R38)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC33 "Cancel Lesson" (R39, R40)."""
        raise NotImplementedError

    def seeCustomer(self) -> None:
        """Realizes UC34 "See Customer" (R43, R62, R63)."""
        raise NotImplementedError

    def seeSubscription(self) -> None:
        """Realizes UC35 "See Subscription" (R44)."""
        raise NotImplementedError

    def haveFine(self) -> None:
        """Realizes UC36 "Have Fine" (R45, R46)."""
        raise NotImplementedError

    def addAdmin(self) -> None:
        """Realizes UC37 "Add Admin" (R48)."""
        raise NotImplementedError

    def addTrainer(self) -> None:
        """Realizes UC38 "Add Trainer" (R47)."""
        raise NotImplementedError

    def removeTrainer(self) -> None:
        """Realizes UC39 "Remove Trainer" (R49)."""
        raise NotImplementedError


@_dc.dataclass
class Lesson:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37"""
    name: _t.Optional[str] = None
    time: _t.Optional[str] = None
    description: _t.Optional[str] = None
    room: _t.Optional[str] = None
    number: _t.Optional[int] = None
    type: _t.Optional[str] = None
    record_: _t.Optional[str] = None

    def addLesson(self) -> None:
        """Realizes UC21 "Add Lesson" (R26)."""
        raise NotImplementedError

    def setTime(self) -> None:
        """Realizes UC22 "Set Time" (R27)."""
        raise NotImplementedError

    def setDescription(self) -> None:
        """Realizes UC23 "Set Description" (R28)."""
        raise NotImplementedError

    def setRoom(self) -> None:
        """Realizes UC24 "Set Room" (R29)."""
        raise NotImplementedError

    def setNumber(self) -> None:
        """Realizes UC25 "Set Number" (R31)."""
        raise NotImplementedError

    def setType(self) -> None:
        """Realizes UC26 "Set Type" (R30)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC27 "Edit Lesson" (R33, R38)."""
        raise NotImplementedError

    def editTime(self) -> None:
        """Realizes UC28 "Edit Time" (R34)."""
        raise NotImplementedError

    def editRoom(self) -> None:
        """Realizes UC29 "Edit Room" (R35)."""
        raise NotImplementedError

    def editDescription(self) -> None:
        """Realizes UC30 "Edit Description" (R36)."""
        raise NotImplementedError

    def editNumber(self) -> None:
        """Realizes UC31 "Edit Number" (R37)."""
        raise NotImplementedError
