from db import Base

from sqlalchemy import Column, Integer, String, Float, DateTime, func, Boolean, ForeignKey


class Expenses(Base):
    __tablename__ = "Expenses"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    price = Column(Integer, primary_key=True, nullable=False)
    worker_id = Column(Integer,ForeignKey("Users.id"),nullable=False)
    source = Column(String(50),nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    date = Column(DateTime(timezone=True),default=func.now(),nullable=False)
    comment = Column(String(100),nullable=False)
    status = Column(Boolean,default=True)