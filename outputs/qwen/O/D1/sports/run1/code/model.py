class Customer:
    def __init__(self, personalInformation, bankingDetails, subscription, familyMembership):
        self.personalInformation = personalInformation
        self.bankingDetails = bankingDetails
        self.subscription = subscription
        self.familyMembership = familyMembership

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

    def seeOverview(self):
        raise NotImplementedError

    def seeRecord(self):
        raise NotImplementedError

    def seeLesson(self):
        raise NotImplementedError

    def seeRoom(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def bookSpot(self):
        raise NotImplementedError

    def callGym(self):
        raise NotImplementedError

    def addPerson(self):
        raise NotImplementedError

    def removePerson(self):
        raise NotImplementedError

class Admin:
    def __init__(self):
        pass

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

    def editTrainingSession(self):
        raise NotImplementedError

    def cancelLesson(self):
        raise NotImplementedError

    def notifySession(self):
        raise NotImplementedError

    def seeCustomer(self):
        raise NotImplementedError

    def seeInformation(self):
        raise NotImplementedError

    def seeLesson(self):
        raise NotImplementedError

    def seeRoom(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def seeSpot(self):
        raise NotImplementedError

    def bookSpot(self):
        raise NotImplementedError

    def callGym(self):
        raise NotImplementedError

    def addPerson(self):
        raise NotImplementedError

    def removePerson(self):
        raise NotImplementedError

class Trainer:
    def __init__(self, lessons):
        self.lessons = lessons

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

    def seeSchedule(self):
        raise NotImplementedError

    def seeLesson(self):
        raise NotImplementedError

    def seeRoom(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def seeSpot(self):
        raise NotImplementedError

    def bookSpot(self):
        raise NotImplementedError

    def callGym(self):
        raise NotImplementedError

    def addPerson(self):
        raise NotImplementedError

    def removePerson(self):
        raise NotImplementedError

class CustomerWithFamilyMembership:
    def __init__(self, familyMembership, people):
        self.familyMembership = familyMembership
        self.people = people

    def addPerson(self):
        raise NotImplementedError

    def removePerson(self):
        raise NotImplementedError
