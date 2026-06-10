from fastapi import FastAPI, UploadFile, File
import fitz
import os
from chunker import split_text

app = FastAPI()

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

    doc = fitz.open(filepath)

    text = ""

    for page in doc:
        text += page.get_text()

    chunks = split_text(text)

    return {
        "filename": file.filename,
        "characters_extracted": len(text),
        "total_chunks": len(chunks),
        "first_chunk": chunks[0]
    }