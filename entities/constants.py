from enum import Enum


class InvestmentTypes(Enum):
    FIXED_RENT = "fixed rent"
    VARIABLE_RENT = "variable rent"


class VariableRentTypes(Enum):
    STOCK = "stock"
    REAL_STATE_INVESTMENT_FUND = "real state investment fund"


class Sectors(Enum):
    BANKING = "banking"
    MINING = "mining"
    RETAIL = "retail"
    ENERGY = "energy"


class BaseRates(Enum):
    SELIC = "selic"
    CDB = "cdb"
    IPCA = "ipca"


class Coin(Enum):
    USD = "us"
    BRL = "brl"


class StockExchanges(Enum):
    B3 = "b3"

class ExchangeRegion(Enum):
    SAO_PAULO = "SAO"