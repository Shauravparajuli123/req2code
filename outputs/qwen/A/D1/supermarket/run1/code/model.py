"""Code skeleton generated from the shared model of D1/supermarket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None
    password: _t.Optional[str] = None
    pushNotificationsEnabled: _t.Optional[bool] = None
    fontSize: _t.Optional[int] = None
    contrast: _t.Optional[int] = None
    language: _t.Optional[str] = None
    newsletterSubscription: _t.Optional[bool] = None
    wishlist: _t.Optional[str] = None
    orderHistory: _t.Optional[str] = None
    loyaltyCard: _t.Optional[str] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Personal Account" (R1)."""
        raise NotImplementedError

    def subscribeToNewsletter(self) -> None:
        """Realizes UC2 "Subscribe To Newsletter" (R2)."""
        raise NotImplementedError

    def unsubscribeFromNewsletter(self) -> None:
        """Realizes UC3 "Unsubscribe From Newsletter" (R3)."""
        raise NotImplementedError

    def activatePushNotifications(self) -> None:
        """Realizes UC4 "Activate Push Notifications" (R4)."""
        raise NotImplementedError

    def deactivatePushNotifications(self) -> None:
        """Realizes UC5 "Deactivate Push Notifications" (R5)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC6 "Reset Password" (R6)."""
        raise NotImplementedError

    def changeFontSize(self) -> None:
        """Realizes UC7 "Change Font Size" (R7)."""
        raise NotImplementedError

    def changeContrast(self) -> None:
        """Realizes UC8 "Change Contrast" (R8)."""
        raise NotImplementedError

    def changeLanguage(self) -> None:
        """Realizes UC9 "Change Language" (R9)."""
        raise NotImplementedError

    def receiveProductSuggestions(self) -> None:
        """Realizes UC10 "Receive Product Suggestions" (R10)."""
        raise NotImplementedError

    def receivePersonalDiscount(self) -> None:
        """Realizes UC11 "Receive Personal Discount" (R11)."""
        raise NotImplementedError

    def receivePersonalDiscountNotifications(self) -> None:
        """Realizes UC12 "Receive Personal Discount Notifications" (R12)."""
        raise NotImplementedError

    def subscriptionBasedDeliveryService(self) -> None:
        """Realizes UC13 "Subscription Based Delivery Service" (R13)."""
        raise NotImplementedError

    def receiveRecipeSuggestions(self) -> None:
        """Realizes UC14 "Receive Recipe Suggestions" (R14)."""
        raise NotImplementedError

    def contactCustomerService(self) -> None:
        """Realizes UC15 "Contact Customer Service" (R15)."""
        raise NotImplementedError

    def scanProductsForShoppingList(self) -> None:
        """Realizes UC16 "Scan Products For Shopping List" (R16)."""
        raise NotImplementedError

    def addProductToWishlist(self) -> None:
        """Realizes UC17 "Add To Wishlist" (R17)."""
        raise NotImplementedError

    def searchForProduct(self) -> None:
        """Realizes UC18 "Search For Product" (R18)."""
        raise NotImplementedError

    def filterProductsByDietaryRestrictions(self) -> None:
        """Realizes UC19 "Filter Products By Dietary Restrictions" (R19)."""
        raise NotImplementedError

    def orderByPrice(self) -> None:
        """Realizes UC20 "Order By Price" (R20)."""
        raise NotImplementedError

    def orderByPopularity(self) -> None:
        """Realizes UC21 "Order By Popularity" (R21)."""
        raise NotImplementedError

    def receiveSaleNotifications(self) -> None:
        """Realizes UC22 "Receive Sale Notifications" (R22)."""
        raise NotImplementedError

    def scanBarcodeForProductInformation(self) -> None:
        """Realizes UC23 "Scan Barcode For Product Information" (R23)."""
        raise NotImplementedError

    def readProductInformation(self) -> None:
        """Realizes UC24 "Read Product Information" (R24)."""
        raise NotImplementedError

    def checkProductStock(self) -> None:
        """Realizes UC25 "Check Product Stock" (R25)."""
        raise NotImplementedError

    def receiveStockAvailabilityNotifications(self) -> None:
        """Realizes UC26 "Receive Stock Availability Notifications" (R26)."""
        raise NotImplementedError

    def findSoldOutProductInAnotherStore(self) -> None:
        """Realizes UC27 "Find Sold Out Product In Another Store" (R27)."""
        raise NotImplementedError

    def checkProductQuantityInStore(self) -> None:
        """Realizes UC28 "Check Product Quantity In Store" (R28)."""
        raise NotImplementedError

    def checkProductRestockDate(self) -> None:
        """Realizes UC29 "Check Product Restock Date" (R29)."""
        raise NotImplementedError

    def receiveRecipeIdeas(self) -> None:
        """Realizes UC30 "Receive Recipe Ideas" (R30)."""
        raise NotImplementedError

    def seeProductsUsedInRecipe(self) -> None:
        """Realizes UC31 "See Products Used In Recipe" (R31)."""
        raise NotImplementedError

    def purchaseProductsOnline(self) -> None:
        """Realizes UC32 "Purchase Products Online" (R32)."""
        raise NotImplementedError

    def haveGroceriesDelivered(self) -> None:
        """Realizes UC33 "Have Groceries Delivered" (R33)."""
        raise NotImplementedError

    def selectDeliveryDate(self) -> None:
        """Realizes UC34 "Select Delivery Date" (R34)."""
        raise NotImplementedError

    def selectDeliveryTimeSlot(self) -> None:
        """Realizes UC35 "Select Delivery Time Slot" (R35)."""
        raise NotImplementedError

    def useExpressDeliveryService(self) -> None:
        """Realizes UC36 "Use Express Delivery Service" (R36)."""
        raise NotImplementedError

    def placePreviousOrderAgain(self) -> None:
        """Realizes UC38 "Place Previous Order Again" (R38)."""
        raise NotImplementedError

    def addPreviousOrderToNewOrder(self) -> None:
        """Realizes UC39 "Add Previous Order To New Order" (R39)."""
        raise NotImplementedError

    def digitallyPayForDeliveredGroceries(self) -> None:
        """Realizes UC40 "Digitally Pay For Delivered Groceries" (R40)."""
        raise NotImplementedError

    def findProductLocationInStore(self) -> None:
        """Realizes UC41 "Find Product Location In Store" (R41)."""
        raise NotImplementedError

    def getNearestStoreRecommendation(self) -> None:
        """Realizes UC42 "Get Nearest Store Recommendation" (R42)."""
        raise NotImplementedError

    def changeDefaultStore(self) -> None:
        """Realizes UC43 "Change Default Store" (R43)."""
        raise NotImplementedError

    def linkExistingLoyaltyCard(self) -> None:
        """Realizes UC44 "Link Existing Loyalty Card" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R45, R46, R47, R48, R49, R50, R51"""

    def updateRecipes(self) -> None:
        """Realizes UC45 "Update Recipes" (R45)."""
        raise NotImplementedError

    def editProductDiscounts(self) -> None:
        """Realizes UC46 "Edit Product Discounts" (R46)."""
        raise NotImplementedError

    def confirmDeliveryTime(self) -> None:
        """Realizes UC47 "Confirm Delivery Time" (R47)."""
        raise NotImplementedError

    def notifyUnavailableProducts(self) -> None:
        """Realizes UC48 "Notify Of Unavailable Products" (R48)."""
        raise NotImplementedError

    def notifyDelayedDelivery(self) -> None:
        """Realizes UC49 "Notify Of Delayed Delivery" (R49)."""
        raise NotImplementedError

    def notifyCanceledDelivery(self) -> None:
        """Realizes UC50 "Notify Of Canceled Delivery" (R50)."""
        raise NotImplementedError

    def provideNewDeliveryTime(self) -> None:
        """Realizes UC51 "Provide New Delivery Time" (R51)."""
        raise NotImplementedError
