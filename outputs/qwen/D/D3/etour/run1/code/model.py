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


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC7, UC8, UC9, UC10, UC11"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None
    banners: _t.Optional[str] = None

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
    tourist: _t.Optional["Tourist"] = None

    def searchTouristAccount(self) -> None:
        """Operation."""
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
    data: _t.Optional[str] = None
    searchPreferences: _t.Optional[str] = None
    accountData: _t.Optional[str] = None
    favorites: _t.Optional[str] = None
    visitedSites: _t.Optional[str] = None
    feedback: _t.Optional["Feedback"] = None

    def modifyData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editSearchPreferences(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editAccountData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editGeneralPreferences(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewFavorites(self) -> None:
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

    def changeImage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeBannerImage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeBanner(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""
    data: _t.Optional[str] = None

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
    feedback: _t.Optional[str] = None
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)

    def viewFeedback(self) -> None:
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
    text: _t.Optional[str] = None

    def editCommentText(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Search:
    """Source: UC27"""
    site: _t.Optional[str] = None
    tag: _t.Optional["Tag"] = None

    def searchSite(self) -> None:
        """Realizes UC29 "Search For A Specific Site On The Computer" (UC27)."""
        raise NotImplementedError


@_dc.dataclass
class Tag:
    """Source: UC28, UC29, UC30"""
    name: _t.Optional[str] = None

    def removeTag(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertTag(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class UserAccount:
    """Source: UC31, UC35, UC36, UC37"""
    username: _t.Optional[str] = None
    login: _t.Optional["Login"] = None
    tag: _t.Optional["Tag"] = None

    def changePassword(self) -> None:
        """Operation."""
        raise NotImplementedError

    def login(self) -> None:
        """Realizes UC37 "Ensure A Registered User To Access The System With The Privileges That Fall" (UC35)."""
        raise NotImplementedError

    def logout(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Password:
    """Source: UC31, UC32"""
    password: _t.Optional[str] = None

    def confirmPasswordChange(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Login:
    """Source: UC35, UC36"""
    username: _t.Optional[str] = None

    def loginUser(self) -> None:
        """Realizes UC37 "Ensure A Registered User To Access The System With The Privileges That Fall" (UC35)."""
        raise NotImplementedError


@_dc.dataclass
class PointOfRestaurant:
    """Source: UC38, UC39, UC40"""
    banners: _t.Optional[str] = None


@_dc.dataclass
class Restaurant:
    """Source: UC41, UC42, UC43"""
    name: _t.Optional[str] = None
    convention: _t.Optional["Convention"] = None

    def changeDailyMenu(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteDailyMenu(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeRefreshmentData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Convention:
    """Source: UC44"""
    name: _t.Optional[str] = None

    def requestConvention(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC54, UC55, UC57, UC58"""
    userId: _t.Optional[int] = None
    username: _t.Optional[str] = None
