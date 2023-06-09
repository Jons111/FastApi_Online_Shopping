from pydantic import BaseModel
from pydantic.datetime_parse import date,datetime

class OrdersBase(BaseModel):
    date:datetime
    user_id:int

class CreateOrders(OrdersBase):
    date:datetime



class UpdateOrders(OrdersBase):
    id:int
    date: datetime
    status: bool = True