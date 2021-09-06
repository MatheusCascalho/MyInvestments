from typing import List, Tuple, Dict, NoReturn
from investments import FixedRent, VariableRent
from constants import InvestmentTypes, Coin, BaseRates
from datetime import date
import pandas as pd


class Wallet:
    def __init__(
            self,
            money_not_applied: float,
            rate_table: Dict[BaseRates, float],
            target: float,
            creation: date,
            description: str = str(),
            fixed_rents: Tuple[FixedRent] = tuple(),
            variable_rents: Tuple[VariableRent] = tuple(),
            coin: Coin = Coin.BRL
    ):
        self.money_not_applied = money_not_applied
        self.rate_table = rate_table
        self.target = target
        self.creation = creation
        self.description = description
        self.fixed_rents = list(fixed_rents)
        self.variable_rents = list(variable_rents)
        self.coin = coin

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
