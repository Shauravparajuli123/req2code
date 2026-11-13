"""Code skeleton generated from the shared model of D1/sports.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R58, R59, R60, R61, R62, R63"""
    name: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    bankingDetails: _t.Optional[str] = None
    membershipType: _t.Optional[str] = None
    subscription: _t.Optional[str] = None
    previousInformation: _t.Optional[str] = None
    familyMembership: _t.Optional[bool] = None
    lessonOverview: _t.Optional[str] = None
    bookedLessons: _t.Optional[str] = None
    recordOfLessons: _t.Optional[str] = None
    lessonCancellation: _t.Optional[str] = None
    personalTrainingBooking: _t.Optional[str] = None
    freePracticeAreaBooking: _t.Optional[str] = None
    notificationMethod: _t.Optional[str] = None
    subscriptionCheck: _t.Optional[bool] = None
    checkIn: _t.Optional[bool] = None

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

    def addPersonToFamilyMembership(self) -> None:
        """Realizes UC12 "Add Person To Family Membership" (R13)."""
        raise NotImplementedError

    def removePersonFromFamilyMembership(self) -> None:
        """Realizes UC13 "Remove Person From Family Membership" (R14)."""
        raise NotImplementedError

    def seeOverviewOfLessons(self) -> None:
        """Realizes UC14 "See Overview Of Lessons" (R15)."""
        raise NotImplementedError

    def seeBookedLessons(self) -> None:
        """Realizes UC15 "See Booked Lessons" (R16)."""
        raise NotImplementedError

    def seeRecordOfLessons(self) -> None:
        """Realizes UC16 "See Record Of Lessons" (R17)."""
        raise NotImplementedError

    def callGymToBookLesson(self) -> None:
        """Realizes UC17 "Call Gym To Book Lesson" (R18)."""
        raise NotImplementedError

    def callGymToCancelLesson(self) -> None:
        """Realizes UC18 "Call Gym To Cancel Lesson" (R19)."""
        raise NotImplementedError

    def callGymToBookPersonalTraining(self) -> None:
        """Realizes UC19 "Call Gym To Book Personal Training" (R21)."""
        raise NotImplementedError

    def callGymToCancelPersonalTraining(self) -> None:
        """Realizes UC20 "Call Gym To Cancel Personal Training" (R22)."""
        raise NotImplementedError

    def bookSpotForFreePracticeArea(self) -> None:
        """Realizes UC21 "Book Spot For Free Practice Area" (R23)."""
        raise NotImplementedError

    def seeBookedSpots(self) -> None:
        """Realizes UC22 "See Booked Spots" (R24)."""
        raise NotImplementedError

    def seeFreeRooms(self) -> None:
        """Realizes UC23 "See Free Rooms" (R25)."""
        raise NotImplementedError

    def seeTrainerSchedule(self) -> None:
        """Realizes UC52 "See Trainer Schedule" (R32)."""
        raise NotImplementedError


@_dc.dataclass
class Admin:
    """Source: R46, R47, R48, R49, R50, R51, R52, R53, R54, R55, R56, R57, R60"""
    name: _t.Optional[str] = None
    notificationMethod: _t.Optional[str] = None
    subscriptionCheck: _t.Optional[bool] = None
    trainer: _t.Optional["Trainer"] = None

    def addTrainer(self) -> None:
        """Realizes UC41 "Add Trainer" (R47)."""
        raise NotImplementedError

    def addAdmin(self) -> None:
        """Realizes UC42 "Add Admin" (R48)."""
        raise NotImplementedError

    def removeTrainer(self) -> None:
        """Realizes UC43 "Remove Trainer" (R49)."""
        raise NotImplementedError

    def logIntoSystem(self) -> None:
        """Realizes UC44 "Log Into System" (R50)."""
        raise NotImplementedError

    def chooseNotificationMethod(self) -> None:
        """Realizes UC45 "Choose Notification Method" (R51)."""
        raise NotImplementedError

    def receiveEmailNotification(self) -> None:
        """Realizes UC46 "Receive Email Notification" (R52)."""
        raise NotImplementedError

    def receivePushNotification(self) -> None:
        """Realizes UC47 "Receive Push Notification" (R53)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC48 "Choose Notifications" (R54)."""
        raise NotImplementedError

    def confirmBookingCancellation(self) -> None:
        """Realizes UC49 "Confirm Booking Cancellation" (R56)."""
        raise NotImplementedError

    def seeCustomerNoShow(self) -> None:
        """Realizes UC38 "Know Customer No Show" (R43)."""
        raise NotImplementedError

    def seeNumberOfNoShows(self) -> None:
        """Realizes UC39 "Know Number Of No Shows" (R44)."""
        raise NotImplementedError

    def issueFineForNoShow(self) -> None:
        """Realizes UC40 "Issue Fine For No Show" (R45, R46)."""
        raise NotImplementedError


@_dc.dataclass
class Trainer:
    """Source: R20, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R42, R43, R44, R45, R52, R53, R54, R55, R56, R60"""
    name: _t.Optional[str] = None
    notificationMethod: _t.Optional[str] = None
    subscriptionCheck: _t.Optional[bool] = None

    def editLesson(self) -> None:
        """Realizes UC34 "Edit Lesson" (R20, R33)."""
        raise NotImplementedError

    def editLessonTime(self) -> None:
        """Realizes UC30 "Edit Lesson Time" (R34)."""
        raise NotImplementedError

    def editLessonRoom(self) -> None:
        """Realizes UC31 "Edit Lesson Room" (R35)."""
        raise NotImplementedError

    def editLessonDescription(self) -> None:
        """Realizes UC32 "Edit Lesson Description" (R36)."""
        raise NotImplementedError

    def editLessonNumber(self) -> None:
        """Realizes UC33 "Edit Lesson Number" (R37)."""
        raise NotImplementedError

    def cancelLesson(self) -> None:
        """Realizes UC35 "Cancel Lesson" (R39, R40)."""
        raise NotImplementedError
