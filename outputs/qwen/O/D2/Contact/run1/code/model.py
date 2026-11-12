class Contact:
    def __init__(self, name):
        self.name = name
    def set_name(self, new_name):
        raise NotImplementedError

class CellPhoneNumber:
    def __init__(self, number):
        self.number = number
    def get_number(self):
        raise NotImplementedError