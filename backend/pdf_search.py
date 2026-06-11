import fitz
from chunker import split_text
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

pdf_path = "uploads/Final PRJ 3 Report.pdf"

print("Opening PDF...")
doc = fitz.open(pdf_path)

text = ""

print("Extracting text...")
for page in doc:
    text += page.get_text()

print("Creating chunks...")
chunks = split_text(text)

print("Total chunks:", len(chunks))

print("Generating embeddings...")
chunk_embeddings = model.encode(chunks)

print("Embeddings generated!")

def search_pdf(query):

    print("Encoding query...")
    query_embedding = model.encode([query])

    print("Calculating similarity...")
    scores = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    best_index = np.argmax(scores)

    return chunks[best_index]