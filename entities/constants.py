from enum import Enum


class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __str__(self):
        return self.value


class InvestmentTypes(OrderedEnum):
    FIXED_RENT = "fixed rent"
    VARIABLE_RENT = "variable rent"


class VariableRentTypes(OrderedEnum):
    STOCK = "stock"
    REAL_STATE_INVESTMENT_FUND = "real state investment fund"


class Sectors(OrderedEnum):
    BANKING = "banking"
    MINING = "mining"
    RETAIL = "retail"
    ENERGY = "energy"
    PAPER_FUND = "paper fund"


class BaseRates(OrderedEnum):
    SELIC = "selic"
    CDB = "cdb"
    IPCA = "ipca"
    CDI = "cdi"


class Coin(OrderedEnum):
    USD = "us"
    BRL = "brl"


class StockExchanges(OrderedEnum):
    B3 = "b3"


class ExchangeRegion(OrderedEnum):
    SAO_PAULO = "SAO"


class ExchangeOperation(OrderedEnum):
    BUY = "buy"
    SELL = "sell"
    DUE_DATE = "due date"
    TRANSFER = "transfer"


class InvestmentNature(OrderedEnum):
    FIXED = "fixed"
    VARIABLE = "variable"
