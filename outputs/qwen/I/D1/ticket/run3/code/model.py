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
    preferences: Preference

class Guest(TypedDict):
    name: str
    email: str

class Link(TypedDict):
    url: str
    platform: str

class Preference(TypedDict):
    music_genre: str
    event_types: List[str]

class Process(TypedDict):
    steps: List[str]

class Reseller(TypedDict):
    name: str
    bank_account: BankAccount

class ResellingProcess(TypedDict):
    tickets: List[Ticket]
    price: float
    description: str

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
    favorites: List[Event]

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


class AddTicket:
    def __init__(self):
        raise NotImplementedError

class AvoidBehavior:
    def __init__(self):
        raise NotImplementedError

class BuyTicket:
    def __init__(self):
        raise NotImplementedError

class ChangePassword:
    def __init__(self):
        raise NotImplementedError

class ClickEvent:
    def __init__(self):
        raise NotImplementedError

class DeductServiceFee:
    def __init__(self):
        raise NotImplementedError

class EditInformation:
    def __init__(self):
        raise NotImplementedError

class FavoriteEvent:
    def __init__(self):
        raise NotImplementedError

class FillInformation:
    def __init__(self):
        raise NotImplementedError

class FillName:
    def __init__(self):
        raise NotImplementedError

class FillSurvey:
    def __init__(self):
        raise NotImplementedError

class FilterList:
    def __init__(self):
        raise NotImplementedError

class FilterSearch:
    def __init__(self):
        raise NotImplementedError

class FilterSearchResult:
    def __init__(self):
        raise NotImplementedError

class FindInformation:
    def __init__(self):
        raise NotImplementedError

class FindList:
    def __init__(self):
        raise NotImplementedError

class GetList:
    def __init__(self):
        raise NotImplementedError

class HaveBuyingProcess:
    def __init__(self):
        raise NotImplementedError

class HaveDescription:
    def __init__(self):
        raise NotImplementedError

class HaveLink:
    def __init__(self):
        raise NotImplementedError

class HavePrice:
    def __init__(self):
        raise NotImplementedError

class HaveReseller:
    def __init__(self):
        raise NotImplementedError

class HaveSearchEngine:
    def __init__(self):
        raise NotImplementedError

class LandEventPage:
    def __init__(self):
        raise NotImplementedError

class ProtectUser:
    def __init__(self):
        raise NotImplementedError

class PurchaseTicket:
    def __init__(self):
        raise NotImplementedError

class ReadEvent:
    def __init__(self):
        raise NotImplementedError

class ResellTicket:
    def __init__(self):
        raise NotImplementedError

class SaveBankAccount:
    def __init__(self):
        raise NotImplementedError

class SaveInformation:
    def __init__(self):
        raise NotImplementedError

class SeeContent:
    def __init__(self):
        raise NotImplementedError

class SeeEvent:
    def __init__(self):
        raise NotImplementedError

class SeeHistory:
    def __init__(self):
        raise NotImplementedError

class SeeList:
    def __init__(self):
        raise NotImplementedError

class SeeOrderSummary:
    def __init__(self):
        raise NotImplementedError

class SeeOverview:
    def __init__(self):
        raise NotImplementedError

class SeePreference:
    def __init__(self):
        raise NotImplementedError

class SeeSeat:
    def __init__(self):
        raise NotImplementedError

class SeeType:
    def __init__(self):
        raise NotImplementedError

class SellTicket:
    def __init__(self):
        raise NotImplementedError

class SortSearchResult:
    def __init__(self):
        raise NotImplementedError

class ValidateTicket:
    def __init__(self):
        raise NotImplementedError