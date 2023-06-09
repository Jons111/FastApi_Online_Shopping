from fastapi import HTTPException

from models.customers import Customers
import datetime

from utils.pageination import pageination

def all_customers(search, status, start_date, end_date, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Customers.name.like(search_formatted)|\
                        Customers.phone.like(search_formatted)|Customers.address.like(search_formatted)
    else:
        search_filter = Customers.id > 0

    if status in [True,False]:
        status_filter = Customers.status == status
    else:
        status_filter = Customers.status.in_([True,False])

    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date),"%Y-%m-%d").date() + datetime.timedelta(days = 1)
    except Exception as error:
        raise HTTPException(status_code=400,detail="Faqat yyy-mmm-dd formatida yozing")
    dones = db.query(Customers).filter(Customers.date > start_date).filter(
        Customers.date <= end_date).filter(search_filter,status_filter).order_by(Customers.id.desc())
    if page and limit:
        return pageination(dones,page,limit)
    else:
        return dones.all()



def add_customers(form,db):
    new_customers = Customers(
        name = form.name,
        phone = form.phone,
        address = form.address,
        date = form.date,
    )
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    return {"date":"Customers saqlandi"}


def read_customers(db):
    customers = db.query(Customers).all()
    return customers

def one_customer(id:int, db):
    customer = db.query(Customers).filter(Customers.id == id).first()
    return customer

def update_customer(form,db):
    customer = db.query(Customers).filter(Customers.id == form.id).update(
        {
            Customers.id:form.id,
            Customers.name:form.name,
            Customers.phone:form.phone,
            Customers.address:form.address,
            Customers.status:form.status,
        }
    )
    db.commit()
    return {"date":"Ma'lumot o'zgartirildi"}

def delete_customer(id:int,db):
    customer = db.query(Customers).filter(Customers.id==id).update(
        {
            Customers.status:False
        }
    )
    db.commit()
    return {'date':"Ma'lumot o'chirildi"}