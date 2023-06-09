from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import get_db
from functions.product_types import *
from schemas.products_types import TypeBase,UpdateType,CreateType
from pydantic.datetime_parse import date
import datetime
user_router = APIRouter()


@user_router.post("/add")
def type_qoshish(form:CreateType,db:Session=Depends(get_db)):
    return add_product_type(form=form,db=db)

@user_router.get('/')
def get_types(search:str=None,status:bool=True,id:int=0,start_date:date=datetime.datetime.now().date().min,end_date:date=datetime.datetime.now().date().min,page:int=1,limit:int=2, db: Session=Depends(get_db)):
    if id:
        return one_product_type(id=id,db=db)
    else:
        return all_types(search=search,status=status,start_date=start_date,end_date=end_date,page=page,limit=limit,db=db)


@user_router.put("/update")
def type_update(form:UpdateType,db:Session=Depends(get_db)):
    return update_product_type(form=form,db=db)


@user_router.delete("/delete")
def type_delete(id:int,db:Session=Depends(get_db)):
    return delete_product_type(id=id,db=db)