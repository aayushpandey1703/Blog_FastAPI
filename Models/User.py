from .database import Base
from sqlalchemy import Column, String,Integer,DateTime,Text,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__="user"

    user_id=Column(Integer,primary_key=True,nullable=False,index=True,autoincrement=True)
    username=Column(String(50),nullable=False,index=True,unique=True)
    email=Column(String(100),nullable=False,unique=True,index=True)
    password=Column(String(255),nullable=False)
    created_at=Column(DateTime,default=datetime.now)

    blog=relationship("Blog",back_populates="author")
