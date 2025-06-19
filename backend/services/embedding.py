from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer
from uuid import uuid4

class EmbeddingService:
    def __init__(self, collection_name: str = "notes"):
        self.client = QdrantClient(host="vector-db", port=6333)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.collection_name = collection_name

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    def embed(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()

    def index(self, text: str, note_id: str = None):
        vector = self.embed(text)
        point_id = note_id or str(uuid4())
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload={"text": text}
                )
            ]
        )
        return point_id

    def search(self, query: str, limit: int = 5):
        vector = self.embed(query)
        return self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=limit
        )
