"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    subscription: _t.Optional[str] = None
    familyMembers: _t.Optional[str] = None
    notifications: _t.Optional[str] = None
    membership: _t.Optional["Membership"] = None

    def createAccount(self) -> None:
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

    def seeFamilyMembers(self) -> None:
        """Realizes UC12 "See Family Members" (R12)."""
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

    def seeFutureLessons(self) -> None:
        """Realizes UC16 "See Future Lessons" (R16)."""
        raise NotImplementedError

    def seePastLessons(self) -> None:
        """Realizes UC17 "See Past Lessons" (R17)."""
        raise NotImplementedError

    def callToBookLesson(self) -> None:
        """Realizes UC18 "Call To Book Lesson" (R18, R21)."""
        raise NotImplementedError

    def callToCancelLesson(self) -> None:
        """Realizes UC19 "Call To Cancel Lesson" (R19, R22)."""
        raise NotImplementedError

    def bookFreePracticeArea(self) -> None:
        """Realizes UC20 "Book Free Practice Area" (R23)."""
        raise NotImplementedError

    def seeBookedSpots(self) -> None:
        """Realizes UC21 "See Booked Spots" (R24)."""
        raise NotImplementedError

    def seeFreeRooms(self) -> None:
        """Realizes UC22 "See Free Rooms" (R25)."""
        raise NotImplementedError

    def logIn(self) -> None:
        """Realizes UC45 "Log In" (R50)."""
        raise NotImplementedError

    def chooseNotificationMethod(self) -> None:
        """Realizes UC46 "Choose Notification Method" (R51)."""
        raise NotImplementedError

    def receiveEmailNotifications(self) -> None:
        """Realizes UC47 "Receive Email Notifications" (R52)."""
        raise NotImplementedError

    def receivePushNotifications(self) -> None:
        """Realizes UC48 "Receive Push Notifications" (R53)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC49 "Choose Notifications" (R54)."""
        raise NotImplementedError

    def receiveCanceledLessonNotification(self) -> None:
        """Realizes UC50 "Receive Canceled Lesson Notification" (R55)."""
        raise NotImplementedError

    def confirmCanceledLesson(self) -> None:
        """Realizes UC51 "Confirm Canceled Lesson" (R56)."""
        raise NotImplementedError

    def seeCustomerSubscription(self) -> None:
        """Realizes UC52 "See Customer Subscription" (R57)."""
        raise NotImplementedError

    def seeCustomerCheckIn(self) -> None:
        """Realizes UC53 "See Customer Check In" (R61)."""
        raise NotImplementedError

    def seeCustomerBookings(self) -> None:
        """Realizes UC54 "See Customer Bookings" (R62)."""
        raise NotImplementedError

    def seeCustomerPastAndFutureSessions(self) -> None:
        """Realizes UC55 "See Customer Past And Future Sessions" (R60)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R47, R48, R49, R50, R58, R59"""
    name: _t.Optional[str] = None
    users: _t.Optional[str] = None
    customer: _t.Optional["Customer"] = None
    lesson: _t.Optional["Lesson"] = None

    def addTrainer(self) -> None:
        """Realizes UC42 "Add Trainer" (R47)."""
        raise NotImplementedError

    def addAdmin(self) -> None:
        """Realizes UC43 "Add Admin" (R48)."""
        raise NotImplementedError

    def removeTrainer(self) -> None:
        """Realizes UC44 "Remove Trainer" (R49)."""
        raise NotImplementedError

    def seeCustomerSubscription(self) -> None:
        """Realizes UC52 "See Customer Subscription" (R57)."""
        raise NotImplementedError

    def seeCustomerCheckIn(self) -> None:
        """Realizes UC53 "See Customer Check In" (R61)."""
        raise NotImplementedError

    def seeCustomerBookings(self) -> None:
        """Realizes UC54 "See Customer Bookings" (R62)."""
        raise NotImplementedError

    def seeCustomerPastAndFutureSessions(self) -> None:
        """Realizes UC55 "See Customer Past And Future Sessions" (R60)."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R40, R41, R42, R43, R44, R45, R46, R50, R58, R59"""
    name: _t.Optional[str] = None
    lessons: _t.Optional[str] = None
    lesson: _t.Optional["Lesson"] = None

    def addLesson(self) -> None:
        """Realizes UC23 "Add Lesson" (R26)."""
        raise NotImplementedError

    def setLessonTime(self) -> None:
        """Realizes UC24 "Set Lesson Time" (R27)."""
        raise NotImplementedError

    def setLessonDescription(self) -> None:
        """Realizes UC25 "Set Lesson Description" (R28)."""
        raise NotImplementedError

    def setLessonRoom(self) -> None:
        """Realizes UC26 "Set Lesson Room" (R29)."""
        raise NotImplementedError

    def setLessonType(self) -> None:
        """Realizes UC27 "Set Lesson Type" (R30)."""
        raise NotImplementedError

    def setLessonMaxPeople(self) -> None:
        """Realizes UC28 "Set Lesson Max People" (R31)."""
        raise NotImplementedError

    def seeSchedule(self) -> None:
        """Realizes UC29 "See Schedule" (R32)."""
        raise NotImplementedError

    def editLessonTime(self) -> None:
        """Realizes UC30 "Edit Lesson Time" (R34)."""
        raise NotImplementedError

    def changeLessonRoom(self) -> None:
        """Realizes UC31 "Change Lesson Room" (R35)."""
        raise NotImplementedError

    def editLessonDescription(self) -> None:
        """Realizes UC32 "Edit Lesson Description" (R36)."""
        raise NotImplementedError

    def editLessonMaxPeople(self) -> None:
        """Realizes UC33 "Edit Lesson Max People" (R37)."""
        raise NotImplementedError

    def editAnyLesson(self) -> None:
        """Realizes UC34 "Edit Any Lesson" (R38)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC35 "Cancel Lesson" (R39, R40)."""
        raise NotImplementedError


@_dc.dataclass
class Lesson:
    """Source: R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R40, R41, R42, R43, R44, R45, R46"""
    name: _t.Optional[str] = None
    time: _t.Optional[str] = None
    description: _t.Optional[str] = None
    room: _t.Optional[str] = None
    type: _t.Optional[str] = None
    maxPeople: _t.Optional[int] = None
    trainer: _t.Optional[str] = None

    def setTime(self) -> None:
        """Realizes UC24 "Set Lesson Time" (R27)."""
        raise NotImplementedError

    def setDescription(self) -> None:
        """Realizes UC25 "Set Lesson Description" (R28)."""
        raise NotImplementedError

    def setRoom(self) -> None:
        """Realizes UC26 "Set Lesson Room" (R29)."""
        raise NotImplementedError

    def setType(self) -> None:
        """Realizes UC27 "Set Lesson Type" (R30)."""
        raise NotImplementedError

    def setMaxPeople(self) -> None:
        """Realizes UC28 "Set Lesson Max People" (R31)."""
        raise NotImplementedError

    def editTime(self) -> None:
        """Realizes UC30 "Edit Lesson Time" (R34)."""
        raise NotImplementedError

    def changeRoom(self) -> None:
        """Realizes UC31 "Change Lesson Room" (R35)."""
        raise NotImplementedError

    def editDescription(self) -> None:
        """Realizes UC32 "Edit Lesson Description" (R36)."""
        raise NotImplementedError

    def editMaxPeople(self) -> None:
        """Realizes UC33 "Edit Lesson Max People" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Membership:
    """Source: R3, R4, R5, R6"""
    type: _t.Optional[str] = None
    duration: _t.Optional[int] = None


@_dc.dataclass
class Notification:
    """Source: R51, R52, R53, R54, R55, R56, R57"""
    method: _t.Optional[str] = None
    message: _t.Optional[str] = None
