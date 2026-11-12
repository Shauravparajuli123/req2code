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
    newses: _t.List["News"] = _dc.field(default_factory=list)
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)

    def logIn(self) -> None:
        """Operation."""
        raise NotImplementedError

    def logOut(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CulturalHeritage:
    """Source: UC4, UC10, UC12"""
    name: _t.Optional[str] = None
    description: _t.Optional[str] = None
    location: _t.Optional[str] = None

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Search Cultural Heritage" (UC4)."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Realizes UC5 "View Cultural Object Details" (UC5)."""
        raise NotImplementedError

    def viewHistory(self) -> None:
        """Realizes UC11 "View Refreshment Point History" (UC11)."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC8, UC9, UC11"""
    name: _t.Optional[str] = None
    location: _t.Optional[str] = None
    type: _t.Optional[str] = None

    def searchRefreshmentPoint(self) -> None:
        """Realizes UC9 "Search Refreshment Point" (UC9)."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Realizes UC10 "View Refreshment Point Details" (UC10)."""
        raise NotImplementedError

    def viewHistory(self) -> None:
        """Realizes UC11 "View Refreshment Point History" (UC11)."""
        raise NotImplementedError

    def deleteRefreshmentPoint(self) -> None:
        """Realizes UC6 "Delete Refreshment Point" (UC6)."""
        raise NotImplementedError

    def activateConvention(self) -> None:
        """Realizes UC7 "Activate Convention At Refreshment Point" (UC7)."""
        raise NotImplementedError

    def editData(self) -> None:
        """Realizes UC8 "Edit Refreshment Point Data" (UC8)."""
        raise NotImplementedError

    def checkBanners(self) -> None:
        """Realizes UC18 "Check Point" (UC18)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC20 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Realizes UC19 "Delete Banner Ad" (UC19, UC40)."""
        raise NotImplementedError


@_dc.dataclass
class TouristAccount:
    """Source: UC12, UC13, UC14"""
    username: _t.Optional[str] = None
    status: _t.Optional[str] = None
    email: _t.Optional[str] = None

    def searchTouristAccount(self) -> None:
        """Realizes UC14 "Search Tourist Account" (UC14)."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Realizes UC12 "View Tourist Account Details" (UC12)."""
        raise NotImplementedError

    def enableDisableAccount(self) -> None:
        """Realizes UC13 "Enable Disable Tourist Account" (UC13)."""
        raise NotImplementedError

    def viewHistory(self) -> None:
        """Realizes UC12 "View Tourist Account Details" (UC12)."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC15, UC16"""
    name: _t.Optional[str] = None
    site: _t.Optional["Site"] = None
    feedback: _t.Optional["Feedback"] = None
    advancedSearch: _t.Optional["AdvancedSearch"] = None

    def searchTourist(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editSearchPreference(self) -> None:
        """Realizes UC40 "Edit Search Preference" (UC46)."""
        raise NotImplementedError

    def editPersonalData(self) -> None:
        """Realizes UC41 "Edit Personal Data" (UC47)."""
        raise NotImplementedError

    def editPreferences(self) -> None:
        """Realizes UC42 "Edit Preferences" (UC48)."""
        raise NotImplementedError

    def viewListFavorites(self) -> None:
        """Realizes UC43 "View List Of Favorites" (UC49)."""
        raise NotImplementedError

    def viewListSites(self) -> None:
        """Realizes UC44 "View List Of Sites" (UC50)."""
        raise NotImplementedError

    def insertSite(self) -> None:
        """Realizes UC45 "Insert Site" (UC51)."""
        raise NotImplementedError

    def deleteSite(self) -> None:
        """Realizes UC46 "Delete Site" (UC52)."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Realizes UC47 "Insert Feedback" (UC53)."""
        raise NotImplementedError


@_dc.dataclass
class BannerAd:
    """Source: UC17, UC19, UC20"""
    image: _t.Optional[str] = None


@_dc.dataclass
class News:
    """Source: UC21, UC22, UC23"""
    title: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def insertNews(self) -> None:
        """Realizes UC21 "Insert News" (UC21)."""
        raise NotImplementedError

    def deleteNews(self) -> None:
        """Realizes UC22 "Delete News" (UC22)."""
        raise NotImplementedError

    def modifyNews(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC24, UC25, UC26"""
    site: _t.Optional[str] = None
    comments: _t.Optional[str] = None
    text: _t.Optional[str] = None
    siteId: _t.Optional[int] = None

    def viewFeedback(self) -> None:
        """Realizes UC23 "View Feedback" (UC24)."""
        raise NotImplementedError

    def viewReport(self) -> None:
        """Realizes UC24 "View Report" (UC25)."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC25 "Edit Comment" (R54, UC26)."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC24, UC25, UC26"""
    name: _t.Optional[str] = None
    id: _t.Optional[int] = None
    feedback: _t.Optional["Feedback"] = None


@_dc.dataclass
class GuestUser:
    """Source: UC33, UC34, UC37"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def requireCreation(self) -> None:
        """Realizes UC33 "Require Creation" (UC33)."""
        raise NotImplementedError

    def researchHeritage(self) -> None:
        """Realizes UC34 "Research Heritage" (UC34)."""
        raise NotImplementedError


@_dc.dataclass
class RegisteredUser:
    """Source: UC35, UC36, UC37"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def supplyLogin(self) -> None:
        """Realizes UC31 "Supply Login" (UC36)."""
        raise NotImplementedError

    def endSession(self) -> None:
        """Realizes UC32 "End Session" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class AgencyOperator:
    """Source: UC28, UC29, UC30, UC31"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def removeSearchTag(self) -> None:
        """Realizes UC27 "Remove Search Tag" (UC28)."""
        raise NotImplementedError

    def askSearchTag(self) -> None:
        """Realizes UC28 "Ask Search Tag" (UC29)."""
        raise NotImplementedError

    def insertTagSearch(self) -> None:
        """Realizes UC29 "Insert Tag Search" (UC30)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: UC38, UC39, UC40"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None
    bannerAd: _t.Optional["BannerAd"] = None

    def insertBanner(self) -> None:
        """Realizes UC20 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def changeImage(self) -> None:
        """Realizes UC17 "Change Image" (UC17, UC39)."""
        raise NotImplementedError

    def deleteBannerAd(self) -> None:
        """Realizes UC19 "Delete Banner Ad" (UC19, UC40)."""
        raise NotImplementedError

    def changeMenu(self) -> None:
        """Realizes UC35 "Change Menu" (UC41)."""
        raise NotImplementedError

    def deleteMenu(self) -> None:
        """Realizes UC36 "Delete Menu" (UC42)."""
        raise NotImplementedError

    def changeDataPoint(self) -> None:
        """Realizes UC37 "Change Data Point" (UC43)."""
        raise NotImplementedError

    def requireConvention(self) -> None:
        """Realizes UC38 "Require Convention" (UC44)."""
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
class Banner:
    """Source: UC38, UC39, UC40"""
    image: _t.Optional[str] = None


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
class Position:
    """Source: UC56"""
    latitude: _t.Optional[float] = None
    longitude: _t.Optional[float] = None


@_dc.dataclass
class AdvancedSearch:
    """Source: UC57"""
    criteria: _t.Optional[str] = None


@_dc.dataclass
class User:
    """Source: UC54, UC55, UC56, UC57, UC58"""
    id: _t.Optional[int] = None
    username: _t.Optional[str] = None
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)
