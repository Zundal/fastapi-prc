from fastapi import FastAPI
from .api.api_v1.endpoints import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}