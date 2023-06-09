from db import Base

from sqlalchemy import Column,Integer,String,Float,DateTime,func,Boolean

class Customers(Base):
    __tablename__ = "Customers"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String(20),nullable=False)
    phone = Column(String(20),nullable=False)
    address = Column(String(30),nullable=False)
    date = Column(DateTime(timezone=True),default=func.now(),nullable=False)
    status = Column(Boolean,default=True)