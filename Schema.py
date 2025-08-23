## Pydantic models
from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime

class UserRegister(BaseModel):
    user_id: str = str(uuid.uuid4())
    username:str
    password:str | None=None
    confirm_password:str | None=None
    email:EmailStr

    class Config:
        fields={
            "password":{"exclude":True},
            "confirm_password":{"exclude":True}
            }
        from_attribute=True

    @field_validator("confirm_password")
    def confirm_pass(cls,confirm_pass,values):
        password=values.get("password")
        if password and password != confirm_pass:
            raise ValueError("confirm password does not match password")
        return confirm_pass

class UserLogin(BaseModel):
    email:EmailStr,
    password:str

    class Config:
        fields:{
            "password":{"exclude":True}
            }
        from_attribute=True
    
class BlogBase(BaseModel):
    blog_id: int=str(uuid.uuid4()),
    title:str,
    content:str

    class Config:
        from_attribute=True

