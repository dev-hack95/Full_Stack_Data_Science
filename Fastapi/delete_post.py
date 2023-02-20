# Delete a POST

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

def find_index_post(id: int):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
def root():
    return {"message": "Home"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post):
    post_dict = post.dict()
    post_dict['id'] = random.randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} doesn't exsist")

    my_posts.pop(index)
    return {'message': f"Post {id} is succesfully deleted"}