from pydantic import BaseModel
from pydantic.datetime_parse import date,datetime

class TypeBase(BaseModel):
    name:str



class CreateType(TypeBase):
    date:datetime


class UpdateType(TypeBase):
    id:int
    status:bool=True
    date: datetime