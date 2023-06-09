from fastapi import FastAPI, Depends, HTTPException
from schemas.users import UsersBase,UpdateUsers,CreateUsers
from sqlalchemy.orm import Session
from models.users import Users
from db import get_db,Base
import datetime

from utils.pageination import pageination


def all_users(search, status, start_date, end_date,title, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Users.name.like(search_formatted)|\
                        Users.title.like(search_formatted)
    else:
        search_filter = Users.id > 0

    if status in [True,False]:
        status_filter = Users.status == status
    else:
        status_filter = Users.status.in_([True,False])

    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date),"%Y-%m-%d").date() + datetime.timedelta(days = 1)
    except Exception as error:
        raise HTTPException(status_code=400,detail="Faqat yyy-mmm-dd formatida yozing")
    dones = db.query(Users).filter(Users.date > start_date).filter(
        Users.date <= end_date).filter(search_filter,status_filter).order_by(Users.id.desc())
    if page and limit:
        return pageination(dones,page,limit)
    else:
        return dones.all()













def add_user(form,db):
    new_user = Users(
        name = form.name,
        phone = form.phone,
        title = form.title,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"date":"Ma'lumot saqlandi"}

def read_users(db):
    users = db.query(Users).all()
    return users

def one_user(id:int, db):
    user = db.query(Users).filter(Users.id == id).first()
    return user

def update_user(form,db):
    user = db.query(Users).filter(Users.id == form.id).update(
        {
            Users.id:form.id,
            Users.name:form.name,
            Users.phone:form.phone,
            Users.title:form.title,
            Users.status:form.status,
        }
    )
    db.commit()
    return {"date":"Ma'lumot o'zgartirildi"}

def delete_user(id:int,db):
    user = db.query(Users).filter(Users.id==id).update(
        {
            Users.status:False
        }
    )
    db.commit()
    return {'date':"Ma'lumot o'chirildi"}




