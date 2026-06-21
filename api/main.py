from fastapi import FastAPI
from pydantic import BaseModel

from app.linker import process_text


app = FastAPI(
    title="Entity Linker API",
    version="1.0.0"
)


class TextRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "message": "Entity Linker API Running"
    }


@app.post("/link")
def link_text(request: TextRequest):
    results = process_text(request.text)

    return {
        "entities": results
    }