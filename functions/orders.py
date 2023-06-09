from fastapi import HTTPException

from models.orders import Orders
import datetime

from utils.pageination import pageination


def all_orders(search, status, start_date, end_date, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Orders.name.like(search_formatted)
    else:
        search_filter = Orders.id > 0

    if status in [True,False]:
        status_filter = Orders.status == status
    else:
        status_filter = Orders.status.in_([True,False])

    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date),"%Y-%m-%d").date() + datetime.timedelta(days = 1)
    except Exception as error:
        raise HTTPException(status_code=400,detail="Faqat yyy-mmm-dd formatida yozing")
    dones = db.query(Orders).filter(Orders.date > start_date).filter(
        Orders.date <= end_date).filter(search_filter,status_filter).order_by(Orders.id.desc())
    if page and limit:
        return pageination(dones,page,limit)
    else:
        return dones.all()





def add_orders(form,db):
    new_order = Orders(

        user_id = form.user_id,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"date":"Order saqlandi"}


def read_order(db):
    order = db.query(Orders).all()
    return order

def one_order(id:int, db):
    order = db.query(Orders).filter(Orders.id == id).first()
    return order

def update_order(form,db):
    order = db.query(Orders).filter(Orders.id == form.id).update(
        {
            Orders.id:form.id,
            Orders.status:form.status,
            Orders.user_id:form.user_id,
        }
    )
    db.commit()
    return {"date":"Ma'lumot o'zgartirildi"}

def delete_order(id:int,db):
    order = db.query(Orders).filter(Orders.id==id).update(
        {
            Orders.status:False
        }
    )
    db.commit()
    return {'date':"Ma'lumot o'chirildi"}