from typing import List, Optional, Union

class Subscription:
    def __init__(self, duration: int):
        self.duration = duration
    def extend(self):
        raise NotImplementedError

class PersonalInformation:
    def __init__(self, personal_info: str):
        self.personal_info = personal_info

class PaymentInformation:
    def __init__(self, payment_info: str):
        self.payment_info = payment_info

class FamilyMembership:
    def __init__(self, members: List[str]):
        self.members = members
    def addPerson(self, person: str):
        raise NotImplementedError
    def removePerson(self, person: str):
        raise NotImplementedError

class Customer:
    def __init__(self, subscription: Subscription, personal_info: PersonalInformation, payment_info: PaymentInformation, family_membership: Optional[FamilyMembership] = None):
        self.subscription = subscription
        self.personal_info = personal_info
        self.payment_info = payment_info
        self.family_membership = family_membership
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
    def seeInformation(self):
        raise NotImplementedError
    def useInformation(self):
        raise NotImplementedError
    def unsubscribe(self):
        raise NotImplementedError
    def resetPassword(self):
        raise NotImplementedError
    def changeDetail(self):
        raise NotImplementedError
    def updatePaymentInformation(self):
        raise NotImplementedError
    def seeRecord(self):
        raise NotImplementedError
    def seeLesson(self):
        raise NotImplementedError
    def seeMembership(self):
        raise NotImplementedError
    def seeOverview(self):
        raise NotImplementedError
    def seeSpot(self):
        raise NotImplementedError
    def bookSpot(self):
        raise NotImplementedError
    def callGym(self):
        raise NotImplementedError
    def receiveNotification(self):
        raise NotImplementedError
    def receivePushNotification(self):
        raise NotImplementedError
    def confirmBooking(self):
        raise NotImplementedError
    def logSystem(self):
        raise NotImplementedError

class Admin:
    def __init__(self):
        pass
    def addTrainer(self):
        raise NotImplementedError
    def addAdmin(self):
        raise NotImplementedError
    def removeTrainer(self):
        raise NotImplementedError
    def editTrainingSession(self):
        raise NotImplementedError
    def cancelLesson(self):
        raise NotImplementedError

class Trainer:
    def __init__(self):
        self.lessons = []
    def addLesson(self):
        raise NotImplementedError
    def setTime(self):
        raise NotImplementedError
    def setDescription(self):
        raise NotImplementedError
    def setRoom(self):
        raise NotImplementedError
    def setNumber(self):
        raise NotImplementedError
    def editLesson(self):
        raise NotImplementedError
    def editTime(self):
        raise NotImplementedError
    def editRoom(self):
        raise NotImplementedError
    def editDescription(self):
        raise NotImplementedError
    def editNumber(self):
        raise NotImplementedError
    def cancelLesson(self):
        raise NotImplementedError

class Lesson:
    def __init__(self, description: str, record: str, room: str, time: str):
        self.description = description
        self.record = record
        self.room = room
        self.time = time
    def setTime(self):
        raise NotImplementedError
    def setDescription(self):
        raise NotImplementedError
    def setRoom(self):
        raise NotImplementedError
    def setNumber(self):
        raise NotImplementedError

class Room:
    def __init__(self, availability: bool):
        self.availability = availability
    def checkAvailability(self):
        raise NotImplementedError

class Notification:
    def __init__(self, method: str):
        self.method = method
    def sendNotification(self):
        raise NotImplementedError
    def sendPushNotification(self):
        raise NotImplementedError

class Fine:
    def __init__(self, amount: int, offense_count: int):
        self.amount = amount
        self.offense_count = offense_count
    def issueFine(self):
        raise NotImplementedError