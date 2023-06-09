from fastapi import Path

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine

import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

manzil = "sqlite:///"+os.path.join(BASE_DIR,'baza2.db')

engine = create_engine(url=manzil,echo=True)


SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
