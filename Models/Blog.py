from .database import Base
from sqlalchemy import Column, String,DateTime,Text,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Blog(Base):
    __tablename__="blog"
     
    blog_id=Column(String(255),primary_key=True,nullable=False,index=True)
    title=Column(String(50),nullable=False,index=True)
    content=Column(Text,nullable=False,index=True)
    created_by=Column(String,ForeignKey("user.user_id"))
    created_at=Column(DateTime,nullable=False,default=datetime.now)

    author=relationship("User",back_populates="blog")

