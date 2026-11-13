"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Agency:
    """Source: -"""
    touristAccount: _t.Optional["TouristAccount"] = None
    refreshmentPoint: _t.Optional["RefreshmentPoint"] = None
    site: _t.Optional["Site"] = None
    news: _t.Optional["News"] = None
    feedback: _t.Optional["Feedback"] = None

    def deleteCulturalObject(self) -> None:
        """Realizes UC1 "Delete Cultural Object" (UC1)."""
        raise NotImplementedError

    def insertCulturalObject(self) -> None:
        """Realizes UC2 "Insert Cultural Object" (UC2)."""
        raise NotImplementedError

    def changeCulturalObjectData(self) -> None:
        """Realizes UC3 "Change Cultural Object Data" (UC3)."""
        raise NotImplementedError

    def getCulturalObjects(self) -> None:
        """Realizes UC4 "Return List Of Cultural Objects" (UC4)."""
        raise NotImplementedError

    def viewCulturalObjectDetails(self) -> None:
        """Realizes UC5 "View Cultural Object Details" (UC5)."""
        raise NotImplementedError

    def deleteRefreshmentPoint(self) -> None:
        """Realizes UC6 "Delete Refreshment Point" (UC6)."""
        raise NotImplementedError

    def requestConvention(self) -> None:
        """Realizes UC7 "Convention Request By Refreshment Point" (UC7)."""
        raise NotImplementedError

    def editRefreshmentPointData(self) -> None:
        """Realizes UC8 "Edit Refreshment Point Data" (UC8)."""
        raise NotImplementedError

    def getRefreshmentPoints(self) -> None:
        """Realizes UC9 "Return List Of Refreshment Points" (UC9)."""
        raise NotImplementedError

    def viewRefreshmentPointDetails(self) -> None:
        """Realizes UC10 "View Refreshment Point Details" (UC10)."""
        raise NotImplementedError

    def viewRefreshmentPointHistory(self) -> None:
        """Realizes UC11 "View Refreshment Point History" (UC11)."""
        raise NotImplementedError

    def enableDisableTouristAccount(self) -> None:
        """Realizes UC12 "Enable Disable Tourist Account" (UC13)."""
        raise NotImplementedError

    def getTouristAccounts(self) -> None:
        """Realizes UC13 "Return List Of Tourist Accounts" (UC14)."""
        raise NotImplementedError

    def viewTouristAccountDetails(self) -> None:
        """Realizes UC14 "View Tourist Account Details" (UC12)."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Realizes UC16 "Delete Account" (UC16)."""
        raise NotImplementedError

    def changeData(self) -> None:
        """Realizes UC15 "Change Data" (UC15, UC23)."""
        raise NotImplementedError

    def viewReport(self) -> None:
        """Realizes UC24 "View Report" (UC25)."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC25 "Edit Comment" (R1, UC26)."""
        raise NotImplementedError


@_dc.dataclass
class CulturalObject:
    """Source: UC1, UC2, UC3, UC4, UC5"""
    name: _t.Optional[str] = None
    description: _t.Optional[str] = None


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC7, UC8, UC9, UC10, UC11"""
    name: _t.Optional[str] = None
    address: _t.Optional[str] = None
    status: _t.Optional[str] = None
    bannerAd: _t.Optional["BannerAd"] = None

    def checkPoint(self) -> None:
        """Realizes UC18 "Check Point" (UC18)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC20 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class TouristAccount:
    """Source: UC12, UC13, UC14"""
    username: _t.Optional[str] = None
    status: _t.Optional[str] = None
    comment: _t.Optional["Comment"] = None


@_dc.dataclass
class Tourist:
    """Source: UC15, UC16"""
    id: _t.Optional[int] = None
    authenticated: _t.Optional[bool] = None
    feedback: _t.Optional["Feedback"] = None
    bookmark: _t.Optional["Bookmark"] = None
    site: _t.Optional["Site"] = None
    statistic: _t.Optional["Statistic"] = None

    def changeData(self) -> None:
        """Realizes UC15 "Change Data" (UC15, UC23)."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Realizes UC16 "Delete Account" (UC16)."""
        raise NotImplementedError


@_dc.dataclass
class BannerAd:
    """Source: UC17"""

    def changeImage(self) -> None:
        """Realizes UC17 "Change Image" (UC17, UC39)."""
        raise NotImplementedError


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""

    def insertNews(self) -> None:
        """Realizes UC21 "Insert News" (UC21)."""
        raise NotImplementedError

    def deleteNews(self) -> None:
        """Realizes UC22 "Delete News" (UC22)."""
        raise NotImplementedError

    def changeData(self) -> None:
        """Realizes UC15 "Change Data" (UC15, UC23)."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC24, UC25, UC26"""
    touristId: _t.Optional[int] = None
    siteId: _t.Optional[int] = None

    def viewFeedback(self) -> None:
        """Realizes UC23 "View Feedback" (UC24)."""
        raise NotImplementedError

    def viewReport(self) -> None:
        """Realizes UC24 "View Report" (UC25)."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC25 "Edit Comment" (R1, UC26)."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Realizes UC41 "Insert Feedback" (UC53)."""
        raise NotImplementedError

    def viewFavoriteList(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewVisitedSites(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Game:
    """Source: -"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC26 "Create Game" (UC27)."""
        raise NotImplementedError


@_dc.dataclass
class SearchTag:
    """Source: UC28, UC29, UC30"""

    def removeSearchTag(self) -> None:
        """Realizes UC27 "Remove Search Tag" (UC28)."""
        raise NotImplementedError

    def insertTagSearch(self) -> None:
        """Realizes UC28 "Insert Tag Search" (UC30)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC33, UC34, UC35, UC36, UC37"""
    feedback: _t.Optional["Feedback"] = None

    def supplyLogin(self) -> None:
        """Realizes UC32 "Supply Login" (UC36)."""
        raise NotImplementedError

    def searchSite(self) -> None:
        """Realizes UC31 "Search Site" (R4, UC34)."""
        raise NotImplementedError

    def endSession(self) -> None:
        """Realizes UC33 "End Session" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: UC38, UC39, UC40"""
    convention: _t.Optional["Convention"] = None
    statistic: _t.Optional["Statistic"] = None

    def insertBanner(self) -> None:
        """Realizes UC20 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def changeImage(self) -> None:
        """Realizes UC17 "Change Image" (UC17, UC39)."""
        raise NotImplementedError

    def deleteBannerAd(self) -> None:
        """Realizes UC19 "Delete Banner Ad" (UC19, UC40)."""
        raise NotImplementedError


@_dc.dataclass
class Menu:
    """Source: UC41, UC42"""
    name: _t.Optional[str] = None

    def createMenu(self) -> None:
        """Realizes UC26 "Create Game" (UC27)."""
        raise NotImplementedError

    def deleteMenu(self) -> None:
        """Realizes UC35 "Delete Menu" (UC42)."""
        raise NotImplementedError


@_dc.dataclass
class DataPoint:
    """Source: UC43"""

    def changeDataPoint(self) -> None:
        """Realizes UC36 "Change Data Point" (UC43)."""
        raise NotImplementedError


@_dc.dataclass
class Convention:
    """Source: UC44"""

    def requireConvention(self) -> None:
        """Realizes UC37 "Require Convention" (UC44)."""
        raise NotImplementedError


@_dc.dataclass
class Statistic:
    """Source: UC45"""

    def viewStatistic(self) -> None:
        """Realizes UC38 "View Statistic" (UC45)."""
        raise NotImplementedError


@_dc.dataclass
class SearchPreference:
    """Source: UC46, UC47, UC48"""

    def editSearchPreference(self) -> None:
        """Realizes UC39 "Edit Search Preference" (UC46)."""
        raise NotImplementedError

    def changePreference(self) -> None:
        """Realizes UC15 "Change Data" (UC15, UC23)."""
        raise NotImplementedError

    def editPreference(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Bookmark:
    """Source: UC51, UC52"""

    def insertBookmark(self) -> None:
        """Realizes UC41 "Insert Feedback" (UC53)."""
        raise NotImplementedError

    def removeBookmark(self) -> None:
        """Realizes UC43 "Delete Site" (UC52)."""
        raise NotImplementedError


@_dc.dataclass
class Comment:
    """Source: UC54"""
    text: _t.Optional[str] = None
    siteId: _t.Optional[int] = None

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Gps:
    """Source: UC56"""
    position: _t.Optional[str] = None

    def getPosition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AdvancedSearch:
    """Source: UC57"""
    criteria: _t.Optional[str] = None

    def searchSites(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC58"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None
    feedback: _t.Optional["Feedback"] = None
    statistic: _t.Optional["Statistic"] = None

    def displayDetails(self) -> None:
        """Operation."""
        raise NotImplementedError
