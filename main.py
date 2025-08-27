from fastapi import FastAPI
from Models.database import Base,db_engine 
from Routers import users
from Routers import blogs
from Routers import auth

app=FastAPI()
## create tables
Base.metadata.create_all(bind=db_engine)


app.include_router(auth.auth_router)
app.include_router(users.router)
app.include_router(blogs.blog_router)