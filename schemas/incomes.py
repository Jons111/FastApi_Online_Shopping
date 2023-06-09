from pydantic import BaseModel
from pydantic.datetime_parse import date, datetime


class IncomesBase(BaseModel):
    price:int
    order_id : int
    user_id : int


class CreateIncomes(IncomesBase):
    date: datetime


class UpdateIncomes(IncomesBase):
    id: int
    date: datetime
    status: bool = True