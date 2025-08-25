from pydantic import BaseModel,Field
from datetime import datetime
import uuid

class BlogRequest(BaseModel):
    title:str | None=None
    content:str | None=None
    created_by:str | None=None
    
    class Config:
        from_attribute=True

class BlogResponse(BaseModel):
    blog_id:str
    title:str
    content:str
    created_by:str | None=None
    created_at:datetime | None=None
    
    class Config:
        from_attribute=True