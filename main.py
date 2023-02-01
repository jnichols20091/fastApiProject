from fastapi import FastAPI, Path
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory="templates")
app = FastAPI( )

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
async def get_item(item_id: int = Path(None, description="The ID of the item you want to view", gt=0, lt=1000)):
    return inventory[item_id]

if __name__ == "__main__":
    uvicorn.run(app, port=8000)