from fastapi import *

app = FastAPI()

@app.get("/")
async def root():
    # async keyword is used to wait to perform some tasks
    return {"message": "Hello World"}

@app.get("/test_1")
def test_1():
    return {"message": "test_1"}

@app.get("/test_2")
def test_2():
    return {"message": "test_2"}

@app.get("/test_2/score")
def test_2_score():
    return {"message": "test_2 scores"}

@app.post("/createposts")
def create_post(payLoad: dict = Body(...)): # For post your personal title and content about it you need to pass it from body 
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}