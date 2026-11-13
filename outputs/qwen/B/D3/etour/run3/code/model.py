"""Code skeleton generated from the shared model of D3/etour.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Agency:
    """Source: -"""
    useCases: _t.List["UseCase"] = _dc.field(default_factory=list)
    culturalHeritages: _t.List["CulturalHeritage"] = _dc.field(default_factory=list)
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)
    touristAccounts: _t.List["TouristAccount"] = _dc.field(default_factory=list)
    tourists: _t.List["Tourist"] = _dc.field(default_factory=list)
    sites: _t.List["Site"] = _dc.field(default_factory=list)
    comments: _t.List["Comment"] = _dc.field(default_factory=list)
    agencyOperator: _t.Optional["AgencyOperator"] = None

    def logIn(self) -> None:
        """Operation."""
        raise NotImplementedError

    def logOut(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CulturalHeritage:
    """Source: UC4, UC10"""
    name: _t.Optional[str] = None
    description: _t.Optional[str] = None


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC8, UC9, UC10, UC11"""
    name: _t.Optional[str] = None
    address: _t.Optional[str] = None
    status: _t.Optional[str] = None

    def searchRefreshmentPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def checkBanners(self) -> None:
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
    username: _t.Optional[str] = None
    status: _t.Optional[str] = None


@_dc.dataclass
class UseCase:
    """Source: UC1, UC2, UC3, UC4, UC5, UC6, UC7, UC8, UC9, UC10, UC11, UC12, UC13, UC14"""
    pass


@_dc.dataclass
class SearchCulturalHeritage:
    """Source: UC4, UC10"""
    pass


@_dc.dataclass
class SearchRefreshmentPoint:
    """Source: UC9, UC10"""
    pass


@_dc.dataclass
class SearchTourist:
    """Source: UC14"""
    pass


@_dc.dataclass
class Delete:
    """Source: UC1, UC6"""

    def deleteCulturalHeritage(self) -> None:
        """Realizes UC1 "Delete Cultural Object" (UC1)."""
        raise NotImplementedError

    def deleteRefreshmentPoint(self) -> None:
        """Realizes UC6 "Delete Refreshment Point" (UC6)."""
        raise NotImplementedError


@_dc.dataclass
class Insert:
    """Source: UC2"""

    def insertCulturalHeritage(self) -> None:
        """Realizes UC2 "Insert Cultural Object" (UC2)."""
        raise NotImplementedError


@_dc.dataclass
class Change:
    """Source: UC3"""

    def changeCulturalHeritageData(self) -> None:
        """Realizes UC3 "Change Cultural Object Data" (UC3)."""
        raise NotImplementedError


@_dc.dataclass
class View:
    """Source: UC5, UC10, UC12"""

    def viewCulturalHeritageDetails(self) -> None:
        """Realizes UC5 "View Cultural Object Details" (UC5, UC10)."""
        raise NotImplementedError

    def viewRefreshmentPointDetails(self) -> None:
        """Realizes UC10 "View Refreshment Point Details" (UC10)."""
        raise NotImplementedError

    def viewTouristAccountDetails(self) -> None:
        """Realizes UC12 "View Tourist Account Details" (UC12)."""
        raise NotImplementedError


@_dc.dataclass
class ActivateConvention:
    """Source: UC7"""

    def activateConventionAtRefreshmentPoint(self) -> None:
        """Realizes UC7 "Activate Convention At Refreshment Point" (UC7)."""
        raise NotImplementedError


@_dc.dataclass
class Edit:
    """Source: UC8"""

    def editRefreshmentPointData(self) -> None:
        """Realizes UC8 "Edit Refreshment Point Data" (UC8)."""
        raise NotImplementedError


@_dc.dataclass
class Search:
    """Source: UC4, UC9, UC14"""

    def searchCulturalHeritage(self) -> None:
        """Realizes UC4 "Search Cultural Heritage" (UC4, UC9)."""
        raise NotImplementedError

    def searchRefreshmentPoint(self) -> None:
        """Realizes UC9 "Search Refreshment Point" (UC9)."""
        raise NotImplementedError

    def searchTouristAccount(self) -> None:
        """Realizes UC14 "Search Tourist Account" (UC14)."""
        raise NotImplementedError


@_dc.dataclass
class EnableDisable:
    """Source: UC13"""

    def enableDisableTouristAccount(self) -> None:
        """Realizes UC13 "Enable Disable Tourist Account" (UC13)."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC15, UC16"""
    name: _t.Optional[str] = None
    feedback: _t.Optional["Feedback"] = None
    site: _t.Optional["Site"] = None
    position: _t.Optional["Position"] = None

    def searchTourist(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editPreferences(self) -> None:
        """Realizes UC42 "Edit Preferences" (UC48)."""
        raise NotImplementedError

    def changeData(self) -> None:
        """Realizes UC15 "Change Data" (UC15, UC23, UC47)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Realizes UC40 "View Statistic" (UC45)."""
        raise NotImplementedError

    def viewFavoriteList(self) -> None:
        """Realizes UC43 "View List" (UC49, UC50)."""
        raise NotImplementedError

    def insertSite(self) -> None:
        """Realizes UC44 "Insert Site" (UC51)."""
        raise NotImplementedError

    def deleteSite(self) -> None:
        """Realizes UC45 "Delete Site" (UC52)."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
        """Realizes UC46 "Insert Feedback" (UC53)."""
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
        """Operation."""
        raise NotImplementedError

    def deleteNews(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editNews(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC24, UC25, UC26"""
    site: _t.Optional[str] = None
    comments: _t.Optional[str] = None

    def viewFeedback(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewReport(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class GuestUser:
    """Source: UC33, UC34, UC38"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None
    email: _t.Optional[str] = None

    def register(self) -> None:
        """Realizes UC31 "Require Creation" (UC33)."""
        raise NotImplementedError

    def login(self) -> None:
        """Realizes UC33 "Supply Login" (UC36)."""
        raise NotImplementedError

    def searchHeritage(self) -> None:
        """Realizes UC32 "Research Heritage" (UC34)."""
        raise NotImplementedError

    def searchSite(self) -> None:
        """Realizes UC26 "Search Site" (UC27)."""
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
        """Realizes UC34 "Change Password" (UC31)."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: UC37, UC38, UC39, UC40"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def endSession(self) -> None:
        """Realizes UC35 "End Session" (UC37)."""
        raise NotImplementedError

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
        """Realizes UC36 "Change Menu" (UC41)."""
        raise NotImplementedError

    def deleteMenu(self) -> None:
        """Realizes UC37 "Delete Menu" (UC42)."""
        raise NotImplementedError

    def changeDataPoint(self) -> None:
        """Realizes UC38 "Change Data Point" (UC43)."""
        raise NotImplementedError

    def requireConvention(self) -> None:
        """Realizes UC39 "Require Convention" (UC44)."""
        raise NotImplementedError


@_dc.dataclass
class SearchTag:
    """Source: UC28, UC29, UC30"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None


@_dc.dataclass
class TagSearch:
    """Source: UC29, UC30"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None


@_dc.dataclass
class Banner:
    """Source: UC38, UC39, UC40"""
    name: _t.Optional[str] = None
    image: _t.Optional[str] = None
    position: _t.Optional[int] = None


@_dc.dataclass
class Comment:
    """Source: UC54"""
    text: _t.Optional[str] = None
    change: _t.Optional["Change"] = None

    def editComment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Site:
    """Source: UC58"""
    pass


@_dc.dataclass
class Position:
    """Source: UC56"""
    pass


@_dc.dataclass
class AdvancedSearch:
    """Source: UC57"""
    pass


@_dc.dataclass
class SearchResult:
    """Source: UC57"""
    pass
