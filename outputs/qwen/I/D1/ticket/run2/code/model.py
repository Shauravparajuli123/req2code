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
    artist: Artist
    description: str
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
    service_fee: ServiceFee
    resellers: List[Reseller]
    search_engine: Platform
    validation_process: Process


class Event:
    def __init__(self, name: str, date: Date, venue: Venue, artist: Artist, description: str, genre: str, types: List[str]):
        self.name = name
        self.date = date
        self.venue = venue
        self.artist = artist
        self.description = description
        self.genre = genre
        self.types = types


class EventPage:
    def __init__(self, event: Event, artist_links: List[Link]):
        self.event = event
        self.artist_links = artist_links


class Fan:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Guest:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Link:
    def __init__(self, url: str, platform: str):
        self.url = url
        self.platform = platform


class Platform:
    def __init__(self, name: str, failure: bool):
        self.name = name
        self.failure = failure


class Preference:
    def __init__(self, music_genre: str, event_types: List[str]):
        self.music_genre = music_genre
        self.event_types = event_types


class Process:
    def __init__(self, steps: List[str]):
        self.steps = steps


class Reseller:
    def __init__(self, name: str, bank_account: BankAccount):
        self.name = name
        self.bank_account = bank_account


class ResellingProcess:
    def __init__(self, tickets: List[Ticket], price: float, description: str):
        self.tickets = tickets
        self.price = price
        self.description = description


class SearchResult:
    def __init__(self, events: List[Event]):
        self.events = events


class Seat:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column


class ServiceFee:
    def __init__(self, percentage: float):
        self.percentage = percentage


class Show:
    def __init__(self, name: str, date: Date, artist: Artist):
        self.name = name
        self.date = date
        self.artist = artist


class Ticket:
    def __init__(self, event: Event, type: str, seat: Seat):
        self.event = event
        self.type = type
        self.seat = seat


class User:
    def __init__(self, name: str, email: str, address: Address, preferences: Preference, profile: UserProfile, tickets: List[Ticket], favorites: List[Event]):
        self.name = name
        self.email = email
        self.address = address
        self.preferences = preferences
        self.profile = profile
        self.tickets = tickets
        self.favorites = favorites


class UserProfile:
    def __init__(self, name: str, email: str, address: Address, preferences: Preference, payment_details: PaymentDetails, history: List[Ticket]):
        self.name = name
        self.email = email
        self.address = address
        self.preferences = preferences
        self.payment_details = payment_details
        self.history = history


class Venue:
    def __init__(self, name: str, map: str):
        self.name = name
        self.map = map


class Visitor:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class PaymentDetails:
    def __init__(self, card_number: str, expiration_date: str, cvv: str):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv


class Company:
    def __init__(self, name: str, service_fee: ServiceFee, resellers: List[Reseller], search_engine: Platform, validation_process: Process):
        self.name = name
        self.service_fee = service_fee
        self.resellers = resellers
        self.search_engine = search_engine
        self.validation_process = validation_process
