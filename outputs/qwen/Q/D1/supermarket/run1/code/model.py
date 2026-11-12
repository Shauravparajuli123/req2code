from typing import List, Optional, Date, Money, String, Integer, Boolean

class Language:
    pass

class DeliveryService:
    def __init__(self, subscription: Boolean):
        self.subscription = subscription

class Delivery:
    def __init__(self, date: Date, timeSlot: String, status: String):
        self.date = date
        self.timeSlot = timeSlot
        self.status = status
    def confirmDeliveryTime(self, use_case: 'Confirm DeliveryTime') -> None:
        raise NotImplementedError

class Newsletter:
    def __init__(self, subscriptionStatus: Boolean):
        self.subscriptionStatus = subscriptionStatus
    def signNewsletter(self, use_case: 'Sign Newsletter') -> None:
        raise NotImplementedError
    def unsubscribeNewsletter(self, use_case: 'Unsubscribe Newsletter') -> None:
        raise NotImplementedError

class Discount:
    def __init__(self, percentage: Integer):
        self.percentage = percentage
    def editDiscount(self, use_case: 'Edit Discount') -> None:
        raise NotImplementedError

class Product:
    def __init__(self, name: String, barcode: String, quantity: Integer, price: Money, dietaryRestrictions: String):
        self.name = name
        self.barcode = barcode
        self.quantity = quantity
        self.price = price
        self.dietaryRestrictions = dietaryRestrictions
    def searchProduct(self, use_case: 'Search Product') -> None:
        raise NotImplementedError
    def filterProduct(self, use_case: 'Filter Product') -> None:
        raise NotImplementedError
    def scanBarcode(self, use_case: 'Scan Barcode') -> None:
        raise NotImplementedError
    def readProductInformation(self, use_case: 'Read ProductInformation') -> None:
        raise NotImplementedError

class Order:
    def __init__(self, date: Date, timeSlot: String, status: String, products: List[Product]):
        self.date = date
        self.timeSlot = timeSlot
        self.status = status
        self.products = products
    def placeOrder(self, use_case: 'Place Order') -> None:
        raise NotImplementedError
    def addProductToOrder(self, use_case: 'Add Product') -> None:
        raise NotImplementedError
    def changeSelection(self, use_case: 'Change Selection') -> None:
        raise NotImplementedError

class Recipe:
    def __init__(self, name: String, ingredients: List[Product]):
        self.name = name
        self.ingredients = ingredients
    def getRecipe(self, use_case: 'Get Recipe') -> None:
        raise NotImplementedError
    def getRecommendation(self, use_case: 'Get Recommendation') -> None:
        raise NotImplementedError

class LoyaltyCard:
    def __init__(self, cardNumber: String, points: Integer):
        self.cardNumber = cardNumber
        self.points = points
    def linkLoyaltyCard(self, use_case: 'Link LoyaltyCard') -> None:
        raise NotImplementedError

class Customer:
    def __init__(self, username: String, password: String, language: Language, pushNotifications: Boolean, deliveryService: Optional[DeliveryService], loyaltyCard: Optional[LoyaltyCard]):
        self.username = username
        self.password = password
        self.language = language
        self.pushNotifications = pushNotifications
        self.deliveryService = deliveryService
        self.loyaltyCard = loyaltyCard
    def createAccount(self, use_case: 'Create Account') -> None:
        raise NotImplementedError
    def signNewsletter(self, use_case: 'Sign Newsletter') -> None:
        raise NotImplementedError
    def unsubscribeNewsletter(self, use_case: 'Unsubscribe Newsletter') -> None:
        raise NotImplementedError
    def activatePushNotification(self, use_case: 'Activate PushNotification') -> None:
        raise NotImplementedError
    def deactivatePushNotification(self, use_case: 'Deactivate PushNotification') -> None:
        raise NotImplementedError
    def resetPassword(self, use_case: 'Reset Password') -> None:
        raise NotImplementedError
    def changeLanguage(self, use_case: 'Change Language') -> None:
        raise NotImplementedError
    def changeSize(self, use_case: 'Change Size') -> None:
        raise NotImplementedError
    def changeContrast(self, use_case: 'Change Contrast') -> None:
        raise NotImplementedError
    def receiveSuggestion(self, use_case: 'Receive Suggestion') -> None:
        raise NotImplementedError
    def receiveDiscount(self, use_case: 'Receive Discount') -> None:
        raise NotImplementedError
    def orderProduct(self, use_case: 'Order Product') -> None:
        raise NotImplementedError
    def payGrocery(self, use_case: 'Pay Grocery') -> None:
        raise NotImplementedError
    def placeOrder(self, use_case: 'Place Order') -> None:
        raise NotImplementedError
    def seeOrderHistory(self, use_case: 'See OrderHistory') -> None:
        raise NotImplementedError
    def seeProduct(self, use_case: 'See Product') -> None:
        raise NotImplementedError
    def seeQuantity(self, use_case: 'See Quantity') -> None:
        raise NotImplementedError
    def selectDate(self, use_case: 'Select Date') -> None:
        raise NotImplementedError
    def selectTimeSlot(self, use_case: 'Select TimeSlot') -> None:
        raise NotImplementedError
    def scanBarcode(self, use_case: 'Scan Barcode') -> None:
        raise NotImplementedError
    def readProductInformation(self, use_case: 'Read ProductInformation') -> None:
        raise NotImplementedError
    def searchProduct(self, use_case: 'Search Product') -> None:
        raise NotImplementedError
    def filterProduct(self, use_case: 'Filter Product') -> None:
        raise NotImplementedError
    def findLocation(self, use_case: 'Find Location') -> None:
        raise NotImplementedError
    def getRecommendation(self, use_case: 'Get Recommendation') -> None:
        raise NotImplementedError
    def linkLoyaltyCard(self, use_case: 'Link LoyaltyCard') -> None:
        raise NotImplementedError
    def addProductToWishlist(self, use_case: 'Add Product') -> None:
        raise NotImplementedError
    def changeSelection(self, use_case: 'Change Selection') -> None:
        raise NotImplementedError

class Employee:
    def __init__(self, username: String, password: String):
        self.username = username
        self.password = password
    def updateApplication(self, use_case: 'Update Application') -> None:
        raise NotImplementedError
    def editDiscount(self, use_case: 'Edit Discount') -> None:
        raise NotImplementedError
    def confirmDeliveryTime(self, use_case: 'Confirm DeliveryTime') -> None:
        raise NotImplementedError
    def notifyCustomer(self, use_case: 'Notify Customer') -> None:
        raise NotImplementedError
    def notifyDiscount(self, use_case: 'Notify Discount') -> None:
        raise NotImplementedError
    def notifyItem(self, use_case: 'Notify Item') -> None:
        raise NotImplementedError
    def contactCustomer(self, use_case: 'Contact Customer') -> None:
        raise NotImplementedError
    def provideCustomer(self, use_case: 'Provide Customer') -> None:
        raise NotImplementedError
    def provideRecipeIdea(self, use_case: 'Provide RecipeIdea') -> None:
        raise NotImplementedError