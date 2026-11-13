class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def createAccount(self):
        raise NotImplementedError


class PushNotification:
    def __init__(self, status):
        self.status = status

    def activatePushNotification(self):
        raise NotImplementedError

    def deactivatePushNotification(self):
        raise NotImplementedError


class Language:
    def __init__(self, language):
        self.language = language

    def changeLanguage(self):
        raise NotImplementedError


class Text:
    def __init__(self, size, contrast):
        self.size = size
        self.contrast = contrast

    def changeSize(self):
        raise NotImplementedError

    def changeContrast(self):
        raise NotImplementedError


class LoyaltyCard:
    def __init__(self, cardNumber):
        self.cardNumber = cardNumber

    def linkLoyaltyCard(self):
        raise NotImplementedError


class Customer:
    def __init__(self, account, pushNotification, language, size, contrast, loyaltyCard):
        self.account = account
        self.pushNotification = pushNotification
        self.language = language
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

    def changeSize(self):
        raise NotImplementedError

    def changeContrast(self):
        raise NotImplementedError

    def changeLanguage(self):
        raise NotImplementedError

    def receiveSuggestion(self):
        raise NotImplementedError

    def receiveDiscount(self):
        raise NotImplementedError

    def haveDeliveryService(self):
        raise NotImplementedError

    def getRecipe(self):
        raise NotImplementedError

    def contactCustomerService(self):
        raise NotImplementedError

    def scanProduct(self):
        raise NotImplementedError

    def addProduct(self):
        raise NotImplementedError

    def searchProduct(self):
        raise NotImplementedError

    def filterProduct(self):
        raise NotImplementedError

    def orderProduct(self):
        raise NotImplementedError

    def payGrocery(self):
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

    def haveGrocery(self):
        raise NotImplementedError

    def linkLoyaltyCard(self):
        raise NotImplementedError


class Employee:
    def __init__(self, application):
        self.application = application

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


class Application:
    def __init__(self, recipes, discounts, deliveryTimes, products, stores):
        self.recipes = recipes
        self.discounts = discounts
        self.deliveryTimes = deliveryTimes
        self.products = products
        self.stores = stores

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


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def getRecipe(self):
        raise NotImplementedError


class Discount:
    def __init__(self, product, discountAmount):
        self.product = product
        self.discountAmount = discountAmount

    def editDiscount(self):
        raise NotImplementedError


class DeliveryTime:
    def __init__(self, time):
        self.time = time

    def confirmDeliveryTime(self):
        raise NotImplementedError

    def notifyCustomer(self):
        raise NotImplementedError

    def notifyDiscount(self):
        raise NotImplementedError

    def notifyItem(self):
        raise NotImplementedError


class Product:
    def __init__(self, name, quantity, price, dietaryRestrictions):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.dietaryRestrictions = dietaryRestrictions

    def orderProduct(self):
        raise NotImplementedError

    def seeQuantity(self):
        raise NotImplementedError

    def filterProduct(self):
        raise NotImplementedError


class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def findLocation(self):
        raise NotImplementedError

    def getRecommendation(self):
        raise NotImplementedError

    def changeSelection(self):
        raise NotImplementedError


class Location:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def findLocation(self):
        raise NotImplementedError

    def getRecommendation(self):
        raise NotImplementedError

    def changeSelection(self):
        raise NotImplementedError
