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
    def __init__(self):
        pass

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
class Account:
    def __init__(self):
        pass

    def createAccount(self):
        raise NotImplementedError
class PushNotification:
    def __init__(self, activated):
        self.activated = activated

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
    def __init__(self):
        pass

    def linkLoyaltyCard(self):
        raise NotImplementedError