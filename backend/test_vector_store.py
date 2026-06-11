from vector_store import create_vector_store

chunks = [
    "Artificial Intelligence is a field of computer science.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks."
]

index = create_vector_store(chunks)

print("Vectors stored:", index.ntotal)