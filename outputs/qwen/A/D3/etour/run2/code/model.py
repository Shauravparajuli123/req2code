"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Agency:
    """Source: -"""
    culturalHeritages: _t.List["CulturalHeritage"] = _dc.field(default_factory=list)
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)
    touristAccounts: _t.List["TouristAccount"] = _dc.field(default_factory=list)
    tourists: _t.List["Tourist"] = _dc.field(default_factory=list)
    sites: _t.List["Site"] = _dc.field(default_factory=list)
    restaurantOperator: _t.Optional["RestaurantOperator"] = None


@_dc.dataclass
class CulturalHeritage:
    """Source: UC1, UC2, UC3, UC4, UC5"""
    name: _t.Optional[str] = None
    id: _t.Optional[int] = None

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Search Cultural Heritage" (UC34, UC4)."""
        raise NotImplementedError

    def viewCulturalDetails(self) -> None:
        """Realizes UC5 "View Cultural Details" (UC5)."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC7, UC8, UC9, UC10, UC11"""
    name: _t.Optional[str] = None
    id: _t.Optional[int] = None
    status: _t.Optional[str] = None
    banners: _t.List["Banner"] = _dc.field(default_factory=list)

    def searchRefreshmentPoint(self) -> None:
        """Realizes UC9 "Search Refreshment Point" (UC17, UC19, UC20, UC9)."""
        raise NotImplementedError

    def viewRefreshmentPointDetails(self) -> None:
        """Realizes UC10 "View Refreshment Point Details" (UC10)."""
        raise NotImplementedError

    def viewRefreshmentPointHistory(self) -> None:
        """Realizes UC11 "View Refreshment Point History" (UC11)."""
        raise NotImplementedError


@_dc.dataclass
class TouristAccount:
    """Source: UC12, UC13, UC14"""
    username: _t.Optional[str] = None
    id: _t.Optional[int] = None
    status: _t.Optional[str] = None

    def searchTouristAccount(self) -> None:
        """Realizes UC14 "Search Tourist Account" (UC14)."""
        raise NotImplementedError

    def viewTouristAccountDetails(self) -> None:
        """Realizes UC12 "View Tourist Account Details" (UC12)."""
        raise NotImplementedError

    def enableDisableTouristAccount(self) -> None:
        """Realizes UC13 "Enable Disable Tourist Account" (UC13)."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC15, UC16"""
    name: _t.Optional[str] = None
    position: _t.Optional[str] = None
    site: _t.Optional["Site"] = None
    feedback: _t.Optional["Feedback"] = None
    touristAccount: _t.Optional["TouristAccount"] = None

    def modifyTouristData(self) -> None:
        """Realizes UC18 "Modify Tourist Data" (UC15)."""
        raise NotImplementedError

    def deleteTouristAccount(self) -> None:
        """Realizes UC19 "Delete Tourist Account" (UC16)."""
        raise NotImplementedError

    def editPersonalSearchPreferences(self) -> None:
        """Realizes UC46 "Edit Personal Search Preferences" (UC46)."""
        raise NotImplementedError

    def changeDataAssociatedAccount(self) -> None:
        """Realizes UC47 "Change Data Associated With Your Account" (UC47)."""
        raise NotImplementedError

    def editGenericPersonalPreferences(self) -> None:
        """Realizes UC48 "Edit Generic Personal Preferences" (UC48)."""
        raise NotImplementedError

    def viewPersonalFavorites(self) -> None:
        """Realizes UC49 "View List Of Personal Favorites" (UC49)."""
        raise NotImplementedError

    def viewSitesVisited(self) -> None:
        """Realizes UC50 "View List Of Sites For Which Feedback Issued" (UC50)."""
        raise NotImplementedError

    def insertSiteBookmark(self) -> None:
        """Realizes UC51 "Insert Site In List Of Bookmarks" (UC51)."""
        raise NotImplementedError

    def deleteSiteBookmark(self) -> None:
        """Realizes UC52 "Delete Site From List Of Bookmarks" (UC52)."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Realizes UC53 "Insert Feedback For Selected Site" (UC53)."""
        raise NotImplementedError

    def searchSite(self) -> None:
        """Operation."""
        raise NotImplementedError

    def advancedSearch(self) -> None:
        """Realizes UC57 "Advanced Search" (R4)."""
        raise NotImplementedError


@_dc.dataclass
class Banner:
    """Source: UC17, UC18, UC19, UC20"""
    image: _t.Optional[str] = None
    refreshmentPoint: _t.Optional[str] = None

    def changeBannerImage(self) -> None:
        """Realizes UC20 "Change Banner Image" (UC17)."""
        raise NotImplementedError

    def checkBannerLimit(self) -> None:
        """Realizes UC21 "Check Banner Limit" (UC18)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Realizes UC22 "Delete Banner" (UC19, UC40)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC23 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""
    title: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def insertNews(self) -> None:
        """Realizes UC24 "Insert News" (UC21)."""
        raise NotImplementedError

    def deleteNews(self) -> None:
        """Realizes UC25 "Delete News" (UC22)."""
        raise NotImplementedError

    def modifyNewsData(self) -> None:
        """Realizes UC26 "Modify News Data" (UC23)."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC24, UC25, UC26"""
    name: _t.Optional[str] = None

    def viewSiteFeedback(self) -> None:
        """Realizes UC27 "View Site Feedback" (UC24)."""
        raise NotImplementedError

    def viewStatisticalReport(self) -> None:
        """Realizes UC28 "View Statistical Report" (UC25)."""
        raise NotImplementedError

    def editFeedbackComment(self) -> None:
        """Realizes UC29 "Edit Feedback Comment" (UC26)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC27, UC28, UC29, UC30, UC31, UC32, UC33, UC34, UC35, UC36, UC37"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None
    accountStatus: _t.Optional[str] = None

    def searchSite(self) -> None:
        """Realizes UC30 "Search Site" (UC27)."""
        raise NotImplementedError

    def removeSearchTag(self) -> None:
        """Realizes UC31 "Remove Search Tag" (UC28)."""
        raise NotImplementedError

    def enterSearchTag(self) -> None:
        """Realizes UC32 "Enter Search Tag" (UC29)."""
        raise NotImplementedError

    def insertNewSearchTag(self) -> None:
        """Realizes UC33 "Insert New Search Tag" (UC30)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC34 "Change Password" (UC31)."""
        raise NotImplementedError

    def confirmPasswordChange(self) -> None:
        """Realizes UC35 "Confirm Password Change" (UC32)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC36 "Create Account" (UC33)."""
        raise NotImplementedError

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Search Cultural Heritage" (UC34, UC4)."""
        raise NotImplementedError

    def login(self) -> None:
        """Realizes UC37 "Login" (UC35)."""
        raise NotImplementedError

    def logout(self) -> None:
        """Realizes UC39 "Logout" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class Moderator:
    """Source: UC31, UC38, UC39, UC40"""

    def changePassword(self) -> None:
        """Realizes UC34 "Change Password" (UC31)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC23 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def editBanner(self) -> None:
        """Realizes UC40 "Edit Banner" (UC39)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Realizes UC22 "Delete Banner" (UC19, UC40)."""
        raise NotImplementedError


@_dc.dataclass
class GuestUser:
    """Source: UC33, UC34"""
    site: _t.Optional["Site"] = None

    def createAccount(self) -> None:
        """Realizes UC36 "Create Account" (UC33)."""
        raise NotImplementedError

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Search Cultural Heritage" (UC34, UC4)."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: -"""
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)

    def changeDailyMenu(self) -> None:
        """Realizes UC41 "Change Daily Menu" (UC41)."""
        raise NotImplementedError

    def deleteDailyMenu(self) -> None:
        """Realizes UC42 "Delete Daily Menu" (UC42)."""
        raise NotImplementedError

    def changeDataPointRefreshment(self) -> None:
        """Realizes UC43 "Change Data Point Associated Refreshment" (UC43)."""
        raise NotImplementedError

    def requestConvention(self) -> None:
        """Realizes UC44 "Request Convention" (UC44)."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC54"""
    comment: _t.Optional[str] = None

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError
