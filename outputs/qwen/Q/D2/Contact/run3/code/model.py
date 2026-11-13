from typing import List

class Contact:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phoneNumber = phone_number
        self.cell_phone_numbers: List[CellPhoneNumber] = []

    def mapPhoneNumber(self) -> None:
        raise NotImplementedError('mapPhoneNumber method needs implementation')

class CellPhoneNumber:
    def __init__(self, number: str):
        self.number = number