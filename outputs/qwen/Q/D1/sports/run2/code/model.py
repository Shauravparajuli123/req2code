from typing import List, Optional, Union

class Person:
    pass

class Room:
    pass

class Lesson:
    def __init__(self, description: str, room: Room, type: str, numberOfPeopleAllowed: int):
        self.description = description
        self.room = room
        self.type = type
        self.numberOfPeopleAllowed = numberOfPeopleAllowed

class FamilyMembership:
    def __init__(self):
        self.members: List[Person] = []
    def addPerson(self, person: Person):
        self.members.append(person)
    def removePerson(self, person: Person):
        self.members.remove(person)

class Customer:
    def __init__(self):
        self.account: Account = Account()
        self.subscription: Subscription = Subscription()
        self.information: Information = Information()
        self.paymentInformation: PaymentInformation = PaymentInformation()
        self.familyMembership: Optional[FamilyMembership] = None
    def openAccount(self):
        raise NotImplementedError
    def addInformation(self):
        raise NotImplementedError
    def addBankingDetail(self):
        raise NotImplementedError
    def chooseMembershipType(self):
        raise NotImplementedError
    def extendSubscription(self):
        raise NotImplementedError
    def seeHowLongSubscriptionLasts(self):
        raise NotImplementedError
    def usePreviousInformation(self):
        raise NotImplementedError
    def unsubscribe(self):
        raise NotImplementedError
    def resetPassword(self):
        raise NotImplementedError
    def changeDetail(self):
        raise NotImplementedError
    def updatePaymentInformation(self):
        raise NotImplementedError
    def seeOverviewOfLessons(self):
        raise NotImplementedError
    def seeFutureLessons(self):
        raise NotImplementedError
    def seeRecordOfPreviousLessons(self):
        raise NotImplementedError
    def callGymToBookLesson(self):
        raise NotImplementedError
    def callGymToCancelLesson(self):
        raise NotImplementedError
    def callGymToBookPersonalTrainingSession(self):
        raise NotImplementedError
    def callGymToCancelPersonalTrainingSession(self):
        raise NotImplementedError
    def bookSpotForFreePracticeArea(self):
        raise NotImplementedError
    def seeHowManySpotsBooked(self):
        raise NotImplementedError
    def receiveNotificationOfBookingCancellation(self):
        raise NotImplementedError
    def confirmBookingCancellation(self):
        raise NotImplementedError
    def seeCustomerInformation(self):
        raise NotImplementedError
    def seeCustomerMembership(self):
        raise NotImplementedError

class Admin:
    def __init__(self):
        pass
    def addNewTrainer(self):
        raise NotImplementedError
    def addNewAdmin(self):
        raise NotImplementedError
    def removeTrainer(self):
        raise NotImplementedError
    def seeCustomerInformation(self):
        raise NotImplementedError
    def seeCustomerSubscription(self):
        raise NotImplementedError
    def seeIfCustomerDidNotShowUp(self):
        raise NotImplementedError
    def seeHowManyTimesCustomerDidNotShowUp(self):
        raise NotImplementedError
    def issueFineForRepeatOffenders(self):
        raise NotImplementedError
    def editAnyLesson(self):
        raise NotImplementedError
    def cancelLessonByAdmin(self):
        raise NotImplementedError

class Trainer:
    def __init__(self):
        self.lessons: List[Lesson] = []
    def addLesson(self):
        raise NotImplementedError
    def setTimeOfLesson(self):
        raise NotImplementedError
    def setDescriptionOfLesson(self):
        raise NotImplementedError
    def setRoomOfLesson(self):
        raise NotImplementedError
    def setTypeOfLesson(self):
        raise NotImplementedError
    def setNumberPeopleAllowed(self):
        raise NotImplementedError
    def seeSchedule(self):
        raise NotImplementedError
    def editLesson(self):
        raise NotImplementedError
    def editTimeOfLesson(self):
        raise NotImplementedError
    def editRoomOfLesson(self):
        raise NotImplementedError
    def editDescriptionOfLesson(self):
        raise NotImplementedError
    def editNumberPeopleAllowed(self):
        raise NotImplementedError
    def cancelLesson(self):
        raise NotImplementedError

class Notification:
    def __init__(self, method: str):
        self.method = method
    def chooseNotificationMethod(self):
        raise NotImplementedError
    def receiveEmailNotification(self):
        raise NotImplementedError
    def receivePushNotification(self):
        raise NotImplementedError
    def chooseWhatToReceiveNotificationsFor(self):
        raise NotImplementedError

class Subscription:
    pass

class Account:
    pass

class Information:
    pass

class PaymentInformation:
    pass

class Method:
    pass