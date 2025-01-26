from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AkwaConnect!"}

@app.get("/about")
def about_page():
    return {"info": "Akwa Connect connects AkwaIbomites"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {'Message': f"hello {name}"}

@app.get("/search/{query}")
def search(query: str):
   
    return {"query": query, "results": "" }