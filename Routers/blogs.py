from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from Schema.Blog import BlogResponse as blog_response,BlogRequest
from Models.database import get_db
from Models.Blog import Blog as blog_db

blog_router=APIRouter(prefix="/blog")

@blog_router.get("/getall",response_model=list[blog_response])
def getall(db:Session=Depends(get_db)):
    blogs=db.query(blog_db).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="blog table is empty")
    return blogs

@blog_router.post("/add_blog",response_model=blog_response)
def add_blog(blog:BlogRequest, db:Session=Depends(get_db)):
    # convert pydantic model to dictionary removing parameters that are None or not passed
    blog_dict=blog.model_dump()
    # add it to table Blog
    blog_model=blog_db(**blog_dict)
    db.add(blog_model)
    db.commit()
    db.refresh(blog_model)
    return blog_model

@blog_router.put("/update_blog/{blog_id}",response_model=blog_response)
def update_blog(id:str,blog:BlogRequest,db:Session=Depends(get_db)):
    blog_dict=blog.model_dump(exclude_unset=True)
    blogdb=db.query(blog_db).filter(blog_db.blog_id==id).first()

    for key,value in blog_dict.items():
        setattr(blogdb,key,value)
    db.commit()
    db.refresh(blogdb)

    return blogdb

@blog_router.delete("/delete_blog/{blog_id}",response_model=blog_response)
def delete_blog(blog_id:str, db:Session=Depends(get_db)):
    blogdb=db.query(blog_db).filter(blog_db.blog_id==blog_id).first()
    if not blogdb:
        raise HTTPException(status_code=404, detail="No blog with provided ID")
    db.delete(blogdb)
    db.commit()
    
    return blogdb
