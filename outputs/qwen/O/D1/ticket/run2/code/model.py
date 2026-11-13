class User:
    def __init__(self, name, dateOfBirth, email, address, preferences):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.address = address
        self.preferences = preferences

    def saveInformation(self):
        raise NotImplementedError

    def savePaymentDetail(self):
        raise NotImplementedError

    def fillSurvey(self):
        raise NotImplementedError

    def seeContent(self):
        raise NotImplementedError

    def seePreference(self):
        raise NotImplementedError

    def changePassword(self):
        raise NotImplementedError

    def editInformation(self):
        raise NotImplementedError

    def seeHistory(self):
        raise NotImplementedError

    def seeOverview(self):
        raise NotImplementedError
class Visitor:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def purchaseTicket(self):
        raise NotImplementedError

    def readEvent(self):
        raise NotImplementedError

    def buyTicket(self):
        raise NotImplementedError

    def seeEvent(self):
        raise NotImplementedError

    def clickEvent(self):
        raise NotImplementedError

    def landEventPage(self):
        raise NotImplementedError

    def filterSearch(self):
        raise NotImplementedError

    def filterList(self):
        raise NotImplementedError

    def filterSearchResult(self):
        raise NotImplementedError

    def sortSearchResult(self):
        raise NotImplementedError

    def addTicket(self):
        raise NotImplementedError

    def seeOrderSummary(self):
        raise NotImplementedError

    def seeSeat(self):
        raise NotImplementedError

    def seeType(self):
        raise NotImplementedError
class Company:
    def __init__(self, buyingProcess):
        self.buyingProcess = buyingProcess

    def avoidBehavior(self):
        raise NotImplementedError

    def deductServiceFee(self):
        raise NotImplementedError

    def validateTicket(self):
        raise NotImplementedError

    def protectUser(self):
        raise NotImplementedError

    def haveReseller(self):
        raise NotImplementedError
class Reseller:
    def __init__(self, bankAccount):
        self.bankAccount = bankAccount

    def resellTicket(self):
        raise NotImplementedError

    def saveBankAccount(self):
        raise NotImplementedError
class Address:
    def __init__(self, street, city, state, zipCode):
        self.street = street
        self.city = city
        self.state = state
        self.zipCode = zipCode
class Preference:
    def __init__(self, musicGenre, eventTypes):
        self.musicGenre = musicGenre
        self.eventTypes = eventTypes
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
class Event:
    def __init__(self, description, date, artist, venue, price, type):
        self.description = description
        self.date = date
        self.artist = artist
        self.venue = venue
        self.price = price
        self.type = type

    def seeEvent(self):
        raise NotImplementedError
class EventPage:
    def __init__(self, event, links):
        self.event = event
        self.links = links

    def findInformation(self):
        raise NotImplementedError

    def haveLink(self):
        raise NotImplementedError
class Link:
    def __init__(self, url):
        self.url = url
class Cent:
    def __init__(self, value):
        self.value = value
class Venue:
    def __init__(self, map):
        self.map = map