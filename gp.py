from fastapi import FastAPI

from post import Item

#from pydantic import BaseModel

app=FastAPI()
@app.get("/items/")
def read_items():
    return {"message": "Send POST request to create item"}

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
uvi