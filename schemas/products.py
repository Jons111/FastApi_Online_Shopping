from pydantic import BaseModel
from pydantic.datetime_parse import date,datetime

class ProductBase(BaseModel):
    name:str
    birlik:str
    old_price:int
    new_price:int
    type:str


class CreateProduct(ProductBase):
    date:datetime
    user_id:int


class UpdateProduct(ProductBase):
    id:int
    status:bool=True
    date: datetime