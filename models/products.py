from db import Base

from sqlalchemy import Column, Integer, String, Float, DateTime, func, Boolean, ForeignKey


class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String(20),nullable=False)
    birlik = Column(String(20),nullable=False)
    old_price = Column(Integer, nullable=False)
    new_price = Column(Integer, nullable=False)
    type = Column(Integer,ForeignKey("Products_Types.id"),nullable=False)
    user_id = Column(Integer,ForeignKey("Users.id"),nullable=False)
    date = Column(DateTime(timezone=True),default=func.now(),nullable=False)
    status = Column(Boolean,default=True)