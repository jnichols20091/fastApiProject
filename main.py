from fastapi import FastAPI

app = FastAPI()

inventory = {
        1: {"name": "Foo",
            "price": 50,
            "brand": "Bar"
        }
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return inventory[item_id]

