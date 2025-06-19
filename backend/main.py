from fastapi import FastAPI
from services.embedding import EmbeddingService

app = FastAPI()
es = EmbeddingService()

@app.post("/index")
def index(text: str):
    return {"id": es.index(text)}

@app.get("/search")
def search(q: str):
    results = es.search(q)
    return [{"id": r.id, "score": r.score, "text": r.payload["text"]} for r in results]
