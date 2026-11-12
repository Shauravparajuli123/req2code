# Artefact set D1_ticket_Z

## Use cases
- Fill Information (actor: user)
- Save Information (actor: user)
- Save PaymentDetail (actor: user)
- Fill Survey (actor: user)
- See Content (actor: user)
- See Event (actor: visitor)
- Purchase Ticket (actor: visitor)
- See History (actor: user)
- See Overview (actor: user)
- See Preference (actor: user)
- See Seat (actor: visitor)
- See Type (actor: visitor)
- Edit Information (actor: user)
- Change Password (actor: user)
- See OrderSummary (actor: visitor)
- Land EventPage (actor: visitor)
- Click Event (actor: visitor)
- Have BuyingProcess (actor: company)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)
-  (actor: -)

## Class diagram
- User: attributes ['name', 'dateOfBirth', 'email', 'address', 'preferences', 'personalInformation', 'paymentDetails', 'history', 'profile']; methods ['fillInformation', 'saveInformation', 'editInformation', 'changePassword', 'seeContent', 'seePreference', 'seeHistory', 'seeOverview']
- Visitor: attributes ['name', 'email', 'tickets', 'events']; methods ['seeEvent', 'purchaseTicket', 'seeSeat', 'seeType', 'clickEvent', 'landEventPage', 'seeOrderSummary', 'seeHistory', 'seeOverview', 'seeContent']
- Artist: attributes ['name', 'events', 'description', 'links']; methods ['findInformation', 'haveDescription', 'haveLink']
- Event: attributes ['name', 'date', 'location', 'artist', 'type', 'price', 'tickets']; methods ['seeEvent', 'seeType', 'seeSeat']
- Ticket: attributes ['event', 'price', 'type', 'seat']; methods ['addTicket', 'sellTicket', 'resellTicket']
- Company: attributes ['buyingProcess', 'resellers', 'serviceFee']; methods ['haveBuyingProcess', 'avoidBehavior', 'deductServiceFee', 'validateTicket']
- Reseller: attributes ['name', 'bankAccount', 'tickets']; methods ['sellTicket', 'resellTicket', 'saveBankAccount']
- Address: attributes ['street', 'city', 'state', 'zipCode']; methods []
- Preference: attributes ['genre', 'eventTypes']; methods []
- PaymentDetail: attributes ['cardNumber', 'expiryDate', 'cvv']; methods []
- OrderSummary: attributes ['tickets', 'totalPrice']; methods []
- UserProfile: attributes ['name', 'dateOfBirth', 'email', 'address', 'preferences', 'paymentDetails', 'history', 'profile']; methods []
- Venue: attributes ['name', 'map']; methods []
- Link: attributes ['url']; methods []
- Cent: attributes ['value']; methods []
- Process: attributes []; methods []
- BankAccount: attributes ['iban']; methods []
- User --association--> UserProfile
- User --association--> PaymentDetail
- User --association--> Preference
- User --association--> OrderSummary
- User --association--> UserProfile
- User --association--> UserProfile
- Visitor --association--> Event
- Visitor --association--> Ticket
- Artist --association--> Event
- Event --association--> Artist
- Event --association--> Venue
- Event --association--> Ticket
- Ticket --association--> Event
- Ticket --association--> Seat
- Company --association--> Reseller
- Reseller --association--> BankAccount
- Reseller --association--> Ticket
- Reseller --association--> Ticket

## Python code
```python
from typing import List, Optional, Union

class String:
    pass
class Date:
    pass
class Cent:
    pass
class Address:
    street: String
city: String
state: String
zipCode: String
class Preference:
    genre: String
eventTypes: List[String]
class PaymentDetail:
    cardNumber: String
expiryDate: Date
cvv: String
class OrderSummary:
    tickets: List[Ticket]
totalPrice: Cent
class UserProfile:
    name: String
dateOfBirth: Date
eMail: String
address: Address
preferences: Preference
paymentDetails: PaymentDetail
history: List[OrderSummary]
profile: UserProfile
class User:
    name: String
dateOfBirth: Date
eMail: String
address: Address
preferences: Preference
personalInformation: String
paymentDetails: PaymentDetail
history: OrderSummary
profile: UserProfile
    def fillInformation(self):
        raise NotImplementedError
    def saveInformation(self):
        raise NotImplementedError
    def editInformation(self):
        raise NotImplementedError
    def changePassword(self):
        raise NotImplementedError
    def seeContent(self):
        raise NotImplementedError
    def seePreference(self):
        raise NotImplementedError
    def seeHistory(self):
        raise NotImplementedError
    def seeOverview(self):
        raise NotImplementedError
class Visitor:
    name: String
eMail: String
tickets: List[Ticket]
events: List[Event]
    def seeEvent(self):
        raise NotImplementedError
    def purchaseTicket(self):
        raise NotImplementedError
    def seeSeat(self):
        raise NotImplementedError
    def seeType(self):
        raise NotImplementedError
    def clickEvent(self):
        raise NotImplementedError
    def landEventPage(self):
        raise NotImplementedError
    def seeOrderSummary(self):
        raise NotImplementedError
    def seeHistory(self):
        raise NotImplementedError
    def seeOverview(self):
        raise NotImplementedError
    def seeContent(self):
        raise NotImplementedError
class Artist:
    name: String
events: List[Event]
description: String
links: List[Link]
    def findInformation(self):
        raise NotImplementedError
    def haveDescription(self):
        raise NotImplementedError
    def haveLink(self):
        raise NotImplementedError
class Event:
    name: String
date: Date
location: Venue
artist: Artist
type: String
price: Cent
tickets: List[Ticket]
    def seeEvent(self):
        raise NotImplementedError
    def seeType(self):
        raise NotImplementedError
    def seeSeat(self):
        raise NotImplementedError
class Ticket:
    event: Event
price: Cent
type: String
seat: String
    def addTicket(self):
        raise NotImplementedError
    def sellTicket(self):
        raise NotImplementedError
    def resellTicket(self):
        raise NotImplementedError
class Company:
    buyingProcess: Process
resellers: List[Reseller]
serviceFee: Cent
    def haveBuyingProcess(self):
        raise NotImplementedError
    def avoidBehavior(self):
        raise NotImplementedError
    def deductServiceFee(self):
        raise NotImplementedError
    def validateTicket(self):
        raise NotImplementedError
class Reseller:
    name: String
bankAccount: BankAccount
tickets: List[Ticket]
    def sellTicket(self):
        raise NotImplementedError
    def resellTicket(self):
        raise NotImplementedError
    def saveBankAccount(self):
        raise NotImplementedError
class Venue:
    name: String
map: String
class Link:
    url: String
class Process:
    pass
class BankAccount:
    iban: String
```