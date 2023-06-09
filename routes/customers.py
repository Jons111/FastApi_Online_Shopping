import datetime

from fastapi import APIRouter,Depends
from pydantic.datetime_parse import date
from sqlalchemy.orm import Session
from db import get_db
from functions.customers import *
from schemas.customers import CustomersBase,CreateCustomer,UpdateCustomer

user_router = APIRouter()


@user_router.post("/add")
def customer_qoshish(form:CreateCustomer,db:Session=Depends(get_db)):
    return add_customers(form=form,db=db)

@user_router.get('/')
def get_customers(search:str=None,status:bool=True,id:int=0,start_date:date=datetime.datetime.now().date().min,end_date:date=datetime.datetime.now().date(),page:int=1,limit:int=2, db: Session=Depends(get_db)):
    if id:
        return one_customer(id=id,db=db)
    else:
        return all_customers(search=search,status=status,start_date=start_date,end_date=end_date,db=db,page=page,limit=limit)


@user_router.put("/update")
def customer_update(form:UpdateCustomer,db:Session=Depends(get_db)):
    return update_customer(form=form,db=db)


@user_router.delete("/delete")
def customer_delete(id:int,db:Session=Depends(get_db)):
    return delete_customer(id=id,db=db)