"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R21, R22, R23, R50, R51, R52, R53, R54, R55, R56, R58, R59, R61, R62, R63"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscriptionDuration: _t.Optional[int] = None
    familyMembers: _t.Optional[str] = None
    pastLessons: _t.Optional[str] = None
    futureLessons: _t.Optional[str] = None
    personalInformationUpdated: _t.Optional[bool] = None
    paymentInformationUpdated: _t.Optional[bool] = None
    checkInStatus: _t.Optional[bool] = None
    notificationMethod: _t.Optional["NotificationMethod"] = None
    notification: _t.Optional["Notification"] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R1)."""
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

    def unsubscribe(self) -> None:
        """Realizes UC7 "Unsubscribe" (R8)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC8 "Reset Password" (R9)."""
        raise NotImplementedError

    def changePersonalDetails(self) -> None:
        """Realizes UC9 "Change Personal Details" (R10)."""
        raise NotImplementedError

    def updatePaymentInformation(self) -> None:
        """Realizes UC10 "Update Payment Information" (R11)."""
        raise NotImplementedError

    def addPersonToFamilyMembership(self) -> None:
        """Realizes UC12 "Add Person To Family Membership" (R13)."""
        raise NotImplementedError

    def removePersonFromFamilyMembership(self) -> None:
        """Realizes UC13 "Remove Person From Family Membership" (R14)."""
        raise NotImplementedError

    def seeAvailableLessons(self) -> None:
        """Realizes UC14 "See Available Lessons" (R15)."""
        raise NotImplementedError

    def seeFutureLessons(self) -> None:
        """Realizes UC15 "See Future Lessons" (R16)."""
        raise NotImplementedError

    def seePastLessons(self) -> None:
        """Realizes UC16 "See Past Lessons" (R17)."""
        raise NotImplementedError

    def callGymToBookLesson(self) -> None:
        """Realizes UC17 "Call Gym To Book Lesson" (R21)."""
        raise NotImplementedError

    def callGymToCancelLesson(self) -> None:
        """Realizes UC18 "Call Gym To Cancel Lesson" (R22)."""
        raise NotImplementedError

    def bookSpotForFreePracticeArea(self) -> None:
        """Realizes UC19 "Book Spot For Free Practice Area" (R23)."""
        raise NotImplementedError

    def seeBookedSpots(self) -> None:
        """Realizes UC20 "See Booked Spots" (R24)."""
        raise NotImplementedError

    def seeFreeRooms(self) -> None:
        """Realizes UC21 "See Free Rooms" (R25)."""
        raise NotImplementedError

    def seePersonalInformation(self) -> None:
        """Realizes UC51 "See Personal Information" (R58)."""
        raise NotImplementedError

    def seeMembershipInformation(self) -> None:
        """Realizes UC52 "See Membership Information" (R59)."""
        raise NotImplementedError

    def seePastAndFutureTrainingSessions(self) -> None:
        """Realizes UC53 "See Past And Future Training Sessions" (R60)."""
        raise NotImplementedError

    def checkIn(self) -> None:
        """Realizes UC54 "Check In" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37"""
    name: _t.Optional[str] = None
    lessonSchedule: _t.Optional[str] = None

    def addLessonToSchedule(self) -> None:
        """Realizes UC22 "Add Lesson To Schedule" (R26)."""
        raise NotImplementedError

    def setLessonTime(self) -> None:
        """Realizes UC23 "Set Lesson Time" (R27)."""
        raise NotImplementedError

    def setLessonDescription(self) -> None:
        """Realizes UC24 "Set Lesson Description" (R28)."""
        raise NotImplementedError

    def setLessonRoom(self) -> None:
        """Realizes UC25 "Set Lesson Room" (R29)."""
        raise NotImplementedError

    def setLessonType(self) -> None:
        """Realizes UC26 "Set Lesson Type" (R30)."""
        raise NotImplementedError

    def setLessonCapacity(self) -> None:
        """Realizes UC27 "Set Lesson Capacity" (R31)."""
        raise NotImplementedError

    def editOwnLessonTime(self) -> None:
        """Realizes UC29 "Edit Own Lesson Time" (R34)."""
        raise NotImplementedError

    def editOwnLessonRoom(self) -> None:
        """Realizes UC30 "Edit Own Lesson Room" (R35)."""
        raise NotImplementedError

    def editOwnLessonDescription(self) -> None:
        """Realizes UC31 "Edit Own Lesson Description" (R36)."""
        raise NotImplementedError

    def editOwnLessonCapacity(self) -> None:
        """Realizes UC32 "Edit Own Lesson Capacity" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""

    def cancelLesson(self) -> None:
        """Realizes UC34 "Cancel Lesson" (R40)."""
        raise NotImplementedError

    def seeNoShow(self) -> None:
        """Realizes UC37 "Admin See No Show" (R43)."""
        raise NotImplementedError

    def seeNoShowCount(self) -> None:
        """Realizes UC38 "Admin See No Show Count" (R44)."""
        raise NotImplementedError

    def issueFine(self) -> None:
        """Realizes UC39 "Admin Issue Fine" (R45)."""
        raise NotImplementedError

    def issueFineExponentially(self) -> None:
        """Realizes UC40 "Admin Issue Fine Exponentially" (R46)."""
        raise NotImplementedError

    def addTrainer(self) -> None:
        """Realizes UC41 "Admin Add Trainer" (R47)."""
        raise NotImplementedError

    def addAdmin(self) -> None:
        """Realizes UC42 "Admin Add Admin" (R48)."""
        raise NotImplementedError

    def removeTrainer(self) -> None:
        """Realizes UC43 "Admin Remove Trainer" (R49)."""
        raise NotImplementedError


class NotificationMethod(_enum.Enum):
    """Source: R51, R52, R53"""
    EMAIL = "EMAIL"
    PUSH = "PUSH"


@_dc.dataclass
class Notification:
    """Source: R55, R56, R57"""
    method: _t.Optional[str] = None
    confirmed: _t.Optional[bool] = None

    def receiveNotification(self) -> None:
        """Operation."""
        raise NotImplementedError
