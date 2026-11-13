"""Code skeleton generated from the shared model of D1/ticket.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class User:
    """Source: R1, R6, R7, R8, R9, R10, R44, R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    dateOfBirth: _t.Optional[str] = None
    email: _t.Optional[str] = None
    address: _t.Optional[str] = None
    preferences: _t.Optional[str] = None
    bankAccount: _t.Optional[str] = None
    preference: _t.Optional["Preference"] = None

    def createUser(self) -> None:
        """Realizes UC1 "Save Information" (R1, R17)."""
        raise NotImplementedError

    def changePassword(self) -> None:
        """Realizes UC2 "Change Password" (R6)."""
        raise NotImplementedError

    def editInformation(self) -> None:
        """Realizes UC3 "Edit Information" (R7)."""
        raise NotImplementedError

    def seeHistory(self) -> None:
        """Realizes UC4 "See History" (R8)."""
        raise NotImplementedError

    def seeOverview(self) -> None:
        """Realizes UC5 "See Overview" (R9)."""
        raise NotImplementedError

    def seePreference(self) -> None:
        """Realizes UC6 "See Preference" (R5)."""
        raise NotImplementedError

    def fillInformation(self) -> None:
        """Realizes UC33 "Fill Information" (R16)."""
        raise NotImplementedError

    def fillName(self) -> None:
        """Realizes UC34 "Fill Name" (R15)."""
        raise NotImplementedError

    def fillSurvey(self) -> None:
        """Realizes UC35 "Fill Survey" (R3)."""
        raise NotImplementedError


@_dc.dataclass
class Address:
    """Source: R1"""
    street: _t.Optional[str] = None
    city: _t.Optional[str] = None
    state: _t.Optional[str] = None
    zipCode: _t.Optional[str] = None


@_dc.dataclass
class Preference:
    """Source: R3, R4, R5"""
    genre: _t.Optional[str] = None
    eventTypes: _t.Optional[str] = None


@_dc.dataclass
class BankAccount:
    """Source: R45"""
    iban: _t.Optional[str] = None
