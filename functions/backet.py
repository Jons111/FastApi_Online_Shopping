import datetime

from fastapi import HTTPException

from models.backet import Backet
from utils.pageination import pageination


def all_backet(search, status, start_date, end_date, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Backet.name.like(search_formatted)
    else:
        search_filter = Backet.id > 0

    if status in [True,False]:
        status_filter = Backet.status == status
    else:
        status_filter = Backet.status.in_([True,False])

    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date),"%Y-%m-%d").date() + datetime.timedelta(days = 1)
    except Exception as error:
        raise HTTPException(status_code=400,detail="Faqat yyy-mmm-dd formatida yozing")
    dones = db.query(Backet).filter(Backet.date > start_date).filter(
        Backet.date <= end_date).filter(search_filter,status_filter).order_by(Backet.id.desc())
    if page and limit:
        return pageination(dones,page,limit)
    else:
        return dones.all()







def add_backet(form,db):
    new_backet = Backet(
        name = form.name,
        quantity = form.quantitiy,
        order_id = form.order_id,
        user_id = form.user_id,
        date = form.date,
    )
    db.add(new_backet)
    db.commit()
    db.refresh(new_backet)
    return {"date":"Backet saqlandi"}


def read_backet(db):
    backet = db.query(Backet).all()
    return backet

def one_backet(id:int, db):
    backet = db.query(Backet).filter(Backet.id == id).first()
    return backet

def update_backet(form,db):
    backet = db.query(Backet).filter(Backet.id == form.id).update(
        {
            Backet.id:form.id,
            Backet.name:form.name,
            Backet.quantity:form.quantity,
            Backet.order_id:form.order_id,
            Backet.user_id:form.user_id,
            Backet.status:form.status,
        }
    )
    db.commit()
    return {"date":"Ma'lumot o'zgartirildi"}

def delete_backet(id:int,db):
    backet = db.query(Backet).filter(Backet.id==id).update(
        {
            Backet.status:False
        }
    )
    db.commit()
    return {'date':"Ma'lumot o'chirildi"}