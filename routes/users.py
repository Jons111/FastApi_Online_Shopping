from fastapi import APIRouter,Depends
from pydantic.datetime_parse import date
from sqlalchemy.orm import Session
from db import get_db
from functions.users import add_user,one_user,read_users,update_user,delete_user,all_users
from schemas.users import CreateUsers,UsersBase,UpdateUsers
import datetime

user_router = APIRouter()


@user_router.post("/add")
def user_qoshish(form:CreateUsers,db:Session=Depends(get_db)):
    return add_user(form=form,db=db)

@user_router.get('/')
def get_users(search:str=None,title:str=None,status:bool=True,id:int=0,start_date:date=datetime.datetime.now().date().min,end_date:date=datetime.datetime.now().date(),page:int=1,limit:int=20, db: Session=Depends(get_db)):
    if id:
        return one_user(id=id,db=db)
    else:
        return all_users(search=search,title=title,status=status,start_date=start_date,end_date=end_date,db=db,page=page,limit=limit)



@user_router.put("/update")
def user_update(form:UpdateUsers,db:Session=Depends(get_db)):
    return update_user(form=form,db=db)


@user_router.delete("/delete")
def user_delete(id:int,db:Session=Depends(get_db)):
    return delete_user(id=id,db=db)