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
    tourists: _t.List["Tourist"] = _dc.field(default_factory=list)
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)
    culturalHeritages: _t.List["CulturalHeritage"] = _dc.field(default_factory=list)
    games: _t.List["Game"] = _dc.field(default_factory=list)

    def deleteAccount(self) -> None:
        """Realizes UC8 "Delete Account" (UC16)."""
        raise NotImplementedError

    def changeData(self) -> None:
        """Realizes UC3 "Change Data" (R3, UC15, UC23)."""
        raise NotImplementedError

    def viewReport(self) -> None:
        """Realizes UC16 "View Report" (UC25)."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC17 "Edit Comment" (R1, UC26)."""
        raise NotImplementedError


@_dc.dataclass
class Tourist:
    """Source: UC12, UC13, UC14"""
    name: _t.Optional[str] = None
    account: _t.Optional[str] = None
    id: _t.Optional[int] = None
    area: _t.Optional[str] = None
    feedbacks: _t.List["Feedback"] = _dc.field(default_factory=list)
    bookmarks: _t.List["Bookmark"] = _dc.field(default_factory=list)
    searchPreference: _t.Optional["SearchPreference"] = None
    useCases: _t.List["UseCase"] = _dc.field(default_factory=list)

    def viewDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def enableDisableAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def search(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeData(self) -> None:
        """Realizes UC3 "Change Data" (R3, UC15, UC23)."""
        raise NotImplementedError

    def deleteAccount(self) -> None:
        """Realizes UC8 "Delete Account" (UC16)."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: UC13"""
    isActive: _t.Optional[bool] = None

    def changeData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CulturalHeritage:
    """Source: UC1, UC3, UC4, UC5"""
    name: _t.Optional[str] = None
    details: _t.Optional[str] = None

    def delete(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def search(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RefreshmentPoint:
    """Source: UC6, UC8, UC9, UC10, UC11"""
    name: _t.Optional[str] = None
    details: _t.Optional[str] = None

    def delete(self) -> None:
        """Operation."""
        raise NotImplementedError

    def changeData(self) -> None:
        """Operation."""
        raise NotImplementedError

    def search(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewHistory(self) -> None:
        """Operation."""
        raise NotImplementedError

    def checkPoint(self) -> None:
        """Realizes UC10 "Check Point" (UC18)."""
        raise NotImplementedError

    def insertBanner(self) -> None:
        """Realizes UC12 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def deleteBanner(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class UseCase:
    """Source: -"""
    pass


@_dc.dataclass
class BannerAd:
    """Source: UC17"""

    def changeImage(self) -> None:
        """Realizes UC9 "Change Image" (UC17, UC39)."""
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

    def changeData(self) -> None:
        """Realizes UC3 "Change Data" (R3, UC15, UC23)."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: UC24, UC25, UC26"""
    touristId: _t.Optional[int] = None
    siteId: _t.Optional[int] = None
    comment: _t.Optional["Comment"] = None

    def viewFeedback(self) -> None:
        """Realizes UC15 "View Feedback" (UC24)."""
        raise NotImplementedError

    def viewReport(self) -> None:
        """Realizes UC16 "View Report" (UC25)."""
        raise NotImplementedError

    def editComment(self) -> None:
        """Realizes UC17 "Edit Comment" (R1, UC26)."""
        raise NotImplementedError

    def insertFeedback(self) -> None:
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
    """Source: UC27, UC28, UC29, UC30"""

    def removeSearchTag(self) -> None:
        """Realizes UC19 "Remove Search Tag" (UC28)."""
        raise NotImplementedError

    def insertTagSearch(self) -> None:
        """Realizes UC20 "Insert Tag Search" (UC30)."""
        raise NotImplementedError

    def askSearchTag(self) -> None:
        """Realizes UC21 "Ask Search Tag" (UC29)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: UC31, UC32, UC33, UC34, UC35, UC36, UC37"""
    feedback: _t.Optional["Feedback"] = None

    def ensureUser(self) -> None:
        """Realizes UC23 "Ensure User" (UC35)."""
        raise NotImplementedError

    def supplyLogin(self) -> None:
        """Realizes UC24 "Supply Login" (UC36)."""
        raise NotImplementedError

    def endSession(self) -> None:
        """Realizes UC25 "End Session" (UC37)."""
        raise NotImplementedError


@_dc.dataclass
class RestaurantOperator:
    """Source: UC38, UC39, UC40"""
    agencies: _t.List["Agency"] = _dc.field(default_factory=list)

    def insertBanner(self) -> None:
        """Realizes UC12 "Insert Banner" (UC20, UC38)."""
        raise NotImplementedError

    def changeImage(self) -> None:
        """Realizes UC9 "Change Image" (UC17, UC39)."""
        raise NotImplementedError

    def deleteBannerAd(self) -> None:
        """Realizes UC11 "Delete Banner Ad" (UC19, UC40)."""
        raise NotImplementedError

    def createGame(self) -> None:
        """Realizes UC18 "Create Game" (UC27)."""
        raise NotImplementedError


@_dc.dataclass
class Restaurant:
    """Source: -"""
    menus: _t.List["Menu"] = _dc.field(default_factory=list)
    days: _t.List["Day"] = _dc.field(default_factory=list)
    refreshmentPoints: _t.List["RefreshmentPoint"] = _dc.field(default_factory=list)
    useCases: _t.List["UseCase"] = _dc.field(default_factory=list)


@_dc.dataclass
class Menu:
    """Source: UC41"""
    name: _t.Optional[str] = None

    def editMenu(self) -> None:
        """Operation."""
        raise NotImplementedError


class Day(_enum.Enum):
    """Source: UC41"""
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


@_dc.dataclass
class SearchPreference:
    """Source: UC46, UC47, UC48"""

    def editPreferences(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Bookmark:
    """Source: UC51, UC52"""

    def insertBookmark(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeBookmark(self) -> None:
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
