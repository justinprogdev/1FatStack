from fastapi import FastAPI
from services.embedding import EmbeddingService
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)
es = EmbeddingService()

@app.post("/index")
def index(text: str):
    return {"id": es.index(text)}

@app.get("/search")
def search(q: str):
    results = es.search(q)
    return [{"id": r.id, "score": r.score, "text": r.payload["text"]} for r in results]
