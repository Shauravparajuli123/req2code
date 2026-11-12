# Artefact set D1_ticket_Y

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
- User: attributes ['name', 'dateOfBirth', 'email', 'address', 'preferences']; methods ['fillInformation', 'editInformation', 'saveInformation', 'seePreference', 'seeContent', 'seeOrderSummary', 'seeHistory', 'seeOverview', 'seeEvent', 'seeSeat', 'seeType', 'seeOrderSummary', 'seeEventPage', 'seeCalendarView', 'seePopularEvents', 'seeUserProfile', 'seeLinks', 'seeDescription', 'seeFavoriteEvents', 'changePassword']
- Guest: attributes ['name', 'email']; methods ['fillName', 'fillInformation', 'seeOrderSummary', 'seeEvent', 'seeSeat', 'seeType', 'seeOrderSummary', 'seeEventPage', 'seeCalendarView', 'seePopularEvents', 'seeFavoriteEvents']
- Visitor: attributes []; methods ['seeEvent', 'seeSeat', 'seeType', 'seeOrderSummary', 'seeEventPage', 'seeCalendarView', 'seePopularEvents', 'seeFavoriteEvents']
- Company: attributes ['minimumResellPrice', 'resellingProcess']; methods ['haveBuyingProcess', 'haveReseller', 'avoidBehavior', 'protectUser', 'validateTicket', 'deductServiceFee']
- Reseller: attributes ['bankAccount']; methods ['resellTicket', 'uploadTicket', 'setPrice', 'addDescription', 'saveBankAccount']
- Event: attributes ['description', 'date', 'venue', 'artist', 'price']; methods ['findInformation', 'seeEventPage']
- Ticket: attributes ['type', 'seat']; methods ['addTicketToCart', 'seeOrderSummary']
- Address: attributes ['street', 'city', 'zipCode']; methods []
- Preference: attributes ['genre', 'eventTypes']; methods []
- BankAccount: attributes ['iban']; methods []
- Cent: attributes []; methods []
- ResellingProcess: attributes []; methods []
- SearchResult: attributes []; methods []
- Seat: attributes ['row', 'column']; methods []
- Venue: attributes ['map']; methods []
- Artist: attributes ['links']; methods []
- Link: attributes ['url']; methods []
- User --association--> UserProfile
- User --association--> Preference
- User --association--> Ticket
- User --association--> Event
- Guest --association--> Ticket
- Visitor --association--> Ticket
- Company --association--> Reseller
- Reseller --association--> Ticket
- Event --association--> Venue
- Event --association--> Artist
- Artist --association--> Event

## Python code
```python
from typing import TypedDict, List, Optional

class Address(TypedDict):
    street: str
    city: str
    state: str
    zip_code: str

class BankAccount(TypedDict):
    iban: str

class Event(TypedDict):
    name: str
    date: Date
    venue: Venue
    description: str
    artist: Artist
    genre: str
    types: List[str]

class EventPage(TypedDict):
    event: Event
    artist_links: List[Link]

class Fan(TypedDict):
    name: str
    email: str

class Guest(TypedDict):
    name: str
    email: str

class Link(TypedDict):
    url: str
    platform: str

class Platform(TypedDict):
    name: str
    failure: bool

class Preference(TypedDict):
    music_genre: str
    event_types: List[str]

class Process(TypedDict):
    steps: List[str]

class Reseller(TypedDict):
    name: str
    bank_account: BankAccount

class ResellingProcess(TypedDict):
    reseller: Reseller
    ticket: Ticket
    price: int

class SearchResult(TypedDict):
    events: List[Event]

class Seat(TypedDict):
    row: int
    column: int

class ServiceFee(TypedDict):
    percentage: float

class Show(TypedDict):
    name: str
    date: Date
    artist: Artist

class Ticket(TypedDict):
    event: Event
    type: str
    seat: Seat

class User(TypedDict):
    name: str
    email: str
    address: Address
    preferences: Preference
    profile: UserProfile
    tickets: List[Ticket]
    favorites: List[Event]

class UserProfile(TypedDict):
    name: str
    email: str
    address: Address
    preferences: Preference
    payment_details: PaymentDetails
    history: List[Ticket]

class Venue(TypedDict):
    name: str
    map: str

class Visitor(TypedDict):
    name: str
    email: str

class PaymentDetails(TypedDict):
    card_number: str
    expiration_date: str
    cvv: str

class Company(TypedDict):
    name: str
    process: Process
    service_fee: ServiceFee
    resellers: List[Reseller]
    search_engine: Platform
    validation_process: Process

class Date(TypedDict):
    year: int
    month: int
    day: int


class AddTicket:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class AvoidBehavior:
    def __init__(self, company: Company):
        raise NotImplementedError

class BuyTicket:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class ChangePassword:
    def __init__(self, user: User):
        raise NotImplementedError

class ClickEvent:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class DeductServiceFee:
    def __init__(self, company: Company):
        raise NotImplementedError

class EditInformation:
    def __init__(self, user: User):
        raise NotImplementedError

class FavoriteEvent:
    def __init__(self, user: User):
        raise NotImplementedError

class FillInformation:
    def __init__(self, guest: Guest):
        raise NotImplementedError

class FillName:
    def __init__(self, guest: Guest):
        raise NotImplementedError

class FillSurvey:
    def __init__(self, user: User):
        raise NotImplementedError

class FilterList:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class FilterSearch:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class FilterSearchResult:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class FindInformation:
    def __init__(self, artist: Artist):
        raise NotImplementedError

class FindList:
    def __init__(self, user: User):
        raise NotImplementedError

class GetList:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class HaveBuyingProcess:
    def __init__(self, company: Company):
        raise NotImplementedError

class HaveDescription:
    def __init__(self, artist: Artist):
        raise NotImplementedError

class HaveLink:
    def __init__(self, artist: Artist):
        raise NotImplementedError

class HavePrice:
    def __init__(self, company: Company):
        raise NotImplementedError

class HaveReseller:
    def __init__(self, company: Company):
        raise NotImplementedError

class HaveSearchEngine:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class LandEventPage:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class ProtectUser:
    def __init__(self, company: Company):
        raise NotImplementedError

class PurchaseTicket:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class ReadEvent:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class ResellTicket:
    def __init__(self, reseller: Reseller):
        raise NotImplementedError

class SaveBankAccount:
    def __init__(self, reseller: Reseller):
        raise NotImplementedError

class SaveInformation:
    def __init__(self, user: User):
        raise NotImplementedError

class SeeContent:
    def __init__(self, user: User):
        raise NotImplementedError

class SeeEvent:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class SeeHistory:
    def __init__(self, user: User):
        raise NotImplementedError

class SeeList:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class SeeOrderSummary:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class SeeOverview:
    def __init__(self, user: User):
        raise NotImplementedError

class SeePreference:
    def __init__(self, user: User):
        raise NotImplementedError

class SeeSeat:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class SeeType:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class SellTicket:
    def __init__(self, reseller: Reseller):
        raise NotImplementedError

class SortSearchResult:
    def __init__(self, visitor: Visitor):
        raise NotImplementedError

class ValidateTicket:
    def __init__(self, company: Company):
        raise NotImplementedError
```