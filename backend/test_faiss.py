from sentence_transformers import SentenceTransformer
from faiss_store import create_faiss_index

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning"
]

embeddings = model.encode(chunks)

index = create_faiss_index(embeddings)

print("Vectors Stored:", index.ntotal)