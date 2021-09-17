import sys
import pandas as pd
from dataclasses import dataclass
from datetime import date
from entities.constants import VariableRentTypes, Sectors
from entities.investment_attributes import Rent, ValueRegister
from abc import abstractmethod
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, NoReturn, Tuple
from extractors.stock_stractors import download_stock_history

sys.path.append("../entities")


def id_generator():
    i = 0
    while True:
        i += 1
        yield i


generator = id_generator()


class Investment(BaseModel):
    title: str
    unitary_value: float
    amount: int
    acquisition: date

    @abstractmethod
    def current_value(self) -> float:
        pass


class FixedRent(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(generator))
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
    id: Optional[int] = Field(default_factory=lambda: next(generator))
    title: str
    unitary_value: float
    amount: int
    acquisition: date
    type: VariableRentTypes
    company: str
    sector: Sectors
    has_dividend: bool = False
    history: Optional[List[Tuple[date, float]]] = Field(default_factory=list)

    def update_history(self) -> NoReturn:
        file = download_stock_history(
            stock=self.title
        )
        history = pd.read_csv(file)
        if all([col in history.columns for col in ['open', 'close']]):
            history['mean'] = (history['open'] + history['close']) / 2
            history['timestamp'] = history['timestamp'].apply(lambda x: date.fromisoformat(x)).values
            history['month'] = history['timestamp'].apply(lambda x: x.month).values
            history['day'] = history['timestamp'].apply(lambda x: x.day).values
            history['registers'] = history[['timestamp', 'mean']].apply(
                lambda x: ValueRegister(date=x[0], value=x[1])
            )
            last_day = history['day'].values[0]
            filtered_history = history[history['day'] == last_day]
            self.history = list(filtered_history[['timestamp', 'mean']].values)[:5]
            history.to_csv(file)
        else:
            print(f"Problems to download {self.title} data")

    def current_value(self) -> float:
        if len(self.history) > 0:
            value = self.amount * self.history[0][1]
        else:
            value = self.unitary_value * self.amount
        return value


class VariableRentHistory(BaseModel):
    name: str
    history: Optional[List[Dict[date, float]]] = Field(default_factory=list)


