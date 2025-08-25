from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from Models.database import get_db
from Models.User import User
from Schema.User import loginSchema
from datetime import datetime,timedelta
from jose import jwt, JWTError
from utils.auth import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
from passlib.context import CryptContext

auth_router=APIRouter(prefix="/auth")

# for verifying hashed password in user model with plain password
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_token(data:dict,expire_time:timedelta):
    try:
        to_encode=data.copy()
        new_expire=datetime.utcnow() + expire_time
        to_encode.update({"exp":new_expire})
        token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
        return {"access_token":token, "token_type":"bearer"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="Failed to create JWT token")

def get_user_from_header_token(token:str=Depends(oauth2_scheme), db:Session=Depends(get_db)):
    try:
        token_decode=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        search_user=token_decode.get("userid",None)
        if search_user is None:
            raise HTTPException(status_code=401, detail="No user id found")
        user=db.query(User).filter(User.user_id==search_user).first()
        if not user:
            raise HTTPException(status_code=401,detail="Failed to validate credentails")
        return user      
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=401, detail="Could not validate credentials")




@auth_router.post("/login")
def login(user_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    login_pass=user_data.password
    login_username=user_data.username

    ## check if username exists in db
    user=db.query(User).filter(User.username==login_username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exists")
    ## check if correct password is entered
    check_pass=pwd_context.verify(login_pass,user.password)
    if not check_pass:
        raise HTTPException(status_code=401, detail="invalid credentials")
    
    expiry_time=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    jwttoken=create_token({"userid":user.user_id},expiry_time)

    return jwttoken

    