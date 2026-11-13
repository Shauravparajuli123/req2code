"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R21, R22, R23, R24, R50, R51, R52, R53, R54, R55, R56, R58, R59"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscription: _t.Optional[str] = None
    familyMembers: _t.Optional[str] = None
    lessonsBooked: _t.Optional[str] = None
    preferredNotificationMethod: _t.Optional[str] = None
    checkInStatus: _t.Optional[bool] = None
    lesson: _t.Optional["Lesson"] = None
    notification: _t.Optional["Notification"] = None

    def openAccount(self) -> None:
        """Realizes UC1 "Open Account" (R1)."""
        raise NotImplementedError

    def addInformation(self) -> None:
        """Realizes UC2 "Add Information" (R2)."""
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

    def seeInformation(self) -> None:
        """Realizes UC6 "See Information" (R6)."""
        raise NotImplementedError

    def useInformation(self) -> None:
        """Realizes UC7 "Use Information" (R7)."""
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

    def seeMembership(self) -> None:
        """Realizes UC14 "See Membership" (R12)."""
        raise NotImplementedError

    def seeLesson(self) -> None:
        """Realizes UC15 "See Lesson" (R15)."""
        raise NotImplementedError

    def seeRecord(self) -> None:
        """Realizes UC16 "See Record" (R17)."""
        raise NotImplementedError

    def callGym(self) -> None:
        """Realizes UC40 "Call Gym" (R18, R19, R21)."""
        raise NotImplementedError

    def bookSpot(self) -> None:
        """Realizes UC41 "Book Spot" (R23)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC42 "Receive Notification" (R41, R51, R52, R53, R54, R56)."""
        raise NotImplementedError

    def receivePushNotification(self) -> None:
        """Realizes UC43 "Receive Push Notification" (R53)."""
        raise NotImplementedError

    def confirmBooking(self) -> None:
        """Realizes UC44 "Confirm Booking" (R56)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    lesson: _t.Optional["Lesson"] = None
    customer: _t.Optional["Customer"] = None

    def editLesson(self) -> None:
        """Realizes UC25 "Edit Lesson" (R33, R38)."""
        raise NotImplementedError

    def editTrainingSession(self) -> None:
        """Realizes UC31 "Edit Training Session" (R20)."""
        raise NotImplementedError

    def haveMethod(self) -> None:
        """Realizes UC32 "Have Method" (R61)."""
        raise NotImplementedError

    def haveSystem(self) -> None:
        """Realizes UC33 "Have System" (R45)."""
        raise NotImplementedError

    def haveFine(self) -> None:
        """Realizes UC34 "Have Fine" (R46)."""
        raise NotImplementedError

    def seeSchedule(self) -> None:
        """Realizes UC35 "See Schedule" (R32)."""
        raise NotImplementedError

    def seeCustomer(self) -> None:
        """Realizes UC36 "See Customer" (R43, R62, R63)."""
        raise NotImplementedError

    def knowCustomer(self) -> None:
        """Realizes UC37 "Know Customer" (R57)."""
        raise NotImplementedError

    def knowSubscription(self) -> None:
        """Realizes UC38 "Know Subscription" (R44)."""
        raise NotImplementedError

    def notifySession(self) -> None:
        """Realizes UC39 "Notify Session" (R42)."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39"""
    name: _t.Optional[str] = None
    lessons: _t.Optional[str] = None

    def addLesson(self) -> None:
        """Realizes UC19 "Add Lesson" (R26)."""
        raise NotImplementedError

    def setTime(self) -> None:
        """Realizes UC22 "Set Time" (R27)."""
        raise NotImplementedError

    def setDescription(self) -> None:
        """Realizes UC20 "Set Description" (R28)."""
        raise NotImplementedError

    def setRoom(self) -> None:
        """Realizes UC21 "Set Room" (R29)."""
        raise NotImplementedError

    def setNumber(self) -> None:
        """Realizes UC23 "Set Number" (R31)."""
        raise NotImplementedError

    def setType(self) -> None:
        """Realizes UC24 "Set Type" (R30)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC25 "Edit Lesson" (R33, R38)."""
        raise NotImplementedError


@_dc.dataclass
class Lesson:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39"""
    description: _t.Optional[str] = None
    room: _t.Optional[str] = None
    time: _t.Optional[str] = None
    number: _t.Optional[int] = None
    type: _t.Optional[str] = None

    def addLesson(self) -> None:
        """Realizes UC19 "Add Lesson" (R26)."""
        raise NotImplementedError

    def setTime(self) -> None:
        """Realizes UC22 "Set Time" (R27)."""
        raise NotImplementedError

    def setDescription(self) -> None:
        """Realizes UC20 "Set Description" (R28)."""
        raise NotImplementedError

    def setRoom(self) -> None:
        """Realizes UC21 "Set Room" (R29)."""
        raise NotImplementedError

    def setNumber(self) -> None:
        """Realizes UC23 "Set Number" (R31)."""
        raise NotImplementedError

    def setType(self) -> None:
        """Realizes UC24 "Set Type" (R30)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC25 "Edit Lesson" (R33, R38)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R51, R52, R53, R54, R55, R56"""
    method: _t.Optional[str] = None
    message: _t.Optional[str] = None
