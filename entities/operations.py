from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from entities.constants import ExchangeOperation, Coin, InvestmentNature


class InvestmentOperation(BaseModel):
    id: Optional[int]
    date: datetime
    type: ExchangeOperation
    value: float
    coin: Optional[Coin] = Field(default=Coin.BRL)
    title: Optional[str]
    investment_nature: Optional[InvestmentNature]
    description: Optional[str]
