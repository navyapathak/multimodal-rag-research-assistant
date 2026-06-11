from sentence_transformers import SentenceTransformer
from rag_search import search_rag

chunks = [
    "Artificial Intelligence is a field of computer science.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks."
]

model = SentenceTransformer("all-MiniLM-L6-v2")

chunk_embeddings = model.encode(chunks)

result = search_rag(
    "What is machine learning?",
    chunks,
    chunk_embeddings
)

print(result)