from fastapi import FastAPI
from Routers import users
from Models.database import Base,db_engine 

app=FastAPI()
Base.metadata.create_all(bind=db_engine)

app.include_router(users.router)