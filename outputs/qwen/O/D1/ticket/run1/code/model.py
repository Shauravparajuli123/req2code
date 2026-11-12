class User:
    def __init__(self, name, dateOfBirth, email, address, preferences):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.address = address
        self.preferences = preferences

    def savePersonalInformation(self):
        raise NotImplementedError

    def savePaymentDetails(self):
        raise NotImplementedError

    def fillSurvey(self):
        raise NotImplementedError

    def seePersonalizedContent(self):
        raise NotImplementedError

    def editPreferences(self):
        raise NotImplementedError

    def changePassword(self):
        raise NotImplementedError

    def editPersonalInformation(self):
        raise NotImplementedError

class Visitor:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def buyTicket(self):
        raise NotImplementedError

class Reseller:
    def __init__(self, bankAccount):
        self.bankAccount = bankAccount

    def resellTicket(self):
        raise NotImplementedError

class Address:
    pass

class Preference:
    pass

class BankAccount:
    pass