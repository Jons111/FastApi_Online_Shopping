from pydantic import BaseModel
from pydantic.datetime_parse import date,datetime

class BacketBase(BaseModel):
    name:str
    quantity:int
    order_id:int
    user_id:int



class CreateBacket(BacketBase):
    date:datetime



class UpdateBacket(BacketBase):
    id:int
    status:bool=True
    date: datetime