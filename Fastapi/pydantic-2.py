from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import random

app = FastAPI()

# We are creating a varible to hold a specific datatype 
class post(BaseModel):
    title: str
    context: str
    published: bool = True
    rating: Optional[int] = None

# Api also supports the concepts of array 
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "title of post 2", "content": "content of post 2", "id": 2}]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.post("/posts")
def fetch_post(post: post):
    # print(new_post.published)
    # print(new_post.title)
    # print(new_post.context)
    # print(new_post.rating)
    post_dict = post.dict()
    post_dict['id'] = random.randrange(0, 1000000000)
    my_posts.append(post_dict)
    return {"data": post_dict}