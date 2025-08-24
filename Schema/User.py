from pydantic import BaseModel,EmailStr,model_validator

class UserRequest(BaseModel):
    username:str | None=None
    email:EmailStr | None=None
    password:str | None=None
    confirm_password:str | None=None

    class Config:
        from_attribute=True

    @model_validator(mode="after")
    def confirmcheck(self):
        if self.confirm_password is not None and self.confirm_password != self.password:
            raise ValueError("Confirm password and password mismatch")
        return self


class UserResponse(BaseModel):
    user_id:int
    email:str
    username:str

    class Config:
        from_attribute=True
