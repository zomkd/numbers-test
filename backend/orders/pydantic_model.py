from datetime import datetime
from pydantic import BaseModel, Field


class Order(BaseModel):
    num: int = Field(alias='№')
    order_num: int = Field(alias='заказ №')
    dollar_price: int = Field(alias='стоимость,$')
    ruble_price: int = Field(alias='стоимость, руб')
    delivery_time: datetime = Field(alias='срок поставки')
    