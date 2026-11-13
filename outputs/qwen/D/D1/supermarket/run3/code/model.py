"""Code skeleton generated from the shared model of D1/supermarket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Customer:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44"""
    account: _t.Optional[str] = None
    newsletterSubscription: _t.Optional[bool] = None
    pushNotifications: _t.Optional[bool] = None
    password: _t.Optional[str] = None
    language: _t.Optional[str] = None
    fontSize: _t.Optional[int] = None
    contrast: _t.Optional[int] = None
    notification: _t.Optional["Notification"] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create A Personal Account" (R1)."""
        raise NotImplementedError

    def subscribeToNewsletter(self) -> None:
        """Realizes UC2 "Sign Up For The Newsletter" (R2)."""
        raise NotImplementedError

    def unsubscribeFromNewsletter(self) -> None:
        """Realizes UC3 "Unsubscribe From The Newsletter" (R3)."""
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
        """Realizes UC9 "Change Application S Language" (R9)."""
        raise NotImplementedError


@_dc.dataclass
class Product:
    """Source: R10, R11, R12, R19, R20, R21, R22, R25, R26, R27, R28, R29, R30, R31"""
    discount: _t.Optional[bool] = None
    availability: _t.Optional[bool] = None
    order: _t.Optional["Order"] = None

    def suggestProduct(self) -> None:
        """Realizes UC10 "Receive Product Suggestions" (R10)."""
        raise NotImplementedError

    def personalDiscount(self) -> None:
        """Realizes UC11 "Receive Personal Discount" (R11)."""
        raise NotImplementedError

    def personalDiscountNotification(self) -> None:
        """Realizes UC12 "Receive Personal Discount Notifications" (R12)."""
        raise NotImplementedError

    def filterByDietaryRestrictions(self) -> None:
        """Realizes UC19 "Filter Products By Dietary Restrictions" (R19)."""
        raise NotImplementedError

    def orderByPrice(self) -> None:
        """Realizes UC20 "Order By Price" (R20)."""
        raise NotImplementedError

    def orderByPopularity(self) -> None:
        """Realizes UC21 "Order By Popularity" (R21)."""
        raise NotImplementedError

    def checkStock(self) -> None:
        """Realizes UC25 "Check Product Stock" (R25)."""
        raise NotImplementedError

    def checkBackInStock(self) -> None:
        """Realizes UC26 "Be Notified When Product Is Back In Stock" (R26)."""
        raise NotImplementedError

    def checkAvailabilityInOtherStores(self) -> None:
        """Realizes UC27 "Check Availability In Other Stores" (R27)."""
        raise NotImplementedError

    def seeQuantityInStore(self) -> None:
        """Realizes UC28 "See Product Quantity In Store" (R28)."""
        raise NotImplementedError

    def seeAvailabilityDate(self) -> None:
        """Realizes UC29 "See Product Availability Date" (R29)."""
        raise NotImplementedError

    def getRecipeIdeas(self) -> None:
        """Realizes UC30 "Get Recipe Ideas" (R30)."""
        raise NotImplementedError

    def seeProductsUsedInRecipe(self) -> None:
        """Realizes UC31 "See Products Used In Recipe" (R31)."""
        raise NotImplementedError


@_dc.dataclass
class Order:
    """Source: R32, R33, R34, R35, R37, R38, R39"""
    history: _t.Optional[str] = None
    previousOrder: _t.Optional[str] = None

    def purchaseOnline(self) -> None:
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

    def useExpressDelivery(self) -> None:
        """Realizes UC36 "Use Express Delivery" (R36)."""
        raise NotImplementedError

    def repeatPreviousOrder(self) -> None:
        """Realizes UC38 "Repeat Previous Order" (R38)."""
        raise NotImplementedError

    def addPreviousOrderToNewOrder(self) -> None:
        """Realizes UC39 "Add Previous Order To New Order" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R22, R26, R36"""
    type: _t.Optional[str] = None

    def notifySale(self) -> None:
        """Realizes UC22 "Be Notified Of Sales" (R22)."""
        raise NotImplementedError

    def notifyBackInStock(self) -> None:
        """Realizes UC26 "Be Notified When Product Is Back In Stock" (R26)."""
        raise NotImplementedError

    def payDigitally(self) -> None:
        """Realizes UC40 "Digitally Pay For Delivery" (R40)."""
        raise NotImplementedError
