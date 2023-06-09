from db import Base

from sqlalchemy import Column,Integer,String,Float,DateTime,func,Boolean

class Products_Types(Base):
    __tablename__ = "Products_Types"
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String(20),nullable=False)
    date = Column(DateTime(timezone=True),default=func.now(),nullable=False)
    status = Column(Boolean,default=True)