# Create post --> 201 Created
from fastapi import FastAPI, Response, status, HTTPException
from typing import Optional
from pydantic import BaseModel
import random

app = FastAPI()

class post(BaseModel):
    title: str
    context: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "title of post 2", "content": "content of post 2", "id": 2},
            {"title": "title of post 3", "content": "content of post 3", "id": 3},
            {"title": "title of post 4", "content": "content of post 4", "id": 4},
            {"title": "title of post 5", "content": "content of post 5", "id": 5}]


def find_post(id: int) -> "post":
    for p in my_posts:
        if p['id'] == id:
            return p


@app.get("/")
def root():
    return {"message": "Home"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post):
    post_dict = post.dict()
    post_dict['id'] = random.randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}