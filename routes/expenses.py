from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import get_db
from functions.expenses import *
from schemas.expenses import CreateExpenses,ExpensesBase,UpdateExpenses
from pydantic.datetime_parse import date
user_router = APIRouter()


@user_router.post("/add")
def expenses_qoshish(form:CreateExpenses,db:Session=Depends(get_db)):
    return add_expenses(form=form,db=db)

@user_router.get('/')
def get_expenses(search:str=None,status:bool=True,id:int=0,start_date:date=datetime.datetime.now().date().min,end_date:date=datetime.datetime.now().date().min,page:int=1,limit:int=2, db: Session=Depends(get_db)):
    if id:
        return one_expense(id=id,db=db)
    else:
        return all_expenses(search=search,status=status,start_date=start_date,end_date=end_date,page=page,limit=limit,db=db)


@user_router.put("/update")
def expenses_update(form:UpdateExpenses,db:Session=Depends(get_db)):
    return update_expenses(form=form,db=db)


@user_router.delete("/delete")
def expenses_delete(id:int,db:Session=Depends(get_db)):
    return delete_expense(id=id,db=db)