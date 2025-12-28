# uvicorn fastApiAnnotated:app --reload

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def readCharlieBrownCharacters(
    name: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
    age: Annotated[int, Query(gt=0, le=100)] = 10,
):
    return {
        "name": name,
        "age": age,
    }
