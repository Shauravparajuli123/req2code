from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
def log_in(self):
        pass

class Admin(User):
    def add_trainer(self):
        pass
    def add_admin(self):
        pass
    def remove_trainer(self):
        pass
    def see_if_customer_has_subscription(self):
        pass
    def see_if_customer_has_bookings(self):
        pass

class Customer(User):
    def open_account(self):
        pass
    def add_information(self):
        pass
    def add_banking_detail(self):
        pass
    def choose_membership_type(self):
        pass
    def extend_subscription(self):
        pass
    def unsubscribe(self):
        pass
    def reset_password(self):
        pass
    def change_detail(self):
        pass
    def update_payment_information(self):
        pass
    def see_overview(self):
        pass
    def see_information(self):
        pass
    def see_record(self):
        pass
    def see_future_bookings(self):
        pass
    def receive_notification(self):
        pass
    def confirm_booking(self):
        pass
    def check_in(self):
        pass

class Trainer(User):
    def add_lesson(self):
        pass
    def set_time(self):
        pass
    def set_description(self):
        pass
    def set_room(self):
        pass
    def set_type(self):
        pass
    def set_number(self):
        pass
    def see_schedule(self):
        pass
    def edit_lesson(self):
        pass
    def cancel_lesson(self):
        pass
    def change_room(self):
        pass
    def change_description(self):
        pass
    def change_number(self):
        pass
    def change_time(self):
        pass

class DailySports:
    def call_gym(self):
        pass

class Lesson:
    def __init__(self, description, record):
        self.description = description
        self.record = record
    def set_description(self, description):
        pass
    def set_record(self, record):
        pass

class Gym:
    def __init__(self, requirement):
        self.requirement = requirement

class FamilyMembership(Customer):
    def add_person(self):
        pass
    def remove_person(self):
        pass

class Fine:
    def __init__(self, times_missed):
        self.times_missed = times_missed
    def increase_fine(self):
        pass

class Notification:
    def __init__(self, method):
        self.method = method
    def send_notification(self):
        pass

class Method:
    def __init__(self, method):
        self.method = method

class NotificationMethod(Method):
    def __init__(self, method):
        super().__init__(method)

class NotificationEmail(NotificationMethod):
    def send_email(self):
        pass

class NotificationPush(NotificationMethod):
    def send_push(self):
        pass

class NotificationSubscription(Notification):
    def __init__(self, subscription):
        super().__init__(subscription)

class NotificationBookingCancellation(NotificationSubscription):
    def send_cancellation_notification(self):
        pass

class NotificationNoShow(NotificationSubscription):
    def send_no_show_notification(self):
        pass

class NotificationAdmin(Notification):
    def __init__(self, admin):
        super().__init__(admin)

class NotificationCustomer(NotificationAdmin):
    def notify_customer(self):
        pass

class NotificationAdminCustomer(NotificationAdmin):
    def notify_customer(self):
        pass

class NotificationAdminSubscription(NotificationAdmin):
    def notify_customer(self):
        pass

class NotificationAdminNoShow(NotificationAdminSubscription):
    def notify_customer(self):
        pass

class NotificationAdminFine(NotificationAdminSubscription):
    def notify_customer(self):
        pass

class NotificationAdminFineIncrease(NotificationAdminFine):
    def notify_customer(self):
        pass
