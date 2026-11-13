"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R21, R22, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscriptionDuration: _t.Optional[int] = None
    previousInformation: _t.Optional[str] = None
    password: _t.Optional[str] = None
    personalDetails: _t.Optional[str] = None
    paymentInformation: _t.Optional[str] = None
    familyMembers: _t.Optional[str] = None
    bookedLessons: _t.Optional[str] = None
    checkInStatus: _t.Optional[bool] = None
    notificationMethod: _t.Optional[str] = None

    def openAccount(self) -> None:
        """Realizes UC1 "Open Account" (R1)."""
        raise NotImplementedError

    def addPersonalInformation(self) -> None:
        """Realizes UC2 "Add Personal Information" (R2)."""
        raise NotImplementedError

    def addBankingDetails(self) -> None:
        """Realizes UC3 "Add Banking Details" (R3)."""
        raise NotImplementedError

    def chooseMembershipType(self) -> None:
        """Realizes UC4 "Choose Membership Type" (R4)."""
        raise NotImplementedError

    def extendSubscription(self) -> None:
        """Realizes UC5 "Extend Subscription" (R5)."""
        raise NotImplementedError

    def knowSubscriptionDuration(self) -> None:
        """Realizes UC6 "Know Subscription Duration" (R6)."""
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

    def changePersonalDetails(self) -> None:
        """Realizes UC10 "Change Personal Details" (R10)."""
        raise NotImplementedError

    def updatePaymentInformation(self) -> None:
        """Realizes UC11 "Update Payment Information" (R11)."""
        raise NotImplementedError

    def addPersonToMembership(self) -> None:
        """Realizes UC13 "Add Person To Membership" (R13)."""
        raise NotImplementedError

    def removePersonFromMembership(self) -> None:
        """Realizes UC14 "Remove Person From Membership" (R14)."""
        raise NotImplementedError

    def seeAvailableLessons(self) -> None:
        """Realizes UC15 "See Available Lessons" (R15)."""
        raise NotImplementedError

    def seeBookedLessons(self) -> None:
        """Realizes UC16 "See Booked Lessons" (R16)."""
        raise NotImplementedError

    def seePastLessons(self) -> None:
        """Realizes UC17 "See Past Lessons" (R17)."""
        raise NotImplementedError

    def callToBookLesson(self) -> None:
        """Realizes UC18 "Call To Book Lesson" (R18)."""
        raise NotImplementedError

    def callToCancelLesson(self) -> None:
        """Realizes UC19 "Call To Cancel Lesson" (R19)."""
        raise NotImplementedError

    def seeCustomerSubscriptions(self) -> None:
        """Realizes UC49 "See Customer Subscriptions" (R57)."""
        raise NotImplementedError

    def seeCustomerCheckIn(self) -> None:
        """Realizes UC50 "See Customer Check In" (R62)."""
        raise NotImplementedError

    def seeCustomerBookings(self) -> None:
        """Realizes UC51 "See Customer Bookings" (R63)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R47, R48, R49, R57"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None
    customers: _t.List["Customer"] = _dc.field(default_factory=list)
    lessons: _t.List["Lesson"] = _dc.field(default_factory=list)
    trainers: _t.List["Trainer"] = _dc.field(default_factory=list)

    def addTrainer(self) -> None:
        """Realizes UC39 "Add Trainer" (R47)."""
        raise NotImplementedError

    def addAdmin(self) -> None:
        """Realizes UC40 "Add Admin" (R48)."""
        raise NotImplementedError

    def removeTrainer(self) -> None:
        """Realizes UC41 "Remove Trainer" (R49)."""
        raise NotImplementedError

    def seeNoShows(self) -> None:
        """Realizes UC35 "See No Shows" (R43)."""
        raise NotImplementedError

    def seeNoShowCount(self) -> None:
        """Realizes UC36 "See No Show Count" (R44)."""
        raise NotImplementedError

    def issueFine(self) -> None:
        """Realizes UC37 "Issue Fine For No Show" (R45)."""
        raise NotImplementedError

    def increaseFine(self) -> None:
        """Realizes UC38 "Increase Fine For Repeat No Show" (R46)."""
        raise NotImplementedError

    def seeCustomerSubscriptions(self) -> None:
        """Realizes UC49 "See Customer Subscriptions" (R57)."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R20, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None
    lessons: _t.Optional[str] = None
    lesson: _t.Optional["Lesson"] = None
    admin: _t.Optional["Admin"] = None

    def addLesson(self) -> None:
        """Realizes UC20 "Add Lesson" (R26)."""
        raise NotImplementedError

    def setLessonTime(self) -> None:
        """Realizes UC21 "Set Lesson Time" (R27)."""
        raise NotImplementedError

    def setLessonDescription(self) -> None:
        """Realizes UC22 "Set Lesson Description" (R28)."""
        raise NotImplementedError

    def setLessonRoom(self) -> None:
        """Realizes UC23 "Set Lesson Room" (R29)."""
        raise NotImplementedError

    def setLessonType(self) -> None:
        """Realizes UC24 "Set Lesson Type" (R30)."""
        raise NotImplementedError

    def setLessonMaxPeople(self) -> None:
        """Realizes UC25 "Set Lesson Max People" (R31)."""
        raise NotImplementedError

    def seeSchedule(self) -> None:
        """Realizes UC26 "See Schedule" (R32)."""
        raise NotImplementedError

    def editLessonTime(self) -> None:
        """Realizes UC27 "Edit Lesson Time" (R34)."""
        raise NotImplementedError

    def changeLessonRoom(self) -> None:
        """Realizes UC28 "Change Lesson Room" (R35)."""
        raise NotImplementedError

    def editLessonDescription(self) -> None:
        """Realizes UC29 "Edit Lesson Description" (R36)."""
        raise NotImplementedError

    def editLessonMaxPeople(self) -> None:
        """Realizes UC30 "Edit Lesson Max People" (R37)."""
        raise NotImplementedError

    def editAnyLesson(self) -> None:
        """Realizes UC31 "Edit Any Lesson" (R38)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC32 "Cancel Lesson" (R39, R40)."""
        raise NotImplementedError


@_dc.dataclass
class Lesson:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40"""
    time: _t.Optional[str] = None
    description: _t.Optional[str] = None
    room: _t.Optional[str] = None
    type: _t.Optional[str] = None
    maxPeople: _t.Optional[int] = None
    trainer: _t.Optional[str] = None

    def setTime(self) -> None:
        """Realizes UC21 "Set Lesson Time" (R27)."""
        raise NotImplementedError

    def setDescription(self) -> None:
        """Realizes UC22 "Set Lesson Description" (R28)."""
        raise NotImplementedError

    def setRoom(self) -> None:
        """Realizes UC23 "Set Lesson Room" (R29)."""
        raise NotImplementedError

    def setType(self) -> None:
        """Realizes UC24 "Set Lesson Type" (R30)."""
        raise NotImplementedError

    def setMaxPeople(self) -> None:
        """Realizes UC25 "Set Lesson Max People" (R31)."""
        raise NotImplementedError
