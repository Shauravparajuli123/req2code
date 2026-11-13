from typing import List, Double, String, Boolean, Date, Integer, DeliveryTime, Product, Order, Recipe, Discount, DeliveryService, Newsletter, Language, Location, Stock, Delivery

class Language:
    def __init__(self, languageCode: String):
        self.languageCode = languageCode

class DeliveryService:
    def __init__(self, serviceType: String):
        self.serviceType = serviceType

class DeliveryTime:
    def __init__(self, date: Date, timeSlot: String):
        self.date = date
        self.timeSlot = timeSlot

class Discount:
    def __init__(self, percentage: Double):
        self.percentage = percentage

class Product:
    def __init__(self, name: String, price: Double, quantity: Integer, barcode: String, dietaryRestrictions: String):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.barcode = barcode
        self.dietaryRestrictions = dietaryRestrictions

    def addProduct(self):
        raise NotImplementedError

    def changeSelection(self):
        raise NotImplementedError

class Order:
    def __init__(self, items: List[Product]):
        self.items = items

    def placeOrder(self):
        raise NotImplementedError

    def seeOrderHistory(self):
        raise NotImplementedError

class Recipe:
    def __init__(self, ingredients: List[Product]):
        self.ingredients = ingredients

    def getRecipe(self):
        raise NotImplementedError

    def getRecipeIdea(self):
        raise NotImplementedError

class Newsletter:
    def __init__(self):
        pass

    def signNewsletter(self):
        raise NotImplementedError

    def unsubscribeNewsletter(self):
        raise NotImplementedError

class Customer:
    def __init__(self, email: String, password: String, language: Language, pushNotifications: Boolean, deliveryService: DeliveryService, loyaltyCard: String):
        self.email = email
        self.password = password
        self.language = language
        self.pushNotifications = pushNotifications
        self.deliveryService = deliveryService
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

    def haveDeliveryService(self):
        raise NotImplementedError

    def haveGrocery(self):
        raise NotImplementedError

    def orderProduct(self):
        raise NotImplementedError

    def placeOrder(self):
        raise NotImplementedError

    def seeOrderHistory(self):
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

    def readProductInformation(self):
        raise NotImplementedError

    def searchProduct(self):
        raise NotImplementedError

    def filterProduct(self):
        raise NotImplementedError

    def findLocation(self):
        raise NotImplementedError

    def getRecommendation(self):
        raise NotImplementedError

    def getRecipe(self):
        raise NotImplementedError

    def linkLoyaltyCard(self):
        raise NotImplementedError

    def changeSelection(self):
        raise NotImplementedError

class Employee:
    def __init__(self, employeeID: String):
        self.employeeID = employeeID

    def updateApplication(self):
        raise NotImplementedError

    def editDiscount(self):
        raise NotImplementedError

    def confirmDeliveryTime(self):
        raise NotImplementedError

    def notifyCustomer(self):
        raise NotImplementedError

    def notifyDiscount(self):
        raise NotImplementedError

    def notifyItem(self):
        raise NotImplementedError

    def contactCustomer(self):
        raise NotImplementedError

    def provideCustomer(self):
        raise NotImplementedError

    def provideRecipeIdea(self):
        raise NotImplementedError