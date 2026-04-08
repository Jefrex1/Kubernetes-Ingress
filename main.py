from fastapi import FastAPI

app = FastAPI(title="My API", version="1.0.0")

@app.get("/api/hello")
def hello():
    return {"message": "Привіт!"}

@app.get("/api/items/{item_id}")
def get_item(item_id: int):
    return {"id": item_id, "name": f"Item {item_id}"}