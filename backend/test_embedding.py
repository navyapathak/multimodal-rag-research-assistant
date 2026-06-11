from embeddings import create_embedding

vector = create_embedding("What is Artificial Intelligence?")

print("Vector length:", len(vector))
print(vector[:10])