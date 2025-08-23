from pydantic import BaseModel
import uuid

class Blog(BaseModel):
    blog_id:str=str(uuid.uuid4())
    title:str
    content:str
    created_by:str | None=None
    created_at:str | None=None
    
    class Config:
        from_attribute=True
    