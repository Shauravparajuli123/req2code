from typing import List, String, Integer, Money, Date, Boolean, String, List, Recipe, Product, Discount, Anomaly, Customer, Employee, Delivery, Grocery, Item, Newsletter, Location

class Language:
    def __init__(self, name: String):
        self.name = name

class TextSize:
    def __init__(self, size: String):
        self.size = size

class TextContrast:
    def __init__(self, contrast: String):
        self.contrast = contrast

class Customer:
    def __init__(self, username: String, password: String, language: Language, pushNotifications: Boolean, size: TextSize, contrast: TextContrast, loyaltyCard: String):
        self.username = username
        self.password = password
        self.language = language
        self.pushNotifications = pushNotifications
        self.size = size
        self.contrast = contrast
        self.loyaltyCard = loyaltyCard

    def createAccount(self):
        raise NotImplementedError

    def signNewsletter(self):
        raise NotImplementedError

    def unsubscribeNewsletter(self):
        raise NotImplementedError

    def activatePushNotification(self):
        raise NotImplementedError

    def deactivatePushNotification(self):
        raise NotImplementedError

    def resetPassword(self):
        raise NotImplementedError

    def changeLanguage(self):
        raise NotImplementedError

    def changeSize(self):
        raise NotImplementedError

    def changeContrast(self):
        raise NotImplementedError

    def receiveSuggestion(self):
        raise NotImplementedError

    def receiveDiscount(self):
        raise NotImplementedError

    def linkLoyaltyCard(self):
        raise NotImplementedError

    def addProductToWishlist(self):
        raise NotImplementedError

    def searchProduct(self):
        raise NotImplementedError

    def filterProduct(self):
        raise NotImplementedError

    def readProductInformation(self):
        raise NotImplementedError

    def seeProduct(self):
        raise NotImplementedError

    def seeQuantity(self):
        raise NotImplementedError

    def selectDate(self):
        raise NotImplementedError

    def selectTimeSlot(self):
        raise NotImplementedError

    def scanBarcode(self):
        raise NotImplementedError

    def scanProduct(self):
        raise NotImplementedError

    def orderProduct(self):
        raise NotImplementedError

    def placeOrder(self):
        raise NotImplementedError

    def seeOrderHistory(self):
        raise NotImplementedError

    def changeSelection(self):
        raise NotImplementedError

    def addProductToOrder(self):
        raise NotImplementedError

    def payGrocery(self):
        raise NotImplementedError

    def contactCustomerService(self):
        raise NotImplementedError

class Employee:
    def __init__(self, username: String, password: String):
        self.username = username
        self.password = password

    def updateApplication(self):
        raise NotImplementedError

    def editDiscount(self):
        raise NotImplementedError

    def confirmDeliveryTime(self):
        raise NotImplementedError

    def notifyCustomer(self):
        raise NotImplementedError

    def notifyItem(self):
        raise NotImplementedError

    def contactCustomer(self):
        raise NotImplementedError

    def provideCustomer(self):
        raise NotImplementedError

class Product:
    def __init__(self, name: String, barcode: String, quantity: Integer, price: Money, dietaryRestrictions: String):
        self.name = name
        self.barcode = barcode
        self.quantity = quantity
        self.price = price
        self.dietaryRestrictions = dietaryRestrictions

    def scanBarcode(self):
        raise NotImplementedError

    def readProductInformation(self):
        raise NotImplementedError

class Delivery:
    def __init__(self, date: Date, timeSlot: String, status: String):
        self.date = date
        self.timeSlot = timeSlot
        self.status = status

    def confirmDeliveryTime(self):
        raise NotImplementedError

    def notifyCustomer(self):
        raise NotImplementedError

    def notifyItem(self):
        raise NotImplementedError

class Grocery:
    def __init__(self, items: List[Item], delivery: Delivery):
        self.items = items
        self.delivery = delivery

    def addProductToOrder(self):
        raise NotImplementedError

    def payGrocery(self):
        raise NotImplementedError

class Item:
    def __init__(self, product: Product, quantity: Integer):
        self.product = product
        self.quantity = quantity

class Newsletter:
    def __init__(self, customer: Customer, discounts: List[Discount], anomalies: List[Anomaly], personalDiscounts: List[Discount], suggestions: List[Product], recipes: List[Recipe], loyaltyCard: String):
        self.customer = customer
        self.discounts = discounts
        self.anomalies = anomalies
        self.personalDiscounts = personalDiscounts
        self.suggestions = suggestions
        self.recipes = recipes
        self.loyaltyCard = loyaltyCard

    def signNewsletter(self):
        raise NotImplementedError

    def unsubscribeNewsletter(self):
        raise NotImplementedError

    def notifyCustomer(self):
        raise NotImplementedError

    def notifyDiscount(self):
        raise NotImplementedError

    def provideRecipeIdea(self):
        raise NotImplementedError

class Discount:
    def __init__(self, product: Product, percentage: Integer):
        self.product = product
        self.percentage = percentage

class Anomaly:
    def __init__(self, product: Product, description: String):
        self.product = product
        self.description = description

class Recipe:
    def __init__(self, name: String, ingredients: List[Product], instructions: String):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def getRecipe(self):
        raise NotImplementedError

class Date:
    def __init__(self, day: Integer, month: Integer, year: Integer):
        self.day = day
        self.month = month
        self.year = year

class Location:
    def __init__(self, name: String, coordinates: String):
        self.name = name
        self.coordinates = coordinates