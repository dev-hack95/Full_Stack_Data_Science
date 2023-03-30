import random
import uvicorn
import time
import psycopg2
from fastapi import FastAPI, Request, Response, status, HTTPException, APIRouter, Depends
from fastapi.params import Body
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
router = APIRouter()

class Post(BaseModel):
    title = str
    content = str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host = '192.168.29.244',
                                port=5432,
                                database = 'api_learn_db',
                                user = 'postgres',
                                password = 'postgres',
                                cursor_factory=RealDictCursor)
        # RealDictCursor help to map column name with values like python dict
        cursor = conn.cursor()
        print('DataBase Connected Successfully')
        break
    except Exception as error:
        print("Error: ", error)

 

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.get('/posts')
def get_posts(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts""")
    #posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {'data': posts}

@app.post('/create_post', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    #print(post.title)
    #print(post.content)
    # cursor.execute(f"INSERT INTO posts (title, content) VALUES ({post.title}, {post.content})")
    # This is vulnerable to sql-injection
    #query = """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)"""
    #cursor.execute(query, (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    new_post = models.Post(title = post.title, content = post.content, published = post.published)
    return {'data': new_post}
    
@app.get('/posts/{id}')
def get_post(id: str):
    cursor.execute("""SELECT * FROM posts WHERE id = %s RETURNING *""", (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id-{id} not found")
    return {'postdetails': post}

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str):
    cursor.execute("""DELECT FROM posts WHERE id = %s RETURNING *""", (str(id)))
    delete_post = cursor.fetchone()
    conn.commit()
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id-{id} doest not exsist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

    
@app.put('/posts/{id}')
def update_post(id: str, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s""", (post.title, post.content, post.published))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exsist")
    return {'data': updated_post}
