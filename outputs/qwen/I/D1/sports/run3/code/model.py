from typing import TypedDict, List, Optional

class Gym:
    def __init__(self):
        pass

class Customer(TypedDict):
    personal_info: dict
    banking_details: dict
    membership_type: str
    subscription: Optional[Subscription]
    notifications: List[str]
    def open_account(self):
        raise NotImplementedError
    def add_information(self, info: dict):
        raise NotImplementedError
    def add_banking_detail(self, details: dict):
        raise NotImplementedError
    def choose_membership_type(self, type: str):
        raise NotImplementedError
    def extend_subscription(self):
        raise NotImplementedError
    def unsubscribe(self):
        raise NotImplementedError
    def reset_password(self):
        raise NotImplementedError
    def change_details(self, details: dict):
        raise NotImplementedError
    def update_payment_information(self, details: dict):
        raise NotImplementedError
    def see_overview(self):
        raise NotImplementedError
    def see_record(self):
        raise NotImplementedError
    def see_future_lessons(self):
        raise NotImplementedError
    def call_gym(self, action: str):
        raise NotImplementedError
    def check_in(self):
        raise NotImplementedError
    def see_personal_info(self):
        raise NotImplementedError
    def see_membership(self):
        raise NotImplementedError
    def see_subscriptions(self):
        raise NotImplementedError

class FamilyMembership(Customer):
    def add_person(self, person: Person):
        raise NotImplementedError
    def remove_person(self, person: Person):
        raise NotImplementedError

class Trainer(TypedDict):
    lessons: List[Lesson]
    def see_schedule(self):
        raise NotImplementedError
    def add_lesson(self, lesson: Lesson):
        raise NotImplementedError
    def set_lesson_time(self, lesson: Lesson, time: str):
        raise NotImplementedError
    def set_lesson_room(self, lesson: Lesson, room: Room):
        raise NotImplementedError
    def set_lesson_description(self, lesson: Lesson, description: str):
        raise NotImplementedError
    def set_lesson_type(self, lesson: Lesson, lesson_type: str):
        raise NotImplementedError
    def set_lesson_number(self, lesson: Lesson, number: int):
        raise NotImplementedError
    def edit_lesson(self, lesson: Lesson):
        raise NotImplementedError
    def cancel_lesson(self, lesson: Lesson):
        raise NotImplementedError

class Admin(TypedDict):
    def edit_any_lesson(self, lesson: Lesson):
        raise NotImplementedError
    def add_trainer(self, trainer: Trainer):
        raise NotImplementedError
    def add_admin(self, admin: Admin):
        raise NotImplementedError
    def remove_trainer(self, trainer: Trainer):
        raise NotImplementedError
    def see_unattended_sessions(self):
        raise NotImplementedError
    def issue_fine(self, customer: Customer):
        raise NotImplementedError

class Lesson(TypedDict):
    description: str
    record: List[str]
    def set_description(self, description: str):
        raise NotImplementedError
    def set_room(self, room: Room):
        raise NotImplementedError
    def set_time(self, time: str):
        raise NotImplementedError
    def set_type(self, lesson_type: str):
        raise NotImplementedError
    def set_number(self, number: int):
        raise NotImplementedError

class Room(TypedDict):
    def is_free(self, time: str):
        raise NotImplementedError

class Subscription(TypedDict):
    def get_duration(self):
        raise NotImplementedError

class Notification(TypedDict):
    def send_email(self, message: str):
        raise NotImplementedError
    def send_push_notification(self, message: str):
        raise NotImplementedError
