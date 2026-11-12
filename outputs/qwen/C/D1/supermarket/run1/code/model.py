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

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R1)."""
        raise NotImplementedError

    def signNewsletter(self) -> None:
        """Realizes UC2 "Sign Newsletter" (R2)."""
        raise NotImplementedError

    def unsubscribeNewsletter(self) -> None:
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

    def searchProduct(self) -> None:
        """Realizes UC16 "Search Product" (R18)."""
        raise NotImplementedError

    def filterProduct(self) -> None:
        """Realizes UC17 "Filter Product" (R19)."""
        raise NotImplementedError

    def orderProduct(self) -> None:
        """Realizes UC18 "Order Product" (R20, R21)."""
        raise NotImplementedError

    def seeProduct(self) -> None:
        """Realizes UC19 "See Product" (R25, R27, R29)."""
        raise NotImplementedError

    def seeQuantity(self) -> None:
        """Realizes UC20 "See Quantity" (R28)."""
        raise NotImplementedError

    def seeOrderHistory(self) -> None:
        """Realizes UC21 "See Order History" (R37)."""
        raise NotImplementedError

    def placeOrder(self) -> None:
        """Realizes UC22 "Place Order" (R38)."""
        raise NotImplementedError

    def addProduct(self) -> None:
        """Realizes UC23 "Add Product" (R17, R39)."""
        raise NotImplementedError

    def readProductInformation(self) -> None:
        """Realizes UC24 "Read Product Information" (R24)."""
        raise NotImplementedError

    def scanBarcode(self) -> None:
        """Realizes UC25 "Scan Barcode" (R23)."""
        raise NotImplementedError

    def seeAvailableQuantity(self) -> None:
        """Realizes UC20 "See Quantity" (R28)."""
        raise NotImplementedError

    def seeOrderAvailability(self) -> None:
        """Realizes UC21 "See Order History" (R37)."""
        raise NotImplementedError

    def seeRecipeSuggestions(self) -> None:
        """Realizes UC19 "See Product" (R25, R27, R29)."""
        raise NotImplementedError

    def purchaseOnline(self) -> None:
        """Realizes UC18 "Order Product" (R20, R21)."""
        raise NotImplementedError

    def seeDeliveryOptions(self) -> None:
        """Realizes UC21 "See Order History" (R37)."""
        raise NotImplementedError

    def linkLoyaltyCard(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Employee:
    """Source: R45, R46, R47, R48, R49, R50, R51"""

    def updateApplication(self) -> None:
        """Realizes UC33 "Update Application" (R45)."""
        raise NotImplementedError

    def editDiscount(self) -> None:
        """Realizes UC32 "Edit Discount" (R46)."""
        raise NotImplementedError

    def confirmDeliveryTime(self) -> None:
        """Realizes UC29 "Confirm Delivery Time" (R47)."""
        raise NotImplementedError

    def notifyUnavailableProduct(self) -> None:
        """Realizes UC27 "Notify Item" (R26)."""
        raise NotImplementedError

    def notifyDelayedDelivery(self) -> None:
        """Realizes UC27 "Notify Item" (R26)."""
        raise NotImplementedError

    def contactCustomer(self) -> None:
        """Realizes UC30 "Contact Customer" (R50)."""
        raise NotImplementedError

    def provideNewDeliveryTime(self) -> None:
        """Operation."""
        raise NotImplementedError
