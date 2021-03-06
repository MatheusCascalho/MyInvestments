from entities.investments import (
    FixedRent,
    VariableRent,
    VariableRentTypes,
    Sectors
)
from entities.wallet import Wallet
from entities.investment_attributes import Rent, BaseRates
from datetime import datetime


import json
from enum import Enum
from typing import Any
from dataclasses import is_dataclass, asdict



if __name__ == '__main__':
    selic = FixedRent(
        title="SELIC 2025",
        unitary_value=108.21,
        amount=29,
        acquisition=datetime.strptime("01/01/2020", "%d/%m/%Y"),
        rent=Rent(base_rent=BaseRates.SELIC, extra_rate=0.2),
        liquidity=1,
        due_date=datetime.strptime("01/01/2020", "%d/%m/%Y"),
        pay_tax=True
    )

    taee11 = VariableRent(
        title="TAEE11",
        unitary_value=37.32,
        amount=10,
        acquisition=datetime.strptime("01/01/2020", "%d/%m/%Y"),
        type=VariableRentTypes.STOCK,
        company="Taesa",
        sector=Sectors.ENERGY,
        has_dividend=True
    )

    rate_table = {
        BaseRates.SELIC.value: 5.25
    }

    marriage_wallet = Wallet(
        money_not_applied=300,
        rate_table=rate_table,
        target=11_500.,
        creation=datetime.strptime("01/01/2020", "%d/%m/%Y"),
        description="Carteira de casamento",
        fixed_rents=tuple([selic]),
        variable_rents=tuple([taee11])
    )


    with open('data.json', 'w') as output:
        json.dump(marriage_wallet.__dict__, output, cls=Encoder, indent=2, ensure_ascii=False)
