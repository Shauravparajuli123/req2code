from typing import List, Optional, Union

class Cent:
    pass

class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Preference:
    def __init__(self, genre: str, event_types: List[str]):
        self.genre = genre
        self.event_types = event_types

class BankAccount:
    def __init__(self, iban: str):
        self.iban = iban

class Ticket:
    def __init__(self, type: str, price: Cent):
        self.type = type
        self.price = price

class Event:
    def __init__(self, name: str, date: str, artist: str, venue: str, tickets: List[Ticket]):
        self.name = name
        self.date = date
        self.artist = artist
        self.venue = venue
        self.tickets = tickets

class Artist:
    def __init__(self, name: str, upcoming_events: List[str], links: List[str]):
        self.name = name
        self.upcoming_events = upcoming_events
        self.links = links

class Venue:
    def __init__(self, map: str):
        self.map = map

class User:
    def __init__(self, name: str, date_of_birth: str, email: str, address: Address, preferences: Preference, personal_information: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.address = address
        self.preferences = preferences
        self.personal_information = personal_information
    def fill_information(self):
        raise NotImplementedError
    def save_information(self):
        raise NotImplementedError
    def edit_information(self):
        raise NotImplementedError
    def change_password(self):
        raise NotImplementedError
    def see_content(self):
        raise NotImplementedError
    def see_preference(self):
        raise NotImplementedError
    def see_history(self):
        raise NotImplementedError
    def see_overview(self):
        raise NotImplementedError
    def favorite_event(self):
        raise NotImplementedError
    def filter_list(self):
        raise NotImplementedError
    def filter_search(self):
        raise NotImplementedError
    def sort_search_result(self):
        raise NotImplementedError

class Visitor:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    def read_event(self):
        raise NotImplementedError
    def see_event(self):
        raise NotImplementedError
    def purchase_ticket(self):
        raise NotImplementedError
    def see_available_seats(self):
        raise NotImplementedError
    def see_ticket_types(self):
        raise NotImplementedError
    def add_ticket_to_cart(self):
        raise NotImplementedError
    def see_order_summary(self):
        raise NotImplementedError
    def filter_search(self):
        raise NotImplementedError
    def sort_search_result(self):
        raise NotImplementedError
    def click_event(self):
        raise NotImplementedError
    def land_event_page(self):
        raise NotImplementedError
    def see_available_events(self):
        raise NotImplementedError

class Reseller:
    def __init__(self, bank_account: BankAccount, events: List[Event]):
        self.bank_account = bank_account
        self.events = events
    def resell_ticket(self):
        raise NotImplementedError
    def upload_ticket(self):
        raise NotImplementedError
    def set_ticket_price(self):
        raise NotImplementedError
    def set_ticket_description(self):
        raise NotImplementedError
    def save_bank_account(self):
        raise NotImplementedError

class Company:
    def __init__(self, buying_process: str, resellers: List[Reseller]):
        self.buying_process = buying_process
        self.resellers = resellers
    def have_buying_process(self):
        raise NotImplementedError
    def have_reseller(self):
        raise NotImplementedError
    def validate_ticket(self):
        raise NotImplementedError
    def deduct_service_fee(self):
        raise NotImplementedError

class UserProfile:
    pass

class Process:
    pass

class Link:
    def __init__(self, url: str):
        self.url = url