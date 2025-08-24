from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from Models import database
from Models.User import User as user_model
from Models.Blog import Blog
from Schema.User import UserResponse as User_schema,UserRequest

router=APIRouter(prefix="/users")

## Rest APIs
@router.get("/get_all",response_model=list[User_schema])
def get_users(db:Session=Depends(database.get_db)):
    users=db.query(user_model).all()
    if len(users)==0:
        raise HTTPException(status_code=404, detail="no users")
    return users    

@router.post("/add_user",response_model=User_schema)
def add_user(user_payload:UserRequest,db: Session=Depends(database.get_db)):
    user_dict=user_payload.model_dump(exclude={"confirm_password"})
    print(user_dict)
    user_db=user_model(**user_dict)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@router.put("/update_user/{user_id}",response_model=User_schema)
def update_user(user_payload:UserRequest, user_id:int, db:Session=Depends(database.get_db)):
    user_dict=user_payload.model_dump(exclude_unset=True) # ignore None fields and 
    print(user_dict)
    user=db.query(user_model).filter(user_model.user_id==user_id).first()
    # print(dict(user))
    if not user:
        raise HTTPException(status_code=404,detail="no user with provided id")
    for key,value in user_dict.items():
        setattr(user,key,value)
    db.commit()
    return user

@router.delete("/delete/{user_id}",response_model=User_schema)
def del_user(user_id:int,db:Session=Depends(database.get_db)):
    user=db.query(user_model).filter(user_model.user_id==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="No user with provided user")
    db.delete(user)
    db.commit()
    return user
## API with jwt and login