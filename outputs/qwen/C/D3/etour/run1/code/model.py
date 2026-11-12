"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Agency:
    """Source: -"""
    tourists: _t.List["Tourist"] = _dc.field(default_factory=list)
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)
    sites: _t.List["Site"] = _dc.field(default_factory=list)


@_dc.dataclass
class AccountTourist:
    """Source: UC13"""
    name: _t.Optional[str] = None

    def enableDisableAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Cultural:
    """Source: UC1, UC2, UC3, UC4, UC5"""
    name: _t.Optional[str] = None

    def deleteCultural(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertCultural(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeCulturalData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchCultural(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewCulturalDetails(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC7, UC8, UC9, UC10, UC11"""
    name: _t.Optional[str] = None

    def deleteRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def activateConvention(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeRefreshmentData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewRefreshmentDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewRefreshmentHistory(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC12, UC14"""
    id: _t.Optional[int] = None
    authenticated: _t.Optional[bool] = None
    feedback: _t.Optional["Feedback"] = None

    def viewTouristDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchTourist(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifySearchPreferences(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyAccountData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyGeneralPreferences(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewFavoritesList(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewVisitedSitesList(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertBookmark(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeBookmark(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class BannerAd:
    """Source: UC17, UC19, UC20"""
    image: _t.Optional[str] = None

    def changeImage(self) -> None:
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
class Feedback:
    """Source: UC26"""
    comment: _t.Optional[str] = None
    touristId: _t.Optional[int] = None
    siteId: _t.Optional[int] = None

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Location:
    """Source: UC25"""
    name: _t.Optional[str] = None

    def viewStatisticalReport(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Game:
    """Source: -"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC18 "Create Game" (UC27)."""
        raise NotImplementedError


@_dc.dataclass
class SearchTag:
    """Source: UC27, UC28, UC29"""

    def removeSearchTag(self) -> None:
        """Realizes UC19 "Remove Search Tag" (UC28)."""
        raise NotImplementedError

    def insertTagSearch(self) -> None:
        """Realizes UC20 "Insert Tag Search" (UC30)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC30, UC31, UC32, UC33, UC34, UC35, UC36, UC37, UC38, UC39, UC40"""

    def changePassword(self) -> None:
        """Realizes UC21 "Change Password" (UC31)."""
        raise NotImplementedError

    def requireCreation(self) -> None:
        """Realizes UC23 "Require Creation" (UC33)."""
        raise NotImplementedError

    def supplyLogin(self) -> None:
        """Realizes UC26 "Supply Login" (UC35)."""
        raise NotImplementedError

    def researchHeritage(self) -> None:
        """Realizes UC24 "Research Heritage" (UC34)."""
        raise NotImplementedError

    def searchSite(self) -> None:
        """Realizes UC25 "Search Site" (UC27)."""
        raise NotImplementedError

    def endSession(self) -> None:
        """Realizes UC27 "End Session" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: UC38, UC39, UC40"""

    def insertBanner(self) -> None:
        """Realizes UC12 "Insert Banner" (R20, UC38)."""
        raise NotImplementedError

    def changeImage(self) -> None:
        """Realizes UC16 "Change Image" (R17, UC39)."""
        raise NotImplementedError

    def deleteBannerAd(self) -> None:
        """Realizes UC9 "Delete Banner Ad" (R19, UC40)."""
        raise NotImplementedError

    def activateEditingMenu(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteMenuSelection(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeRefreshmentData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def requestConvention(self) -> None:
        """Operation."""
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


@_dc.dataclass
class AdvancedSearch:
    """Source: UC57"""
    criteria: _t.Optional[str] = None


@_dc.dataclass
class Site:
    """Source: UC58"""
    id: _t.Optional[int] = None
    name: _t.Optional[str] = None
