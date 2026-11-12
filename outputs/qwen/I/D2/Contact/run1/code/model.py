from typing import Dict

class CellPhoneNumber(str):
    pass

class Contact:
    def __init__(self, name: str, cell_phone_number: CellPhoneNumber = None):
        self.name = name
        self.cell_phone_number = cell_phone_number
        self.land_line_numbers: Dict[str, Contact] = {}

def add_land_line_number(contact: Contact, land_line_number: str) -> None:
    raise NotImplementedError

def get_contact_by_land_line_number(land_line_number: str) -> Contact:
    raise NotImplementedError