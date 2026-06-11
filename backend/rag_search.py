from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_rag(query, chunks, chunk_embeddings):

    query_embedding = model.encode([query])

    scores = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    best_index = np.argmax(scores)

    return chunks[best_index]