from typing import Dict

class CellPhoneNumber(str):
    pass

class Contact:
    def __init__(self, name: str, cell_phone_number: CellPhoneNumber):
        self.name = name
        self.cell_phone_number = cell_phone_number
        self.land_line_number: str = ''

    def set_land_line_number(self, land_line_number: str) -> None:
        raise NotImplementedError

    def get_land_line_number(self) -> str:
        raise NotImplementedError

    def set_cell_phone_number(self, cell_phone_number: CellPhoneNumber) -> None:
        raise NotImplementedError

    def get_cell_phone_number(self) -> CellPhoneNumber:
        raise NotImplementedError