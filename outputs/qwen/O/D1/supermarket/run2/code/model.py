class Customer:
    def __init__(self, email, password, language, pushNotification, fontSize, contrast, defaultStore):
        self.email = email
        self.password = password
        self.language = language
        self.pushNotification = pushNotification
        self.fontSize = fontSize
        self.contrast = contrast
        self.defaultStore = defaultStore

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

    def placeOrder(self):
        raise NotImplementedError

    def seeProduct(self):
        raise NotImplementedError

    def seeQuantity(self):
        raise NotImplementedError

    def seeLocation(self):
        raise NotImplementedError

    def getRecommendation(self):
        raise NotImplementedError

    def changeSelection(self):
        raise NotImplementedError

    def linkLoyaltyCard(self):
        raise NotImplementedError


class Employee:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

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


class Product:
    def __init__(self, name, barcode, quantity, dietaryRestrictions, price):
        self.name = name
        self.barcode = barcode
        self.quantity = quantity
        self.dietaryRestrictions = dietaryRestrictions
        self.price = price

    def scanBarcode(self):
        raise NotImplementedError

    def readProductInformation(self):
        raise NotImplementedError

    def seeIfInStock(self):
        raise NotImplementedError

    def seeWhenAvailableAgain(self):
        raise NotImplementedError

    def seeUsedInRecipe(self):
        raise NotImplementedError


class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def findLocation(self):
        raise NotImplementedError

    def getRecommendation(self):
        raise NotImplementedError


class Delivery:
    def __init__(self, date, timeSlot, status):
        self.date = date
        self.timeSlot = timeSlot
        self.status = status

    def selectDate(self):
        raise NotImplementedError

    def selectTimeSlot(self):
        raise NotImplementedError

    def confirmDeliveryTime(self):
        raise NotImplementedError

    def notifyCustomer(self):
        raise NotImplementedError

    def notifyDiscount(self):
        raise NotImplementedError

    def notifyItem(self):
        raise NotImplementedError


class Order:
    def __init__(self, date, timeSlot, status, products):
        self.date = date
        self.timeSlot = timeSlot
        self.status = status
        self.products = products

    def placeOrder(self):
        raise NotImplementedError

    def seeOrderHistory(self):
        raise NotImplementedError


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def provideRecipeIdea(self):
        raise NotImplementedError


class Discount:
    def __init__(self, product, discountAmount):
        self.product = product
        self.discountAmount = discountAmount

    def editDiscount(self):
        raise NotImplementedError