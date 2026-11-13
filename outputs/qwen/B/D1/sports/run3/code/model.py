"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R57, R58, R59, R60, R61, R62, R63"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscription: _t.Optional[str] = None
    previousInformation: _t.Optional[str] = None
    password: _t.Optional[str] = None
    personalDetails: _t.Optional[str] = None
    paymentInformation: _t.Optional[str] = None
    familyMembership: _t.Optional[bool] = None
    lessons: _t.Optional[str] = None
    lessonBookings: _t.Optional[str] = None
    spotsBooked: _t.Optional[int] = None
    checkInMethod: _t.Optional[str] = None

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

    def changePersonalDetails(self) -> None:
        """Realizes UC10 "Change Personal Details" (R10)."""
        raise NotImplementedError

    def updatePaymentInformation(self) -> None:
        """Realizes UC11 "Update Payment Information" (R11)."""
        raise NotImplementedError

    def seeOverviewOfLessons(self) -> None:
        """Realizes UC12 "See Overview Of Lessons" (R15)."""
        raise NotImplementedError

    def seeFutureLessons(self) -> None:
        """Realizes UC13 "See Future Lessons" (R16)."""
        raise NotImplementedError

    def seeRecordOfPreviousLessons(self) -> None:
        """Realizes UC14 "See Record Of Previous Lessons" (R17)."""
        raise NotImplementedError

    def callGymToBookLesson(self) -> None:
        """Realizes UC15 "Call Gym To Book Lesson" (R18)."""
        raise NotImplementedError

    def callGymToCancelLesson(self) -> None:
        """Realizes UC16 "Call Gym To Cancel Lesson" (R19)."""
        raise NotImplementedError

    def bookSpotForFreePracticeArea(self) -> None:
        """Realizes UC17 "Book Spot For Free Practice Area" (R23)."""
        raise NotImplementedError

    def seeNumberOfSpotsBooked(self) -> None:
        """Realizes UC18 "See Number Of Spots Booked" (R24)."""
        raise NotImplementedError

    def seePersonalInformation(self) -> None:
        """Realizes UC48 "See Personal Information" (R58)."""
        raise NotImplementedError

    def seeMembershipInformation(self) -> None:
        """Realizes UC49 "See Membership Information" (R59)."""
        raise NotImplementedError

    def seePastAndFutureTrainingSessions(self) -> None:
        """Realizes UC50 "See Past And Future Training Sessions" (R60)."""
        raise NotImplementedError

    def checkIn(self) -> None:
        """Realizes UC51 "Have Check In Method" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R40, R42, R43, R44, R45, R46, R49, R52, R53, R54, R55, R56, R60"""
    name: _t.Optional[str] = None
    lessons: _t.Optional[str] = None
    lessonTime: _t.Optional[str] = None
    lessonDescription: _t.Optional[str] = None
    lessonRoom: _t.Optional[str] = None
    lessonType: _t.Optional[str] = None
    lessonNumber: _t.Optional[int] = None
    lessonSchedule: _t.Optional[str] = None
    lessonEditTime: _t.Optional[str] = None
    lessonEditRoom: _t.Optional[str] = None
    lessonEditDescription: _t.Optional[str] = None
    lessonEditNumber: _t.Optional[int] = None
    lessonEdit: _t.Optional[bool] = None
    lessonCancel: _t.Optional[bool] = None
    lessonNotification: _t.Optional[str] = None

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

    def setLessonNumber(self) -> None:
        """Realizes UC25 "Set Lesson Number" (R31)."""
        raise NotImplementedError

    def editLessonTime(self) -> None:
        """Realizes UC26 "Edit Lesson Time" (R34)."""
        raise NotImplementedError

    def editLessonRoom(self) -> None:
        """Realizes UC27 "Edit Lesson Room" (R35)."""
        raise NotImplementedError

    def editLessonDescription(self) -> None:
        """Realizes UC28 "Edit Lesson Description" (R36)."""
        raise NotImplementedError

    def editLessonNumber(self) -> None:
        """Realizes UC29 "Edit Lesson Number" (R37)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC30 "Edit Lesson" (R33)."""
        raise NotImplementedError

    def editAnyLesson(self) -> None:
        """Realizes UC31 "Edit Any Lesson" (R38)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC32 "Cancel Lesson" (R39, R40)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R20, R38, R47, R48, R49, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59, R62, R63"""
    name: _t.Optional[str] = None
    notifications: _t.Optional[str] = None
    subscriptions: _t.Optional[str] = None
    trainer: _t.Optional[str] = None
    lessonSchedule: _t.Optional[str] = None
    lessonEdit: _t.Optional[bool] = None
    lessonCancel: _t.Optional[bool] = None
    lessonNotification: _t.Optional[str] = None

    def editLesson(self) -> None:
        """Realizes UC31 "Edit Any Lesson" (R38)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC32 "Cancel Lesson" (R39, R40)."""
        raise NotImplementedError
