from pydantic import BaseModel
from pydantic.datetime_parse import date, datetime


class UsersBase(BaseModel):
    name: str
    phone:int
    title:str


class CreateUsers(UsersBase):
    date: datetime


class UpdateUsers(UsersBase):
    id: int
    status: bool = True
    date: datetime

class UserCurrent(BaseModel):
    id:int
    name: str
    username: str
    password:str
    roll: str
    status: bool