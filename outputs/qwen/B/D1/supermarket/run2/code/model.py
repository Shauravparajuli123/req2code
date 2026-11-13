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
    language: _t.Optional[str] = None
    pushNotifications: _t.Optional[bool] = None
    newsletterSubscription: _t.Optional[bool] = None
    defaultStore: _t.Optional[str] = None
    loyaltyCard: _t.Optional[str] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R1)."""
        raise NotImplementedError

    def signUpForNewsletter(self) -> None:
        """Realizes UC2 "Sign Newsletter" (R2)."""
        raise NotImplementedError

    def unsubscribeFromNewsletter(self) -> None:
        """Realizes UC3 "Unsubscribe Newsletter" (R3)."""
        raise NotImplementedError

    def activatePushNotification(self) -> None:
        """Realizes UC4 "Activate Push Notification" (R4)."""
        raise NotImplementedError

    def deactivatePushNotification(self) -> None:
        """Realizes UC5 "Deactivate Push Notification" (R5)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC6 "Reset Password" (R6)."""
        raise NotImplementedError

    def changeFontSize(self) -> None:
        """Realizes UC7 "Change Size" (R7)."""
        raise NotImplementedError

    def changeContrast(self) -> None:
        """Realizes UC8 "Change Contrast" (R8)."""
        raise NotImplementedError

    def changeLanguage(self) -> None:
        """Realizes UC9 "Change Language" (R9)."""
        raise NotImplementedError

    def receiveSuggestion(self) -> None:
        """Realizes UC10 "Receive Suggestion" (R10)."""
        raise NotImplementedError

    def receiveDiscount(self) -> None:
        """Realizes UC11 "Receive Discount" (R11)."""
        raise NotImplementedError

    def haveDeliveryService(self) -> None:
        """Realizes UC12 "Have Delivery Service" (R13)."""
        raise NotImplementedError

    def getRecipe(self) -> None:
        """Realizes UC13 "Get Recipe" (R14)."""
        raise NotImplementedError

    def contactCustomerService(self) -> None:
        """Realizes UC14 "Contact Customer Service" (R15)."""
        raise NotImplementedError

    def scanProduct(self) -> None:
        """Realizes UC15 "Scan Product" (R16)."""
        raise NotImplementedError

    def addProductToWishlist(self) -> None:
        """Realizes UC16 "Add Product" (R17)."""
        raise NotImplementedError

    def searchProduct(self) -> None:
        """Realizes UC21 "Search Product" (R18)."""
        raise NotImplementedError

    def filterProduct(self) -> None:
        """Realizes UC22 "Filter Product" (R19)."""
        raise NotImplementedError

    def orderProductByPrice(self) -> None:
        """Realizes UC20 "Order Product By Price" (R20)."""
        raise NotImplementedError

    def orderProductByPopularity(self) -> None:
        """Realizes UC19 "Order Product By Popularity" (R21)."""
        raise NotImplementedError

    def seeOrderHistory(self) -> None:
        """Realizes UC23 "See Order History" (R37)."""
        raise NotImplementedError

    def seeProduct(self) -> None:
        """Realizes UC24 "See Product" (R25)."""
        raise NotImplementedError

    def seeQuantity(self) -> None:
        """Realizes UC25 "See Quantity" (R28)."""
        raise NotImplementedError

    def seeProductInStock(self) -> None:
        """Realizes UC26 "See Product In Stock" (R25)."""
        raise NotImplementedError

    def seeProductAvailability(self) -> None:
        """Realizes UC27 "See Product Availability" (R27)."""
        raise NotImplementedError

    def seeProductSoldOut(self) -> None:
        """Realizes UC28 "See Product Sold Out" (R29)."""
        raise NotImplementedError

    def seeProductOnSale(self) -> None:
        """Realizes UC29 "See Product On Sale" (R22)."""
        raise NotImplementedError

    def readProductInformation(self) -> None:
        """Realizes UC30 "Read Product Information" (R24)."""
        raise NotImplementedError

    def readProductBarcode(self) -> None:
        """Realizes UC31 "Read Product Barcode" (R23)."""
        raise NotImplementedError

    def seeProductLocation(self) -> None:
        """Realizes UC32 "See Product Location" (R41)."""
        raise NotImplementedError

    def getRecommendation(self) -> None:
        """Realizes UC33 "Get Recommendation" (R42)."""
        raise NotImplementedError

    def changeSelection(self) -> None:
        """Realizes UC34 "Change Selection" (R43)."""
        raise NotImplementedError

    def linkLoyaltyCard(self) -> None:
        """Realizes UC35 "Link Loyalty Card" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R45, R46, R47, R48, R49, R50, R51"""

    def updateApplicationWithNewRecipes(self) -> None:
        """Realizes UC41 "Provide Recipe Idea" (R51)."""
        raise NotImplementedError

    def editDiscount(self) -> None:
        """Realizes UC36 "Edit Discount" (R46)."""
        raise NotImplementedError

    def confirmDeliveryTime(self) -> None:
        """Realizes UC37 "Confirm Delivery Time" (R47)."""
        raise NotImplementedError

    def notifyCustomerOfDelay(self) -> None:
        """Realizes UC39 "Notify Customer Of Delay" (R49)."""
        raise NotImplementedError

    def notifyCustomerOfCancellation(self) -> None:
        """Realizes UC40 "Notify Customer Of Cancellation" (R50)."""
        raise NotImplementedError

    def provideNewDeliveryTime(self) -> None:
        """Operation."""
        raise NotImplementedError
