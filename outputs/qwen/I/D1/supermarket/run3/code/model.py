from abc import ABC, abstractmethod

class Customer:
    def __init__(self, id: str):
        self.id = id
        self.push_notifications = True
        self.password = None
        self.language = 'en'
        self.font_size = 12
        self.default_store = None
        self.loyalty_card = None
        self.newsletter_subscription = True

    def activate_push_notifications(self):
        self.push_notifications = True
        raise NotImplementedError

    def deactivate_push_notifications(self):
        self.push_notifications = False
        raise NotImplementedError

    def reset_password(self):
        raise NotImplementedError

    def change_font_size(self, size: int):
        self.font_size = size
        raise NotImplementedError

    def change_language(self, language: str):
        self.language = language
        raise NotImplementedError

    def change_selection(self, store: Store):
        self.default_store = store
        raise NotImplementedError

    def link_loyalty_card(self, card: str):
        self.loyalty_card = card
        raise NotImplementedError

    def create_account(self):
        raise NotImplementedError

    def sign_up_for_newsletter(self):
        self.newsletter_subscription = True
        raise NotImplementedError

    def unsubscribe_from_newsletter(self):
        self.newsletter_subscription = False
        raise NotImplementedError

    def change_contrast(self, contrast: int):
        raise NotImplementedError

    def change_product_font_size(self, product: Product, size: int):
        raise NotImplementedError

    def change_product_language(self, product: Product, language: str):
        raise NotImplementedError

    def change_product_contrast(self, product: Product, contrast: int):
        raise NotImplementedError

    def receive_discount(self, discount: Discount):
        raise NotImplementedError

    def receive_suggestion(self, suggestion: str):
        raise NotImplementedError

    def search_product(self, product_name: str):
        raise NotImplementedError

    def filter_products(self, dietary_restrictions: list):
        raise NotImplementedError

    def order_product_by_price(self, ascending: bool):
        raise NotImplementedError

    def order_product_by_popularity(self):
        raise NotImplementedError

    def see_product_on_sale(self):
        raise NotImplementedError

    def scan_barcode(self, barcode: str):
        raise NotImplementedError

    def read_product_information(self, product: Product):
        raise NotImplementedError

    def see_if_product_in_stock(self, product: Product):
        raise NotImplementedError

    def see_when_product_back_in_stock(self, product: Product):
        raise NotImplementedError

    def see_product_location(self, product: Product):
        raise NotImplementedError

    def get_recipe(self, recipe: Recipe):
        raise NotImplementedError

    def see_recipe_ingredients(self, recipe: Recipe):
        raise NotImplementedError

    def purchase_product(self, product: Product):
        raise NotImplementedError

    def place_order(self, products: list):
        raise NotImplementedError

    def add_to_wishlist(self, product: Product):
        raise NotImplementedError

    def see_order_history(self):
        raise NotImplementedError

    def place_previous_order(self):
        raise NotImplementedError

    def add_from_previous_order(self, product: Product):
        raise NotImplementedError

    def pay_grocery(self, amount: Money):
        raise NotImplementedError

    def see_quantity_in_store(self, product: Product):
        raise NotImplementedError

    def select_delivery_date(self, date: Date):
        raise NotImplementedError

    def select_delivery_time_slot(self, time_slot: TimeSlot):
        raise NotImplementedError

    def use_express_delivery(self):
        raise NotImplementedError

    def see_delivery_time(self, delivery: Delivery):
        raise NotImplementedError

    def contact_customer_service(self):
        raise NotImplementedError

    def scan_product_in_store(self, product: Product):
        raise NotImplementedError

    def see_order_status(self, order: Order):
        raise NotImplementedError

    def see_store_recommendation(self):
        raise NotImplementedError

    def update_loyalty_card(self, card: str):
        self.loyalty_card = card
        raise NotImplementedError

    def update_application(self, recipe: Recipe):
        raise NotImplementedError

    def update_delivery_time(self, delivery_time: DeliveryTime):
        raise NotImplementedError

    def notify_customer_of_unavailable_product(self, product: Product):
        raise NotImplementedError

    def notify_customer_of_delayed_delivery(self, delivery: Delivery):
        raise NotImplementedError

    def notify_customer_of_canceled_delivery(self, delivery: Delivery):
        raise NotImplementedError

    def provide_new_delivery_time(self, delivery: Delivery, new_time: DeliveryTime):
        raise NotImplementedError

