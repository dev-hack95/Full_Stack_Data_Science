# Update a post
from fastapi import FastAPI, Response, status, HTTPException
import random
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[float]



my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "title of post 2", "content": "content of post 2", "id": 2},
            {"title": "title of post 3", "content": "content of post 3", "id": 3},
            {"title": "title of post 4", "content": "content of post 4", "id": 4},
            {"title": "title of post 5", "content": "content of post 5", "id": 5}]

def find_index_post(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {'message': 'Home'}

@app.get("/posts")
def get_posts():
    return {'data': my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post):
    post_dict = post.dict()
    post_dict['id'] = random.randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

# While updating post along with updateing part you have to input the non-updating part in put method 
@app.put("/posts/{id}")
def update_post(id: int, post: post):
    print(post)
    index = find_index_post(id)
    # if index not found then return error
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} doesn't exsist")
    print(post)
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {'data': post_dict}
