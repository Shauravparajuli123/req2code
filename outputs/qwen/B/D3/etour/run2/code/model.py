"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CulturalHeritage:
    """Source: UC4, UC10, UC12"""
    name: _t.Optional[str] = None
    description: _t.Optional[str] = None
    location: _t.Optional[str] = None

    def searchCulturalHeritage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC8, UC11, UC14"""
    name: _t.Optional[str] = None
    location: _t.Optional[str] = None
    type: _t.Optional[str] = None

    def searchRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewHistory(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AccountTourist:
    """Source: UC13, UC14"""
    username: _t.Optional[str] = None
    status: _t.Optional[str] = None
    account: _t.Optional["Account"] = None

    def searchTourist(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def enableDisableAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyData(self) -> None:
        """Realizes UC3 "Change Data" (R3, UC15, UC23)."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Realizes UC8 "Delete Account" (UC16)."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: -"""
    accountTourist: _t.Optional["AccountTourist"] = None
    registeredUser: _t.Optional["RegisteredUser"] = None


@_dc.dataclass
class BannerAd:
    """Source: UC17, UC19, UC20"""
    name: _t.Optional[str] = None
    image: _t.Optional[str] = None

    def changeImage(self) -> None:
        """Realizes UC9 "Change Image" (UC17, UC39)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Realizes UC11 "Delete Banner Ad" (UC19, UC40)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC12 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""

    def insertNews(self) -> None:
        """Realizes UC13 "Insert News" (UC21)."""
        raise NotImplementedError

    def deleteNews(self) -> None:
        """Realizes UC14 "Delete News" (UC22)."""
        raise NotImplementedError

    def changeNews(self) -> None:
        """Realizes UC3 "Change Data" (R3, UC15, UC23)."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC24, UC25, UC26"""

    def viewFeedback(self) -> None:
        """Realizes UC15 "View Feedback" (UC24)."""
        raise NotImplementedError

    def viewReport(self) -> None:
        """Realizes UC16 "View Report" (UC25)."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC17 "Edit Comment" (UC26, UC54)."""
        raise NotImplementedError


@_dc.dataclass
class GuestUser:
    """Source: UC33, UC34, UC37"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def register(self) -> None:
        """Operation."""
        raise NotImplementedError

    def searchHeritage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def endSession(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RegisteredUser:
    """Source: UC35, UC37"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def login(self) -> None:
        """Operation."""
        raise NotImplementedError

    def endSession(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AgencyOperator:
    """Source: UC28, UC29, UC30, UC31"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None
    conventions: _t.List["Convention"] = _dc.field(default_factory=list)
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)

    def removeSearchTag(self) -> None:
        """Operation."""
        raise NotImplementedError

    def askSearchTag(self) -> None:
        """Operation."""
        raise NotImplementedError

    def insertTagSearch(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: UC38, UC39, UC40"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def insertBanner(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeImage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteBannerAd(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeMenu(self) -> None:
        """Realizes UC27 "Change Menu" (UC41)."""
        raise NotImplementedError

    def deleteMenu(self) -> None:
        """Realizes UC28 "Delete Menu" (UC42)."""
        raise NotImplementedError

    def changeDataPoint(self) -> None:
        """Realizes UC29 "Change Data Point" (UC43)."""
        raise NotImplementedError

    def requireConvention(self) -> None:
        """Realizes UC30 "Require Convention" (UC44)."""
        raise NotImplementedError

    def viewStatistic(self) -> None:
        """Realizes UC31 "View Statistic" (UC45)."""
        raise NotImplementedError


@_dc.dataclass
class SearchTag:
    """Source: UC28, UC29, UC30"""
    name: _t.Optional[str] = None


@_dc.dataclass
class TagSearch:
    """Source: UC29, UC30"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Image:
    """Source: UC38, UC39, UC40"""
    path: _t.Optional[str] = None


@_dc.dataclass
class Tourist:
    """Source: -"""
    searchPreference: _t.Optional["SearchPreference"] = None
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)
    sites: _t.List["Site"] = _dc.field(default_factory=list)
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)
    position: _t.Optional["Position"] = None

    def editSearchPreference(self) -> None:
        """Realizes UC32 "Edit Search Preference" (UC46)."""
        raise NotImplementedError

    def editPersonalData(self) -> None:
        """Realizes UC33 "Edit Personal Data" (UC47)."""
        raise NotImplementedError

    def editPreferences(self) -> None:
        """Realizes UC34 "Edit Preferences" (UC48)."""
        raise NotImplementedError

    def viewFavoriteList(self) -> None:
        """Realizes UC35 "View List Of Favorites" (UC49)."""
        raise NotImplementedError

    def viewSiteList(self) -> None:
        """Realizes UC36 "View List Of Sites" (UC50)."""
        raise NotImplementedError

    def insertSite(self) -> None:
        """Realizes UC37 "Insert Site" (UC51)."""
        raise NotImplementedError

    def deleteSite(self) -> None:
        """Realizes UC38 "Delete Site" (UC52)."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Realizes UC39 "Insert Feedback" (UC53)."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC17 "Edit Comment" (UC26, UC54)."""
        raise NotImplementedError

    def viewDetail(self) -> None:
        """Realizes UC5 "View Detail" (R10, R12, UC58)."""
        raise NotImplementedError


@_dc.dataclass
class Menu:
    """Source: UC41, UC42"""
    day: _t.Optional[str] = None

    def changeMenu(self) -> None:
        """Realizes UC27 "Change Menu" (UC41)."""
        raise NotImplementedError

    def deleteMenu(self) -> None:
        """Realizes UC28 "Delete Menu" (UC42)."""
        raise NotImplementedError


@_dc.dataclass
class DataPoint:
    """Source: UC43"""

    def changeDataPoint(self) -> None:
        """Realizes UC29 "Change Data Point" (UC43)."""
        raise NotImplementedError


@_dc.dataclass
class Convention:
    """Source: UC44"""

    def requireConvention(self) -> None:
        """Realizes UC30 "Require Convention" (UC44)."""
        raise NotImplementedError


@_dc.dataclass
class Statistic:
    """Source: UC45"""

    def viewStatistic(self) -> None:
        """Realizes UC31 "View Statistic" (UC45)."""
        raise NotImplementedError


@_dc.dataclass
class SearchPreference:
    """Source: UC46, UC47, UC48"""

    def editSearchPreference(self) -> None:
        """Realizes UC32 "Edit Search Preference" (UC46)."""
        raise NotImplementedError

    def editPersonalData(self) -> None:
        """Realizes UC33 "Edit Personal Data" (UC47)."""
        raise NotImplementedError

    def editPreferences(self) -> None:
        """Realizes UC34 "Edit Preferences" (UC48)."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC49, UC50, UC51, UC52, UC53"""
    feedback: _t.Optional["Feedback"] = None
    tourist: _t.Optional["Tourist"] = None

    def viewFavoriteList(self) -> None:
        """Realizes UC35 "View List Of Favorites" (UC49)."""
        raise NotImplementedError

    def viewSiteList(self) -> None:
        """Realizes UC36 "View List Of Sites" (UC50)."""
        raise NotImplementedError

    def insertSite(self) -> None:
        """Realizes UC37 "Insert Site" (UC51)."""
        raise NotImplementedError

    def deleteSite(self) -> None:
        """Realizes UC38 "Delete Site" (UC52)."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Realizes UC39 "Insert Feedback" (UC53)."""
        raise NotImplementedError

    def search(self) -> None:
        """Realizes UC18 "Search Site" (UC27, UC57)."""
        raise NotImplementedError


@_dc.dataclass
class Position:
    """Source: -"""

    def returnPosition(self) -> None:
        """Realizes UC41 "Return Position" (UC56)."""
        raise NotImplementedError
