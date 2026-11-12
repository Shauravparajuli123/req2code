"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R51, R52, R53, R54, R55, R56, R58, R59"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscriptionEndDate: _t.Optional[str] = None
    previousInformation: _t.Optional[bool] = None
    isSubscribed: _t.Optional[bool] = None
    password: _t.Optional[str] = None
    personalDetails: _t.Optional[str] = None
    paymentDetails: _t.Optional[str] = None
    familyMembers: _t.Optional[str] = None
    familyMembership: _t.Optional[bool] = None
    availableLessons: _t.Optional[str] = None
    bookedLessons: _t.Optional[str] = None
    lessonHistory: _t.Optional[str] = None
    lessonBooked: _t.Optional[bool] = None
    lessonCanceled: _t.Optional[bool] = None
    notificationMethod: _t.Optional[str] = None
    preferredNotifications: _t.Optional[str] = None
    lessonCanceledNotification: _t.Optional[bool] = None
    checkInStatus: _t.Optional[bool] = None
    subscriptionStatus: _t.Optional[bool] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R1, R2, R3, R4, R5, R6, R7)."""
        raise NotImplementedError

    def managePersonalInformation(self) -> None:
        """Realizes UC2 "Manage Personal Information" (R10, R11, R12, R13, R14, R58, R59)."""
        raise NotImplementedError

    def bookLessons(self) -> None:
        """Realizes UC3 "Book Lessons" (R15, R16, R17, R23, R24, R50, R51, R52, R53, R54, R55, R56, R57)."""
        raise NotImplementedError

    def callGymToBookLesson(self) -> None:
        """Realizes UC4 "Call Gym To Book Lesson" (R21, R22)."""
        raise NotImplementedError

    def callGymToCancelLesson(self) -> None:
        """Operation."""
        raise NotImplementedError

    def bookPersonalTrainingSession(self) -> None:
        """Realizes UC5 "Book Personal Training Session" (R21, R22)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC6 "Cancel Lesson" (R39)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC8 "Edit Lesson" (R33, R34, R35, R36, R37)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC10 "View Schedule" (R32)."""
        raise NotImplementedError

    def checkIn(self) -> None:
        """Realizes UC16 "Customer Check In" (R61, R62)."""
        raise NotImplementedError

    def adminCheckIn(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R40, R49, R57, R60, R61"""
    name: _t.Optional[str] = None
    lessonSchedule: _t.Optional[str] = None
    lessonTime: _t.Optional[str] = None
    lessonDescription: _t.Optional[str] = None
    lessonRoom: _t.Optional[str] = None
    lessonType: _t.Optional[str] = None
    maxPeopleAllowed: _t.Optional[int] = None
    pastLessons: _t.Optional[str] = None
    canEditLessons: _t.Optional[bool] = None
    lessonTimeEdited: _t.Optional[str] = None
    lessonRoomEdited: _t.Optional[str] = None
    lessonDescriptionEdited: _t.Optional[str] = None
    lessonMaxPeopleEdited: _t.Optional[int] = None
    lessonCanceled: _t.Optional[bool] = None
    checkInStatus: _t.Optional[bool] = None

    def addLesson(self) -> None:
        """Realizes UC12 "Admin Add Trainer" (R47)."""
        raise NotImplementedError

    def editLesson(self) -> None:
        """Realizes UC9 "Admin Edit Lesson" (R38)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC11 "Admin View Schedule" (R32)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC7 "Admin Cancel Lesson" (R40)."""
        raise NotImplementedError

    def checkIn(self) -> None:
        """Realizes UC17 "Trainer Check In" (R60)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R20, R38, R40, R47, R48, R49, R53, R57, R60"""
    name: _t.Optional[str] = None
    canEditAnyLesson: _t.Optional[bool] = None
    lessonCanceled: _t.Optional[bool] = None
    checkInStatus: _t.Optional[bool] = None

    def editLesson(self) -> None:
        """Realizes UC9 "Admin Edit Lesson" (R38)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC7 "Admin Cancel Lesson" (R40)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC11 "Admin View Schedule" (R32)."""
        raise NotImplementedError

    def addTrainer(self) -> None:
        """Realizes UC12 "Admin Add Trainer" (R47)."""
        raise NotImplementedError

    def addAdmin(self) -> None:
        """Realizes UC13 "Admin Add Admin" (R48)."""
        raise NotImplementedError

    def removeTrainer(self) -> None:
        """Realizes UC14 "Admin Remove Trainer" (R49)."""
        raise NotImplementedError
