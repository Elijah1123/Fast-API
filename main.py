from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome my FastAPI application!"}


@app.get("/posts") 
def get_posts():
    return {"data": "Here are your posts"}


@app.post("/createposts")
def create_posts():
    return {"message": "Post created successfully!"}

