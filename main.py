from fastapi import FastAPI
from Models.User import User
from Models.Blog import Blog

app=FastAPI()

@app.get("/")
def index():
    return {"application":"started"}