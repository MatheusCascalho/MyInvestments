from dataclasses import dataclass
from entities.constants import BaseRates


@dataclass
class Rent:
    base_rent: BaseRates
    extra_rate: float

    def to_monthly(self) -> float:
        ...

    def total(self) -> float:
        ...

