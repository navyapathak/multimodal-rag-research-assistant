from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Artificial Intelligence is a branch of computer science.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks.",
    "Python is widely used in AI development."
]

chunk_embeddings = model.encode(chunks)

def search(query):

    query_embedding = model.encode([query])

    scores = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    best_index = np.argmax(scores)

    return chunks[best_index]