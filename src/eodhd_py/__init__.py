"""Package allows for querying the EODHD API using an async interface."""

from eodhd_py.base import EodhdApiConfig
from eodhd_py.client import EodhdApi
from eodhd_py.api.dividends import DividendsApi
from eodhd_py.api.earnings import EarningsApi
from eodhd_py.api.eod_historical import EodHistoricalApi
from eodhd_py.api.exchanges import ExchangesApi
from eodhd_py.api.intraday_historical import IntradayHistoricalApi
from eodhd_py.api.ipos import IposApi
from eodhd_py.api.user import UserApi

__all__ = (
    "DividendsApi",
    "EarningsApi",
    "EodHistoricalApi",
    "EodhdApi",
    "EodhdApiConfig",
    "ExchangesApi",
    "IntradayHistoricalApi",
    "IposApi",
    "UserApi",
)
