from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GlobalStatusData(_message.Message):
    __slots__ = ("bot_id", "total_tether_volume", "total_revenue", "total_finished_transaction_count", "total_bid_krw", "total_ask_krw", "current_price", "krw_gain_per_finished_transaction")
    BOT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TETHER_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REVENUE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FINISHED_TRANSACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BID_KRW_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ASK_KRW_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PRICE_FIELD_NUMBER: _ClassVar[int]
    KRW_GAIN_PER_FINISHED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    bot_id: str
    total_tether_volume: float
    total_revenue: float
    total_finished_transaction_count: int
    total_bid_krw: int
    total_ask_krw: int
    current_price: int
    krw_gain_per_finished_transaction: float
    def __init__(self, bot_id: _Optional[str] = ..., total_tether_volume: _Optional[float] = ..., total_revenue: _Optional[float] = ..., total_finished_transaction_count: _Optional[int] = ..., total_bid_krw: _Optional[int] = ..., total_ask_krw: _Optional[int] = ..., current_price: _Optional[int] = ..., krw_gain_per_finished_transaction: _Optional[float] = ...) -> None: ...

class GlobalStatusRequest(_message.Message):
    __slots__ = ("db_auth", "bot_id")
    DB_AUTH_FIELD_NUMBER: _ClassVar[int]
    BOT_ID_FIELD_NUMBER: _ClassVar[int]
    db_auth: str
    bot_id: str
    def __init__(self, db_auth: _Optional[str] = ..., bot_id: _Optional[str] = ...) -> None: ...
