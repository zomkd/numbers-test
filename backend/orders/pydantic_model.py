from datetime import datetime
from pydantic import BaseModel


class Order(BaseModel):
    num: int
    order_num: int
    dollar_price: int
    ruble_price: int
    delivery_time: datetime.time