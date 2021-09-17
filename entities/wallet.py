from typing import List, Tuple, Dict, NoReturn, Optional
from entities.investments import FixedRent, VariableRent
from entities.constants import InvestmentTypes, Coin, BaseRates
from datetime import date
import pandas as pd
from pydantic import BaseModel, Field


class Wallet(BaseModel):
    money_not_applied: float
    rate_table: Dict[BaseRates, float]
    target: float
    creation: date
    description: str = str()
    fixed_rents: Optional[List[FixedRent]] = Field(default_factory=tuple)
    variable_rents: Optional[List[VariableRent]] = Field(default_factory=tuple)
    coin: Coin = Coin.BRL

    def update_investment_values(self):
        for investment in self.variable_rents:
            investment.update_history()

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
