import pandas as pd
from dataclasses import dataclass
from datetime import date


@dataclass
class Investment:
    title: str
    unitary_value: float
    amount: int
    acquisition: date

