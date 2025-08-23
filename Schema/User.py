from pydantic import BaseModel,EmailStr

class UserRequest(BaseModel):
    username:str | None=None
    email:EmailStr
    password:str
    confirm_password:str | None=None

    class Config:
        from_attribute=True

    @model_validator(mode="after")
    def confirmcheck(self):
        if self.confirm_password is None or self.confirm_password != self.password:
            raise ValueError("Confirm password and password mismatch")
        return self


class UserResponse(BaseModel):
    email:str
    username:str

    class Config:
        from_attribute=True
