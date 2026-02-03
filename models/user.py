from sqlalchemy import Column, Integer, String, Boolean,DateTime
from sqlalchemy.engine import default
from sqlalchemy.sql import func
from sqlalchemy.types import DATE
from db.database import base 

class User(base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,unique = True ,index=True)
    username = Column(String,index=True)
    email = Column(String,unique = True, index = True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default = func.now())
    updated_at = Column(DateTime, default = func.now(), onupdate = func.now())
