from .database import Base
from sqlalchemy import Column, String,DateTime,Text,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

class Blog(Base):
    __tablename__="blog"
     
    blog_id=Column(String(255),primary_key=True,nullable=False,index=True,default=lambda: str(uuid.uuid4()))
    title=Column(String(50),nullable=False,index=True)
    content=Column(Text,nullable=False,index=True)
    created_by=Column(String,ForeignKey("user.user_id"))
    created_at=Column(DateTime,nullable=False,default=datetime.now)

    author=relationship("User",back_populates="blog")

