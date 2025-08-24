from pydantic import BaseModel,Field
from datetime import datetime
import uuid

class Blog(BaseModel):
    blog_id:str = Field(default_factory=lambda: str(uuid.uuid4()))
    title:str
    content:str
    created_by:str | None=None
    created_at:datetime | None=None
    
    class Config:
        from_attribute=True
    