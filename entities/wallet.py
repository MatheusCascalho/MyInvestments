from typing import List, Tuple, Dict, NoReturn
from entities.investments import FixedRent, VariableRent
from entities.constants import InvestmentTypes, Coin, BaseRates
from datetime import date
import pandas as pd
from pydantic import BaseModel


class Wallet(BaseModel):
    money_not_applied: float
    rate_table: Dict[BaseRates, float]
    target: float
    creation: date
    description: str = str()
    fixed_rents: Tuple[FixedRent] = tuple()
    variable_rents: Tuple[VariableRent] = tuple()
    coin: Coin = Coin.BRL

    def total(self) -> float:
        ...

    def __repr__(self):
        return f"Wallet with {self.coin} {self.total()}"

    def current_profit(self) -> float:
        ...

    def current_tax(self) -> float:
        ...

    def profit_by_sector(self) -> pd.DataFrame:
        ...

    def profit_over_base_rate(self, base_rate: BaseRates):
        ...

    def history(self) -> pd.DataFrame:
        ...

    def save(self) -> NoReturn:
        ...


class WalletReport(BaseModel):
    balance: float
    profit: float
    taxes: float
