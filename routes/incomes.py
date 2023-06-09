from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import get_db
from functions.incomes import *
from schemas.incomes import IncomesBase,CreateIncomes,UpdateIncomes
from pydantic.datetime_parse import date
user_router = APIRouter()


@user_router.post("/add")
def income_qoshish(form:CreateIncomes,db:Session=Depends(get_db)):
    return add_incomes(form=form,db=db)

@user_router.get('/')
def get_income(search:str=None,status:bool=True,id:int=0,start_date:date=datetime.datetime.now().date().min,end_date:date=datetime.datetime.now().date().min,page:int=1,limit:int=2, db: Session=Depends(get_db)):
    if id:
        return one_incomes(id=id,db=db)
    else:
        return all_incomes(search=search,status=status,start_date=start_date,end_date=end_date,page=page,limit=limit,db=db)


@user_router.put("/update")
def income_update(form:UpdateIncomes,db:Session=Depends(get_db)):
    return update_incomes(form=form,db=db)


@user_router.delete("/delete")
def income_delete(id:int,db:Session=Depends(get_db)):
    return delete_incomes(id=id,db=db)