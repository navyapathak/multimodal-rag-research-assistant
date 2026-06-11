from fastapi import FastAPI, UploadFile, File
import fitz
import os

from chunker import split_text
from rag_search import search_rag
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Store PDF data in memory
stored_chunks = []
stored_embeddings = []

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Multimodal RAG Backend Running"
    }


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from PDF
    doc = fitz.open(filepath)

    text = ""

    for page in doc:
        text += page.get_text()

    # Split into chunks
    chunks = split_text(text)

    # Save chunks and embeddings globally
    global stored_chunks
    global stored_embeddings

    stored_chunks = chunks
    stored_embeddings = model.encode(chunks)

    return {
        "filename": file.filename,
        "characters_extracted": len(text),
        "total_chunks": len(chunks),
        "first_chunk": chunks[0]
    }


@app.get("/ask")
def ask_question(query: str):

    if not stored_chunks:
        return {
            "error": "Upload PDF first"
        }

    answer = search_rag(
        query,
        stored_chunks,
        stored_embeddings
    )

    return {
        "question": query,
        "answer": answer
    }