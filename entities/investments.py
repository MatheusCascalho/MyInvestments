import sys
sys.path.append("../entities")

import pandas as pd
from dataclasses import dataclass
from datetime import date
from constants import VariableRentTypes, Sectors
from investment_attributes import Rent
from abc import abstractmethod


@dataclass
class Investment:
    title: str
    unitary_value: float
    amount: int
    acquisition: date

    @abstractmethod
    def current_value(self) -> float:
        pass


@dataclass
class FixedRent(Investment):
    rent: Rent
    liquidity: int
    due_date: date
    pay_tax: bool = True

    def current_value(self):
        ...


@dataclass
class VariableRent(Investment):
    type: VariableRentTypes
    company: str
    sector: Sectors
    has_dividend: bool = False

    def current_value(self) -> float:
        ...


