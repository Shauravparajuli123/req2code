"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R21, R22, R50, R51, R52, R53, R54, R55, R56, R58, R59"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscription: _t.Optional[str] = None
    familyMembers: _t.Optional[str] = None
    notifications: _t.Optional[str] = None
    checkInStatus: _t.Optional[bool] = None
    subscriptionStatus: _t.Optional[bool] = None

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

    def unsubscribe(self) -> None:
        """Realizes UC7 "Unsubscribe" (R8)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC8 "Reset Password" (R9)."""
        raise NotImplementedError

    def changeDetail(self) -> None:
        """Realizes UC9 "Change Detail" (R10)."""
        raise NotImplementedError

    def updatePaymentInformation(self) -> None:
        """Realizes UC10 "Update Payment Information" (R11)."""
        raise NotImplementedError

    def seeInformation(self) -> None:
        """Realizes UC13 "See Information" (R59, R60, R63)."""
        raise NotImplementedError

    def seeLesson(self) -> None:
        """Realizes UC14 "See Lesson" (R15, R16, R17)."""
        raise NotImplementedError

    def seeRoom(self) -> None:
        """Realizes UC15 "See Room" (R25)."""
        raise NotImplementedError

    def seeSchedule(self) -> None:
        """Realizes UC16 "See Schedule" (R32)."""
        raise NotImplementedError

    def callGym(self) -> None:
        """Realizes UC35 "Call Gym" (R18, R19, R21)."""
        raise NotImplementedError

    def bookSpot(self) -> None:
        """Realizes UC36 "Book Spot" (R23)."""
        raise NotImplementedError

    def seeSpot(self) -> None:
        """Realizes UC37 "See Spot" (R24)."""
        raise NotImplementedError

    def seeCustomer(self) -> None:
        """Realizes UC38 "See Customer" (R43, R62, R63)."""
        raise NotImplementedError

    def seeSubscription(self) -> None:
        """Realizes UC39 "See Subscription" (R6)."""
        raise NotImplementedError

    def seeNotification(self) -> None:
        """Realizes UC40 "See Notification" (R51, R52, R53, R54)."""
        raise NotImplementedError

    def confirmBooking(self) -> None:
        """Realizes UC42 "Confirm Booking" (R56)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""

    def cancelLesson(self) -> None:
        """Realizes UC29 "Cancel Lesson" (R39, R40)."""
        raise NotImplementedError

    def addTrainer(self) -> None:
        """Realizes UC31 "Add Trainer" (R47)."""
        raise NotImplementedError

    def addAdmin(self) -> None:
        """Realizes UC32 "Add Admin" (R48)."""
        raise NotImplementedError

    def removeTrainer(self) -> None:
        """Realizes UC33 "Remove Trainer" (R49)."""
        raise NotImplementedError

    def seeNoShow(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeNoShowCount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def issueFine(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37"""
    lessons: _t.Optional[str] = None

    def addLesson(self) -> None:
        """Realizes UC17 "Add Lesson" (R26)."""
        raise NotImplementedError

    def setTime(self) -> None:
        """Realizes UC20 "Set Time" (R27)."""
        raise NotImplementedError

    def setDescription(self) -> None:
        """Realizes UC18 "Set Description" (R28)."""
        raise NotImplementedError

    def setRoom(self) -> None:
        """Realizes UC19 "Set Room" (R29)."""
        raise NotImplementedError

    def setNumber(self) -> None:
        """Realizes UC21 "Set Number" (R31)."""
        raise NotImplementedError

    def setType(self) -> None:
        """Realizes UC22 "Set Type" (R30)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC23 "Edit Lesson" (R33, R38)."""
        raise NotImplementedError

    def editTime(self) -> None:
        """Realizes UC25 "Edit Time" (R34)."""
        raise NotImplementedError

    def editRoom(self) -> None:
        """Realizes UC26 "Edit Room" (R35)."""
        raise NotImplementedError

    def editNumber(self) -> None:
        """Realizes UC27 "Edit Number" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Lesson:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37"""
    description: _t.Optional[str] = None
    room: _t.Optional[str] = None
    type: _t.Optional[str] = None
    number: _t.Optional[int] = None
    time: _t.Optional[str] = None

    def editDescription(self) -> None:
        """Realizes UC24 "Edit Description" (R36)."""
        raise NotImplementedError

    def editTime(self) -> None:
        """Realizes UC25 "Edit Time" (R34)."""
        raise NotImplementedError

    def editRoom(self) -> None:
        """Realizes UC26 "Edit Room" (R35)."""
        raise NotImplementedError

    def editNumber(self) -> None:
        """Realizes UC27 "Edit Number" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R51, R52, R53, R54, R55, R56"""
    type: _t.Optional[str] = None
    method: _t.Optional[str] = None


@_dc.dataclass
class Person:
    """Source: R12, R13, R14"""
    pass


@_dc.dataclass
class Room:
    """Source: R25, R32"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R32"""
    pass


@_dc.dataclass
class TrainingSession:
    """Source: R38, R39, R40"""

    def editTrainingSession(self) -> None:
        """Realizes UC28 "Edit Training Session" (R20)."""
        raise NotImplementedError


@_dc.dataclass
class Spot:
    """Source: R23, R24"""
    pass
