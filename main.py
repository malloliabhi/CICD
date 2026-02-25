from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search/")
def search_item(q: str):
    return {"query": q}
