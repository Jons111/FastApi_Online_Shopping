from fastapi import HTTPException

from models.products_types import Products_Types

import datetime

from utils.pageination import pageination


def all_types(search, status, start_date, end_date, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Products_Types.name.like(search_formatted)
    else:
        search_filter = Products_Types.id > 0

    if status in [True,False]:
        status_filter = Products_Types.status == status
    else:
        status_filter = Products_Types.status.in_([True,False])

    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date),"%Y-%m-%d").date() + datetime.timedelta(days = 1)
    except Exception as error:
        raise HTTPException(status_code=400,detail="Faqat yyy-mmm-dd formatida yozing")
    dones = db.query(Products_Types).filter(Products_Types.date > start_date).filter(
        Products_Types.date <= end_date).filter(search_filter,status_filter).order_by(Products_Types.id.desc())
    if page and limit:
        return pageination(dones,page,limit)
    else:
        return dones.all()







def add_product_type(form,db):
    new_product_type = Products_Types(
        name = form.name,
        date = form.date,
    )
    db.add(new_product_type)
    db.commit()
    db.refresh(new_product_type)
    return {"date":"Type saqlandi"}


def read_products_type(db):
    read_products_types = db.query(Products_Types).all()
    return read_products_types

def one_product_type(id:int, db):
    product_type = db.query(Products_Types).filter(Products_Types.id == id).first()
    return product_type

def update_product_type(form,db):
    product_type = db.query(Products_Types).filter(Products_Types.id == form.id).update(
        {
            Products_Types.id:form.id,
            Products_Types.name:form.name,
            Products_Types.status:form.status,
        }
    )
    db.commit()
    return {"date":"Ma'lumot o'zgartirildi"}

def delete_product_type(id:int,db):
    product_type = db.query(Products_Types).filter(Products_Types.id==id).update(
        {
            Products_Types.status:False
        }
    )
    db.commit()
    return {'date':"Ma'lumot o'chirildi"}