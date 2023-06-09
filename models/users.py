from db import Base

from sqlalchemy import Column,Integer,String,Float,DateTime,func,Boolean

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String(20),nullable=False)
    phone = Column(String(20),nullable=False)
    title = Column(String(20),nullable=False)
    date = Column(DateTime(timezone=True),default=func.now(),nullable=False)
    status = Column(Boolean,default=True)