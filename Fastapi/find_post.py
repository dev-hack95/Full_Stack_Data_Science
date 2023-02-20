from fastapi import FastAPI, Response, status, HTTPException
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
            {"title": "title of post 2", "content": "content of post 2", "id": 2},
            {"title": "title of post 3", "content": "content of post 3", "id": 3},
            {"title": "title of post 4", "content": "content of post 4", "id": 4},
            {"title": "title of post 5", "content": "content of post 5", "id": 5}]

def find_post(id: int) -> "post":
    """Function to find the post by using id of that post"""
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    # Get all posts
    return {"data": my_posts}  
    # Return as dict(list(dict)) in postman

@app.post("/posts")
def fetch_post(post: post): # Pydantic Base Model
    post_dict = post.dict() 
    post_dict['id'] = random.randrange(0, 1000000000) # Give Random id to the blog
    my_posts.append(post_dict)
    return {"data": post_dict}

# See the latest post
@app.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}

# Find the post by id
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
        # OR
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id {id} not found"}
    return {"post_details": post}