"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CulturalHeritage:
    """Source: UC1, UC2, UC3, UC4, UC5"""
    name: _t.Optional[str] = None

    def deleteCulturalHeritage(self) -> None:
        """Realizes UC1 "Delete Cultural Object" (UC1)."""
        raise NotImplementedError

    def insertCulturalHeritage(self) -> None:
        """Realizes UC2 "Insert Cultural Object" (UC2)."""
        raise NotImplementedError

    def changeCulturalHeritageData(self) -> None:
        """Realizes UC3 "Change Cultural Object Data" (UC3)."""
        raise NotImplementedError

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Search Cultural Heritage" (UC4)."""
        raise NotImplementedError

    def viewCulturalHeritageDetails(self) -> None:
        """Realizes UC5 "View Cultural Details" (UC5)."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC7, UC8, UC9, UC10, UC11"""
    name: _t.Optional[str] = None

    def deleteRefreshmentPoint(self) -> None:
        """Realizes UC6 "Delete Refreshment Point" (UC6)."""
        raise NotImplementedError

    def activateConvention(self) -> None:
        """Realizes UC7 "Activate Convention" (UC7)."""
        raise NotImplementedError

    def editRefreshmentPointData(self) -> None:
        """Realizes UC8 "Edit Refreshment Point Data" (UC8)."""
        raise NotImplementedError

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

    def enableDisableTouristAccount(self) -> None:
        """Realizes UC13 "Enable Disable Tourist Account" (UC13)."""
        raise NotImplementedError

    def searchTouristAccount(self) -> None:
        """Realizes UC14 "Search Tourist Account" (UC14)."""
        raise NotImplementedError

    def viewTouristAccountDetails(self) -> None:
        """Realizes UC12 "View Tourist Account Details" (UC12)."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC15, UC16"""
    name: _t.Optional[str] = None
    site: _t.Optional["Site"] = None
    searchTags: _t.List["SearchTag"] = _dc.field(default_factory=list)

    def modifyData(self) -> None:
        """Realizes UC16 "Modify Tourist Data" (UC15)."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Realizes UC17 "Delete Tourist Account" (UC16)."""
        raise NotImplementedError

    def editPersonalSearchPreferences(self) -> None:
        """Realizes UC43 "Edit Personal Search Preferences" (UC46)."""
        raise NotImplementedError

    def changeDataAssociatedWithAccount(self) -> None:
        """Realizes UC44 "Change Data Associated With Account" (UC47)."""
        raise NotImplementedError

    def editGenericPersonalPreferences(self) -> None:
        """Realizes UC45 "Edit Generic Personal Preferences" (UC48)."""
        raise NotImplementedError

    def viewPersonalFavorites(self) -> None:
        """Realizes UC46 "View Personal Favorites" (UC49)."""
        raise NotImplementedError

    def viewListSitesForFeedback(self) -> None:
        """Realizes UC47 "View List Of Sites For Feedback" (UC50)."""
        raise NotImplementedError

    def insertSiteInBookmarks(self) -> None:
        """Realizes UC48 "Insert Site In Bookmarks" (UC51)."""
        raise NotImplementedError

    def deleteSiteFromBookmarks(self) -> None:
        """Realizes UC49 "Delete Site From Bookmarks" (UC52)."""
        raise NotImplementedError

    def insertFeedbackForSite(self) -> None:
        """Realizes UC50 "Insert Feedback For Site" (UC53)."""
        raise NotImplementedError


@_dc.dataclass
class Banner:
    """Source: UC17, UC18, UC19, UC20"""
    image: _t.Optional[str] = None

    def changeImage(self) -> None:
        """Realizes UC18 "Change Banner Image" (UC17)."""
        raise NotImplementedError

    def checkBannerLimit(self) -> None:
        """Realizes UC19 "Check Banner Limit" (UC18)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Realizes UC20 "Delete Banner" (UC19, UC40)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC21 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""
    title: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def insertNews(self) -> None:
        """Realizes UC22 "Insert News" (UC21)."""
        raise NotImplementedError

    def deleteNews(self) -> None:
        """Realizes UC23 "Delete News" (UC22)."""
        raise NotImplementedError

    def modifyNews(self) -> None:
        """Realizes UC24 "Modify News Data" (UC23)."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC24, UC25, UC26"""
    name: _t.Optional[str] = None
    id: _t.Optional[int] = None

    def viewFeedback(self) -> None:
        """Realizes UC25 "View Site Feedback" (UC24)."""
        raise NotImplementedError

    def viewStatisticalReport(self) -> None:
        """Realizes UC26 "Generate Statistical Report" (UC25)."""
        raise NotImplementedError

    def editFeedbackComment(self) -> None:
        """Realizes UC27 "Edit Feedback Comment" (UC26)."""
        raise NotImplementedError


@_dc.dataclass
class GuestUser:
    """Source: UC34, UC33"""
    site: _t.Optional["Site"] = None


@_dc.dataclass
class RegisteredUser:
    """Source: UC35, UC36, UC37"""
    site: _t.Optional["Site"] = None


@_dc.dataclass
class PointOfRestaurantOperator:
    """Source: UC38, UC39, UC40"""
    banners: _t.List["Banner"] = _dc.field(default_factory=list)
    refreshmentPoint: _t.Optional["RefreshmentPoint"] = None


@_dc.dataclass
class SearchTag:
    """Source: UC27, UC28, UC29, UC30"""
    pass


@_dc.dataclass
class Game:
    """Source: -"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC15 "Create Game" (R1, UC30)."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: -"""

    def changeDailyMenu(self) -> None:
        """Realizes UC38 "Change Daily Menu" (UC41)."""
        raise NotImplementedError

    def deleteDailyMenu(self) -> None:
        """Realizes UC39 "Delete Daily Menu" (UC42)."""
        raise NotImplementedError

    def changeDataPointRefreshment(self) -> None:
        """Realizes UC40 "Change Data Point Refreshment" (UC43)."""
        raise NotImplementedError

    def requestConvention(self) -> None:
        """Realizes UC41 "Request Convention" (UC44)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Realizes UC42 "View Statistics" (UC45)."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC54, UC55"""
    comment: _t.Optional[str] = None
    siteId: _t.Optional[int] = None
    tourist: _t.Optional["Tourist"] = None

    def editComment(self) -> None:
        """Realizes UC51 "Edit Comment" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC54, UC57"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def authenticate(self) -> None:
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
