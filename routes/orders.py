from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import get_db
from functions.orders import *
from schemas.orders import CreateOrders,UpdateOrders,OrdersBase
from pydantic.datetime_parse import date
user_router = APIRouter()


@user_router.post("/add")
def order_qoshish(form:CreateOrders,db:Session=Depends(get_db)):
    return add_orders(form=form,db=db)

@user_router.get('/')
def get_orders(search:str=None,status:bool=True,id:int=0,start_date:date=datetime.datetime.now().date().min,end_date:date=datetime.datetime.now().date().min,page:int=1,limit:int=2, db: Session=Depends(get_db)):
    if id:
        return one_order(id=id,db=db)
    else:
        return all_orders(search=search,status=status,start_date=start_date,end_date=end_date,page=page,limit=limit,db=db)


@user_router.put("/update")
def order_update(form:UpdateOrders,db:Session=Depends(get_db)):
    return update_order(form=form,db=db)


@user_router.delete("/delete")
def order_delete(id:int,db:Session=Depends(get_db)):
    return delete_order(id=id,db=db)