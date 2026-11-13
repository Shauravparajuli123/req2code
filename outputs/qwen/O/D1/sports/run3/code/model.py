class Customer:
    def __init__(self, personalInformation, bankingDetails, subscription, password):
        self.personalInformation = personalInformation
        self.bankingDetails = bankingDetails
        self.subscription = subscription
        self.password = password

    def addInformation(self):
        raise NotImplementedError

    def addBankingDetail(self):
        raise NotImplementedError

    def chooseMembershipType(self):
        raise NotImplementedError

    def extendSubscription(self):
        raise NotImplementedError

    def knowSubscription(self):
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

    def addPerson(self):
        raise NotImplementedError

    def removePerson(self):
        raise NotImplementedError

    def seeOverview(self):
        raise NotImplementedError

    def seeRecord(self):
        raise NotImplementedError

    def seeLesson(self):
        raise NotImplementedError

    def seeSpot(self):
        raise NotImplementedError

    def seeRoom(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def callGym(self):
        raise NotImplementedError

    def bookSpot(self):
        raise NotImplementedError

    def seeCustomer(self):
        raise NotImplementedError

    def receiveNotification(self):
        raise NotImplementedError

    def haveMethod(self):
        raise NotImplementedError

    def seeInformation(self):
        raise NotImplementedError


class Admin:
    def __init__(self, password):
        self.password = password

    def editLesson(self):
        raise NotImplementedError

    def editTrainingSession(self):
        raise NotImplementedError

    def cancelLesson(self):
        raise NotImplementedError

    def haveFine(self):
        raise NotImplementedError

    def addTrainer(self):
        raise NotImplementedError

    def addAdmin(self):
        raise NotImplementedError

    def removeTrainer(self):
        raise NotImplementedError

    def seeCustomer(self):
        raise NotImplementedError

    def callGym(self):
        raise NotImplementedError

    def bookSpot(self):
        raise NotImplementedError

    def seeInformation(self):
        raise NotImplementedError


class Trainer:
    def __init__(self, password):
        self.password = password

    def addLesson(self):
        raise NotImplementedError

    def setDescription(self):
        raise NotImplementedError

    def setRoom(self):
        raise NotImplementedError

    def setTime(self):
        raise NotImplementedError

    def setNumber(self):
        raise NotImplementedError

    def setType(self):
        raise NotImplementedError

    def editLesson(self):
        raise NotImplementedError

    def cancelLesson(self):
        raise NotImplementedError

    def callGym(self):
        raise NotImplementedError

    def bookSpot(self):
        raise NotImplementedError

    def seeInformation(self):
        raise NotImplementedError


class CustomerWithFamilyMembership(Customer):
    def __init__(self, personalInformation, bankingDetails, subscription, password):
        super().__init__(personalInformation, bankingDetails, subscription, password)

    def addPerson(self):
        raise NotImplementedError

    def removePerson(self):
        raise NotImplementedError


class Gym:
    def __init__(self, requirement):
        self.requirement = requirement


class Lesson:
    def __init__(self, description, record):
        self.description = description
        self.record = record

    def setDescription(self):
        raise NotImplementedError

    def setRoom(self):
        raise NotImplementedError

    def setTime(self):
        raise NotImplementedError

    def setNumber(self):
        raise NotImplementedError

    def setType(self):
        raise NotImplementedError

    def editDescription(self):
        raise NotImplementedError

    def editTime(self):
        raise NotImplementedError

    def editRoom(self):
        raise NotImplementedError

    def editNumber(self):
        raise NotImplementedError

    def editType(self):
        raise NotImplementedError


class Room:
    def __init__(self, free):
        self.free = free

    def setFree(self):
        raise NotImplementedError


class Schedule:
    def __init__(self, lessons):
        self.lessons = lessons

    def addLesson(self):
        raise NotImplementedError

    def setTime(self):
        raise NotImplementedError

    def setRoom(self):
        raise NotImplementedError

    def setNumber(self):
        raise NotImplementedError

    def setType(self):
        raise NotImplementedError

    def editLesson(self):
        raise NotImplementedError

    def cancelLesson(self):
        raise NotImplementedError


class Notification:
    def __init__(self, method):
        self.method = method

    def chooseNotification(self):
        raise NotImplementedError

    def receiveNotification(self):
        raise NotImplementedError


class Fine:
    def __init__(self, offenseCount):
        self.offenseCount = offenseCount

    def haveFine(self):
        raise NotImplementedError
