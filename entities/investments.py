import sys
import pandas as pd
from dataclasses import dataclass
from datetime import date
from entities.constants import VariableRentTypes, Sectors
from entities.investment_attributes import Rent
from abc import abstractmethod
from pydantic import BaseModel

sys.path.append("../entities")


class Investment(BaseModel):
    title: str
    unitary_value: float
    amount: int
    acquisition: date

    @abstractmethod
    def current_value(self) -> float:
        pass


class FixedRent(BaseModel):
    title: str
    unitary_value: float
    amount: int
    acquisition: date
    rent: Rent
    liquidity: int
    due_date: date
    pay_tax: bool = True

    def current_value(self):
        ...


class VariableRent(BaseModel):
    title: str
    unitary_value: float
    amount: int
    acquisition: date
    type: VariableRentTypes
    company: str
    sector: Sectors
    has_dividend: bool = False

    def current_value(self) -> float:
        ...
