from typing import Optional
from datetime import date
from pydantic import BaseModel

class StockPrices (BaseModel):
    id: Optional[int]
    date: date
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: int