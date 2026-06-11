from sentence_transformers import SentenceTransformer
from faiss_store import create_faiss_index, search_faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Artificial Intelligence is a field of computer science.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks."
]

embeddings = model.encode(chunks)

index = create_faiss_index(embeddings)

query = "What is machine learning?"

query_embedding = model.encode([query])

indices = search_faiss(query_embedding, index)

print(indices)

for i in indices:
    print(chunks[i])