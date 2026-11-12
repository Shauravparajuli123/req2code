from typing import String, Integer

class Customer:
    def __init__(self, name: String, subscription: Subscription, familyMembership: Boolean, personalInformation: String, bankingDetails: String, password: String, method: Method):
        self.name = name
        self.subscription = subscription
        self.familyMembership = familyMembership
        self.personalInformation = personalInformation
        self.bankingDetails = bankingDetails
        self.password = password
        self.method = method

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

    def seeLesson(self):
        raise NotImplementedError

    def seeRecord(self):
        raise NotImplementedError

    def seeOverview(self):
        raise NotImplementedError

    def callGym(self):
        raise NotImplementedError

    def bookSpot(self):
        raise NotImplementedError

    def seeSpot(self):
        raise NotImplementedError

    def seeRoom(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def seeCustomer(self):
        raise NotImplementedError

    def seeSubscription(self):
        raise NotImplementedError

    def seeInformation(self):
        raise NotImplementedError

class Admin:
    def __init__(self, name: String):
        self.name = name

    def haveSystem(self):
        raise NotImplementedError

    def knowCustomer(self):
        raise NotImplementedError

    def knowSubscription(self):
        raise NotImplementedError

    def seeCustomer(self):
        raise NotImplementedError

    def addPerson(self):
        raise NotImplementedError

    def removePerson(self):
        raise NotImplementedError

    def addTrainer(self):
        raise NotImplementedError

    def addAdmin(self):
        raise NotImplementedError

    def removeTrainer(self):
        raise NotImplementedError

    def editLesson(self):
        raise NotImplementedError

    def editTime(self):
        raise NotImplementedError

    def editDescription(self):
        raise NotImplementedError

    def editNumber(self):
        raise NotImplementedError

    def editRoom(self):
        raise NotImplementedError

    def editTrainingSession(self):
        raise NotImplementedError

    def cancelLesson(self):
        raise NotImplementedError

class Trainer:
    def __init__(self, name: String):
        self.name = name

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

    def setType(self):
        raise NotImplementedError

    def editLesson(self):
        raise NotImplementedError

    def editTime(self):
        raise NotImplementedError

    def editDescription(self):
        raise NotImplementedError

    def editNumber(self):
        raise NotImplementedError

    def editRoom(self):
        raise NotImplementedError

    def editTrainingSession(self):
        raise NotImplementedError

    def cancelLesson(self):
        raise NotImplementedError
class Method:
    def __init__(self, type: String):
        self.type = type

    def haveMethod(self):
        raise NotImplementedError
class Notification:
    def __init__(self, type: String):
        self.type = type

    def receiveNotification(self):
        raise NotImplementedError

    def receivePushNotification(self):
        raise NotImplementedError

    def chooseNotification(self):
        raise NotImplementedError

    def confirmBooking(self):
        raise NotImplementedError
class Lesson:
    def __init__(self, description: String, record: String):
        self.description = description
        self.record = record

    def addLesson(self):
        raise NotImplementedError

    def setDescription(self):
        raise NotImplementedError

    def setRoom(self):
        raise NotImplementedError

    def setTime(self):
        raise NotImplementedError

    def setType(self):
        raise NotImplementedError

    def setNumber(self):
        raise NotImplementedError
class Subscription:
    def __init__(self, type: String):
        self.type = type

    def extendSubscription(self):
        raise NotImplementedError
class Fine:
    def __init__(self, amount: Integer):
        self.amount = amount

    def haveFine(self):
        raise NotImplementedError