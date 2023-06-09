from fastapi import APIRouter,Depends
from pydantic.datetime_parse import date
from sqlalchemy.orm import Session
from db import get_db
from functions.backet import *
from schemas.backet import CreateBacket,BacketBase,UpdateBacket

user_router = APIRouter()


@user_router.post("/add")
def backet_qoshish(form:CreateBacket,db:Session=Depends(get_db)):
    return add_backet(form=form,db=db)

@user_router.get('/')
def get_backets(search:str=None,status:bool=True,id:int=0,start_date:date=datetime.datetime.now().date().min,end_date:date=datetime.datetime.now().date().min,page:int=1,limit:int=2, db: Session=Depends(get_db)):
    if id:
        return one_backet(id=id,db=db)
    else:
        return all_backet(search=search,status=status,start_date=start_date,end_date=end_date,page=page,limit=limit,db=db)


@user_router.put("/update")
def backet_update(form:UpdateBacket,db:Session=Depends(get_db)):
    return update_backet(form=form,db=db)


@user_router.delete("/delete")
def backet_delete(id:int,db:Session=Depends(get_db)):
    return delete_backet(id=id,db=db)