from typing import TypedDict, List, Optional

class Admin:
    def edit_any_lesson(self, lesson: Lesson):
        raise NotImplementedError

class Customer:
    def open_account(self):
        raise NotImplementedError
    def add_information(self):
        raise NotImplementedError
    def add_banking_detail(self):
        raise NotImplementedError
    def choose_membership_type(self):
        raise NotImplementedError
    def extend_subscription(self):
        raise NotImplementedError
    def unsubscribe(self):
        raise NotImplementedError
    def reset_password(self):
        raise NotImplementedError
    def change_detail(self):
        raise NotImplementedError
    def update_payment_information(self):
        raise NotImplementedError
    def see_overview(self):
        raise NotImplementedError
    def see_record(self):
        raise NotImplementedError
    def see_information(self):
        raise NotImplementedError
    def see_membership(self):
        raise NotImplementedError
    def see_lesson(self):
        raise NotImplementedError
    def see_spot(self):
        raise NotImplementedError
    def call_gym(self, action: str):
        raise NotImplementedError
    def check_in(self):
        raise NotImplementedError
    def receive_notification(self, method: str, event: str):
        raise NotImplementedError

class CustomerWithFamilyMembership(Customer):
    def add_person(self):
        raise NotImplementedError
    def remove_person(self):
        raise NotImplementedError

class Trainer:
    def add_lesson(self):
        raise NotImplementedError
    def set_time(self):
        raise NotImplementedError
    def set_description(self):
        raise NotImplementedError
    def set_room(self):
        raise NotImplementedError
    def set_type(self):
        raise NotImplementedError
    def set_number(self):
        raise NotImplementedError
    def see_schedule(self):
        raise NotImplementedError
    def edit_lesson(self):
        raise NotImplementedError
    def change_room(self):
        raise NotImplementedError
    def change_description(self):
        raise NotImplementedError
    def change_number(self):
        raise NotImplementedError
    def change_time(self):
        raise NotImplementedError
    def cancel_lesson(self):
        raise NotImplementedError

class Gym:
    def see_free_rooms(self, timeslot: Timeslot):
        raise NotImplementedError

class Lesson:
    def __init__(self, description: str, record: str):
        self.description: str = description
        self.record: str = record

class Membership:
    def __init__(self, type: str):
        self.type: str = type

class Method(TypedDict):
    pass

class Notification(TypedDict):
    pass

class People:
    def __init__(self, name: str):
        self.name: str = name

class Person(People):
    pass

class Room:
    def __init__(self, name: str):
        self.name: str = name

class Schedule:
    def __init__(self, lessons: List[Lesson]):
        self.lessons: List[Lesson] = lessons

class Subscription:
    def __init__(self, type: str):
        self.type: str = type

class Timeslot:
    def __init__(self, start_time: str, end_time: str):
        self.start_time: str = start_time
        self.end_time: str = end_time

class TrainingSession(Lesson):
    def __init__(self, description: str, record: str):
        super().__init__(description, record)
