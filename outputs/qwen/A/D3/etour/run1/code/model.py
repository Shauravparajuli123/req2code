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
    sites: _t.List["Site"] = _dc.field(default_factory=list)
    user: _t.Optional["User"] = None


@_dc.dataclass
class CulturalHeritage:
    """Source: UC1, UC2, UC3, UC4, UC5"""
    name: _t.Optional[str] = None
    id: _t.Optional[int] = None

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Search Cultural Heritage" (UC4)."""
        raise NotImplementedError

    def viewCulturalDetails(self) -> None:
        """Realizes UC5 "View Cultural Details" (UC5)."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC7, UC8, UC9, UC10, UC11"""
    name: _t.Optional[str] = None
    id: _t.Optional[int] = None
    banners: _t.List["Banner"] = _dc.field(default_factory=list)

    def searchRefreshmentPoint(self) -> None:
        """Realizes UC9 "Search Refreshment Point" (UC9)."""
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
    games: _t.List["Game"] = _dc.field(default_factory=list)
    sites: _t.List["Site"] = _dc.field(default_factory=list)
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)
    searchTags: _t.List["SearchTag"] = _dc.field(default_factory=list)

    def modifyData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editPersonalSearchPreferences(self) -> None:
        """Realizes UC42 "Edit Personal Search Preferences" (UC46)."""
        raise NotImplementedError

    def changeDataAssociatedWithAccount(self) -> None:
        """Realizes UC43 "Change Data Associated With Your Account" (UC47)."""
        raise NotImplementedError

    def editGenericPersonalPreferences(self) -> None:
        """Realizes UC44 "Edit Generic Personal Preferences" (UC48)."""
        raise NotImplementedError

    def viewPersonalFavorites(self) -> None:
        """Realizes UC45 "View List Of Personal Favorites" (UC49)."""
        raise NotImplementedError

    def viewSitesVisited(self) -> None:
        """Realizes UC46 "View List Of Sites For Which Feedback Issued" (UC50)."""
        raise NotImplementedError

    def insertSiteInBookmarks(self) -> None:
        """Realizes UC47 "Insert Site In List Of Bookmarks" (UC51)."""
        raise NotImplementedError

    def deleteSiteFromBookmarks(self) -> None:
        """Realizes UC48 "Delete Site From List Of Bookmarks" (UC52)."""
        raise NotImplementedError

    def insertFeedbackForSelectedSite(self) -> None:
        """Realizes UC49 "Insert Feedback For Selected Site" (UC53)."""
        raise NotImplementedError


@_dc.dataclass
class Banner:
    """Source: UC17, UC18, UC19, UC20"""
    image: _t.Optional[str] = None

    def changeImage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def checkBannerLimit(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""
    title: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def insertNews(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteNews(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeNewsData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC24, UC25, UC26"""
    name: _t.Optional[str] = None
    id: _t.Optional[int] = None

    def viewFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewStatisticalReport(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editFeedbackComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Game:
    """Source: -"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC28 "Create Game" (UC27)."""
        raise NotImplementedError


@_dc.dataclass
class SearchTag:
    """Source: UC27, UC28, UC29, UC30"""
    name: _t.Optional[str] = None
    status: _t.Optional[str] = None

    def removeSearchTag(self) -> None:
        """Realizes UC29 "Remove Search Tag" (UC28)."""
        raise NotImplementedError

    def enterSearchTag(self) -> None:
        """Realizes UC30 "Enter Search Tag" (UC29)."""
        raise NotImplementedError

    def insertNewSearchTag(self) -> None:
        """Realizes UC31 "Insert New Search Tag" (UC30)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC33, UC35, UC36, UC37"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None
    status: _t.Optional[str] = None

    def register(self) -> None:
        """Realizes UC33 "Register" (UC33)."""
        raise NotImplementedError

    def login(self) -> None:
        """Realizes UC34 "Login" (UC35)."""
        raise NotImplementedError

    def logout(self) -> None:
        """Realizes UC35 "Logout" (UC37)."""
        raise NotImplementedError

    def authenticate(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: UC38, UC39, UC40"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None
    status: _t.Optional[str] = None
    games: _t.List["Game"] = _dc.field(default_factory=list)

    def insertBanner(self) -> None:
        """Realizes UC20 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def editBanner(self) -> None:
        """Realizes UC36 "Edit Banner" (UC39)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Realizes UC19 "Delete Banner" (UC19, UC40)."""
        raise NotImplementedError

    def changeDailyMenu(self) -> None:
        """Realizes UC37 "Change Daily Menu" (UC41)."""
        raise NotImplementedError

    def deleteDailyMenu(self) -> None:
        """Realizes UC38 "Delete Daily Menu" (UC42)."""
        raise NotImplementedError

    def changeDataPointRefreshment(self) -> None:
        """Realizes UC39 "Change Data Point Associated Refreshment" (UC43)."""
        raise NotImplementedError

    def requestConvention(self) -> None:
        """Realizes UC40 "Request Convention" (UC44)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Realizes UC41 "View Statistics" (UC45)."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC54"""
    comment: _t.Optional[str] = None
    siteId: _t.Optional[int] = None

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Gps:
    """Source: UC56, UC57"""
    position: _t.Optional[str] = None
    tourist: _t.Optional["Tourist"] = None

    def getPosition(self) -> None:
        """Operation."""
        raise NotImplementedError
