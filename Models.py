from database import Base
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__="users"

    user_id=Column(String,primary_key=True,index=True,nullable=False)
    username=Column(String(50),unique=True)
    password=Column(String(50))
    email=Column(String(50),unique=True)
    created_at=Column(DateTime,default=datetime.now)

    blog=relationship("Blogs",back_populates="author")

class Blogs(Base):
    __tablename__="blogs"

    blog_id=Column(Integer,primary_key=True,nullable=False,index=True)
    title=Column(String(59),nullable=False,index=True)
    content=Column(Text,nullable=False,index=True)
    created_by=Column(Integer,ForeignKey("users.user_id"))
    created_at=Column(DateTime,default=datetime.now,index=True)
    updated_at=Column(DateTime,default=datetime.now,index=True)

    author=relationship("User",back_populates="blog")






