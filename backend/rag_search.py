from sentence_transformers import SentenceTransformer
from faiss_store import search_faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_rag(query, chunks, index):

    query_embedding = model.encode([query])

    indices = search_faiss(
        query_embedding,
        index
    )

    context = ""

    for i in indices:
        context += chunks[i] + "\n\n"

    return context