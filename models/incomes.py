from db import Base

from sqlalchemy import Column, Integer, String, Float, DateTime, func, Boolean, ForeignKey


class Incomes(Base):
    __tablename__ = "Incomes"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    price = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer,ForeignKey("Orders.id"),nullable=False)
    date = Column(DateTime(timezone=True),default=func.now(),nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    status = Column(Boolean,default=True)