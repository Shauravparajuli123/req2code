from abc import ABC, abstractmethod

class Customer:
    def __init__(self, id: int):
        self.id = id
        self.push_notifications = True
        self.password = None
        self.default_store = None
        self.language = 'en'
        self.text_size = 12
        self.newsletter_subscription = True
        self.password_reset_token = None

    def activate_push_notifications(self):
        self.push_notifications = True
        raise NotImplementedError

    def deactivate_push_notifications(self):
        self.push_notifications = False
        raise NotImplementedError

    def reset_password(self):
        raise NotImplementedError

    def change_text_size(self, size: int):
        self.text_size = size
        raise NotImplementedError

    def change_language(self, language: str):
        self.language = language
        raise NotImplementedError

    def sign_up_for_newsletter(self):
        self.newsletter_subscription = True
        raise NotImplementedError

    def unsubscribe_from_newsletter(self):
        self.newsletter_subscription = False
        raise NotImplementedError

    def create_account(self):
        raise NotImplementedError

    def add_product_to_wishlist(self, product_id: int):
        raise NotImplementedError

    def search_product(self, product_name: str):
        raise NotImplementedError

    def filter_products_by_dietary_restrictions(self, restrictions: list):
        raise NotImplementedError

    def order_product_by_price(self, ascending: bool):
        raise NotImplementedError

    def order_product_by_popularity(self):
        raise NotImplementedError

    def check_product_stock(self, product_id: int):
        raise NotImplementedError

    def get_product_information(self, product_id: int):
        raise NotImplementedError

    def scan_product(self, barcode: str):
        raise NotImplementedError

    def purchase_product(self, product_id: int):
        raise NotImplementedError

    def place_order(self, products: list):
        raise NotImplementedError

    def see_order_history(self):
        raise NotImplementedError

    def see_product(self, product_id: int):
        raise NotImplementedError

    def see_quantity(self, product_id: int):
        raise NotImplementedError

    def select_date(self, date: str):
        raise NotImplementedError

    def select_time_slot(self, time_slot: str):
        raise NotImplementedError

    def have_delivery_service(self, service_type: str):
        raise NotImplementedError

    def digitally_pay_for_groceries(self, amount: float):
        raise NotImplementedError

    def contact_customer_service(self):
        raise NotImplementedError

    def see_product_location(self, product_id: int):
        raise NotImplementedError

    def get_recipe(self, recipe_id: int):
        raise NotImplementedError

    def get_recommendation(self, store_id: int):
        raise NotImplementedError

    def change_default_store(self, store_id: int):
        self.default_store = store_id
        raise NotImplementedError

    def link_loyalty_card(self, card_id: int):
        raise NotImplementedError

    def receive_discount(self, product_id: int):
        raise NotImplementedError

    def receive_suggestion(self, product_id: int):
        raise NotImplementedError

    def see_product_on_sale(self):
        raise NotImplementedError

    def see_special_personal_discount(self, product_id: int):
        raise NotImplementedError

    def see_item_back_in_stock(self, product_id: int):
        raise NotImplementedError

    def see_product_in_other_store(self, product_id: int):
        raise NotImplementedError

    def see_order_delivery_time(self, order_id: int):
        raise NotImplementedError

    def provide_customer_with_new_delivery_time(self, order_id: int, new_time: str):
        raise NotImplementedError

    def provide_customer_with_recipe_idea(self, recipe_id: int):
        raise NotImplementedError

    def update_application_with_new_recipes(self, recipes: list):
        raise NotImplementedError

    def edit_discount_for_product(self, product_id: int, discount: float):
        raise NotImplementedError

    def confirm_delivery_time(self, order_id: int, delivery_time: str):
        raise NotImplementedError

    def notify_customer_of_unavailable_product(self, order_id: int, product_id: int):
        raise NotImplementedError

    def notify_customer_of_delayed_delivery(self, order_id: int, delay_reason: str):
        raise NotImplementedError

    def notify_customer_of_canceled_delivery(self, order_id: int):
        raise NotImplementedError

    def notify_customer_of_new_delivery_time(self, order_id: int, new_time: str):
        raise NotImplementedError
