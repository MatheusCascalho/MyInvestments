from pydantic import BaseModel
from typing import List, Dict
from entities.investments import VariableRent, FixedRent
from entities.graphics import Point


class AssetEvolution(BaseModel):
    title: str
    date: List[Point]


class HistoryRegister(BaseModel):
    date: str
    target: float
    credit: float
    debit: float
    balance: float
    balance_with_profit: float


class Summary(BaseModel):
    applied_value: float
    gross_profit: float
    taxes: float
    liquidity_profit: float


class WalletReport(BaseModel):
    variable_rents: List[VariableRent]
    fixed_rents: List[FixedRent]
    summary: Summary
    history: List[HistoryRegister]
    distribution_by_sector: Dict[str, float]
    distribution_by_title: Dict[str, float]
    distribution_by_nature: Dict[str, float]
    evolution_by_sector: Dict[str, float]
