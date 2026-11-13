"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CulturalHeritage:
    """Source: UC1, UC2, UC3, UC4, UC5"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None

    def createCulturalHeritage(self) -> None:
        """Realizes UC2 "Insert A New Cultural Object" (R2)."""
        raise NotImplementedError

    def updateCulturalHeritage(self) -> None:
        """Realizes UC3 "Change Data Of A Cultural Object" (R3)."""
        raise NotImplementedError

    def deleteCulturalHeritage(self) -> None:
        """Realizes UC1 "Delete A Cultural Object" (R1)."""
        raise NotImplementedError

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Return The List Of Cultural Objects" (R4)."""
        raise NotImplementedError

    def viewCulturalHeritageDetails(self) -> None:
        """Realizes UC5 "View The Details Of A Selected Cultural Object" (R5)."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC7, UC8, UC9, UC10"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None
    banners: _t.Optional[str] = None

    def createRefreshmentPoint(self) -> None:
        """Realizes UC2 "Insert A New Cultural Object" (R2)."""
        raise NotImplementedError

    def updateRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewRefreshmentPointDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class TouristAccount:
    """Source: UC12, UC13, UC14"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None

    def searchTouristAccount(self) -> None:
        """Realizes UC14 "Return The List Of Tourist Accounts" (R14)."""
        raise NotImplementedError

    def viewTouristAccountDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def enableDisableTouristAccount(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC15"""
    selectedAccount: _t.Optional[str] = None
    searchPreferences: _t.Optional[str] = None
    personalFavorites: _t.Optional[str] = None
    visitedSites: _t.Optional[str] = None
    searchPreference: _t.Optional["SearchPreference"] = None
    bookmark: _t.Optional["Bookmark"] = None
    site: _t.Optional["Site"] = None

    def modifyData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editSearchPreferences(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editPersonalData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertFavorite(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeFavorite(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: UC15"""
    data: _t.Optional[str] = None


@_dc.dataclass
class Banner:
    """Source: UC17, UC19, UC20"""
    image: _t.Optional[str] = None

    def insertBanner(self) -> None:
        """Realizes UC40 "Inserting A New Banner Associated With The Point Of Rest" (UC38)."""
        raise NotImplementedError

    def editBanner(self) -> None:
        """Realizes UC41 "Changing The Image Of A Banner Ad" (UC39)."""
        raise NotImplementedError

    def removeBanner(self) -> None:
        """Realizes UC42 "Delete A Banner Ad Associated With The Point Of Rest" (UC40)."""
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

    def modifyNews(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC24, UC25, UC26"""
    feedbacks: _t.Optional[str] = None
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None

    def searchSite(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewStatisticalReport(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC24, UC26"""
    comments: _t.Optional[str] = None
    vote: _t.Optional[str] = None
    comment: _t.Optional[str] = None
    siteId: _t.Optional[int] = None

    def insert(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC100 "Edit Comment" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class Comment:
    """Source: UC26"""
    pass


@_dc.dataclass
class Search:
    """Source: UC27"""
    site: _t.Optional[str] = None
    tags: _t.List["Tag"] = _dc.field(default_factory=list)

    def searchSite(self) -> None:
        """Realizes UC29 "Search For A Specific Site" (UC27)."""
        raise NotImplementedError


@_dc.dataclass
class Tag:
    """Source: UC28, UC29, UC30"""
    name: _t.Optional[str] = None

    def removeTag(self) -> None:
        """Realizes UC30 "Remove One Or More Search Tags" (UC28)."""
        raise NotImplementedError

    def addTag(self) -> None:
        """Realizes UC32 "Insert A New Tag Search" (UC30)."""
        raise NotImplementedError


@_dc.dataclass
class UserAccount:
    """Source: UC31, UC35, UC36, UC37"""
    username: _t.Optional[str] = None

    def changePassword(self) -> None:
        """Realizes UC33 "Change The Password Associated With Your Account" (UC31)."""
        raise NotImplementedError

    def login(self) -> None:
        """Realizes UC37 "Ensure A Registered User To Access The System With The Privileges That Fall" (UC35)."""
        raise NotImplementedError

    def logout(self) -> None:
        """Realizes UC39 "End The Current Session" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class PointOfRestaurant:
    """Source: UC38, UC39, UC40"""
    banners: _t.Optional[str] = None


@_dc.dataclass
class PointOfRestaurantOperator:
    """Source: UC41, UC42, UC43, UC44"""

    def activateMenuEditing(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteMenu(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editDataPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def requestConvention(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class SearchPreference:
    """Source: UC46, UC48"""

    def edit(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Bookmark:
    """Source: UC49, UC51, UC52"""
    site: _t.Optional[str] = None

    def insert(self) -> None:
        """Operation."""
        raise NotImplementedError

    def remove(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Menu:
    """Source: UC41"""
    day: _t.Optional[str] = None

    def uploadData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Convention:
    """Source: UC44"""
    agreementData: _t.Optional[str] = None

    def request(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class DataPoint:
    """Source: UC43"""

    def uploadData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Statistics:
    """Source: UC45"""

    def view(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC54, UC57"""
    userId: _t.Optional[int] = None


@_dc.dataclass
class Gps:
    """Source: UC56, UC57"""
    position: _t.Optional[str] = None
