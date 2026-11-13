"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CulturalHeritage:
    """Source: UC1, UC2, UC3, UC4, UC5, UC11"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None

    def deleteCulturalHeritage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def createCulturalHeritage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updateCulturalHeritage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchCulturalHeritage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewCulturalHeritageDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewCulturalHeritageHistory(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC8, UC9, UC10, UC11"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None
    banners: _t.Optional[str] = None

    def deleteRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def createRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updateRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewRefreshmentPointDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewRefreshmentPointHistory(self) -> None:
        """Operation."""
        raise NotImplementedError

    def checkBannerLimit(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class TouristAccount:
    """Source: UC12, UC13, UC14"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None

    def viewTouristAccountDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def enableDisableTouristAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchTouristAccount(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC15"""
    accountData: _t.Optional[str] = None
    searchPreferences: _t.Optional[str] = None
    personalFavorites: _t.Optional[str] = None

    def modifyData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updateSearchPreferences(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updatePersonalData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewPersonalFavorites(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewVisitedSites(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addBookmark(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeBookmark(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Banner:
    """Source: UC17, UC19, UC20"""
    image: _t.Optional[str] = None
    pointOfRestaurant: _t.Optional["PointOfRestaurant"] = None

    def changeImage(self) -> None:
        """Realizes UC40 "Changing The Image Of A Banner Ad" (UC39)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC39 "Inserting A New Banner Associated With The Point Of Rest" (UC38)."""
        raise NotImplementedError

    def changeBannerImage(self) -> None:
        """Realizes UC40 "Changing The Image Of A Banner Ad" (UC39)."""
        raise NotImplementedError

    def removeBanner(self) -> None:
        """Realizes UC41 "Delete A Banner Ad Associated With The Point Of Rest" (UC40)."""
        raise NotImplementedError


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""
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

    def viewFeedbacks(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewStatisticalReport(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC24, UC26"""
    comments: _t.Optional[str] = None
    comment: _t.Optional[str] = None
    siteId: _t.Optional[int] = None

    def uploadFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Comment:
    """Source: UC26"""

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class SearchTag:
    """Source: UC28, UC29"""
    tag: _t.Optional[str] = None
    userAccount: _t.Optional["UserAccount"] = None

    def removeSearchTag(self) -> None:
        """Realizes UC29 "Remove One Or More Search Tags" (UC28)."""
        raise NotImplementedError

    def enterSearchTag(self) -> None:
        """Realizes UC30 "Enter Search Tags Already In The System" (UC29)."""
        raise NotImplementedError


@_dc.dataclass
class UserAccount:
    """Source: UC31, UC35, UC36, UC37"""
    password: _t.Optional[str] = None

    def changePassword(self) -> None:
        """Realizes UC32 "Change The Password Associated With Your Account" (UC31)."""
        raise NotImplementedError

    def login(self) -> None:
        """Realizes UC36 "Ensure A Registered User To Access The System With The Privileges That Fall" (UC35)."""
        raise NotImplementedError

    def logout(self) -> None:
        """Realizes UC38 "End The Current Session" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class Login:
    """Source: UC35, UC36, UC37"""
    status: _t.Optional[str] = None

    def verifyLogin(self) -> None:
        """Realizes UC36 "Ensure A Registered User To Access The System With The Privileges That Fall" (UC35)."""
        raise NotImplementedError

    def loginError(self) -> None:
        """Realizes UC37 "Data Supplied For The Login Is Incorrect" (UC36)."""
        raise NotImplementedError

    def logout(self) -> None:
        """Realizes UC38 "End The Current Session" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class PointOfRestaurant:
    """Source: UC38, UC39, UC40"""
    banners: _t.Optional[str] = None


@_dc.dataclass
class Game:
    """Source: -"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC27 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class Restaurant:
    """Source: UC41, UC42, UC43, UC44"""
    menu: _t.Optional[str] = None
    dataPoints: _t.Optional[str] = None
    conventions: _t.Optional[str] = None
    statistics: _t.Optional[str] = None
    menus: _t.List["Menu"] = _dc.field(default_factory=list)

    def createMenu(self) -> None:
        """Realizes UC27 "Create Game" (R1)."""
        raise NotImplementedError

    def deleteMenu(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updateDataPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def requestConvention(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Menu:
    """Source: UC41"""
    day: _t.Optional[str] = None


@_dc.dataclass
class DataPoint:
    """Source: UC43"""
    pass


@_dc.dataclass
class Convention:
    """Source: UC44"""
    pass


@_dc.dataclass
class Statistics:
    """Source: UC45"""
    pass


@_dc.dataclass
class SearchPreference:
    """Source: UC46"""
    pass


@_dc.dataclass
class Bookmark:
    """Source: UC51, UC52"""
    pass


@_dc.dataclass
class User:
    """Source: UC54, UC55, UC57, UC58"""
    userId: _t.Optional[int] = None
    username: _t.Optional[str] = None
