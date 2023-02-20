from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# We are creating a varible to hold a specific datatype 
class post(BaseModel):
    title: str
    context: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/posts")
def fetch_post(post: post):
    # print(new_post.published)
    # print(new_post.title)
    # print(new_post.context)
    # print(new_post.rating)
    return {"data": post}