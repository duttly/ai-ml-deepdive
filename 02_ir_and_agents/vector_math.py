from sentence_transformers import SentenceTransformer
import numpy as np

# Load a highly-optimized, small local embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "The cat sits outside.",
    "A dog is playing in the yard.",
    "I love programming in Python."
]

# Generate dense embeddings (this model outputs 384 dimensions)
embeddings = model.encode(sentences)
print(len(embeddings[0]))
print(embeddings)

def cosine_similarity(v1, v2):
    # The math: Dot product divided by the product of their magnitudes (L2 norms)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print(f"Similarity (Cat vs Dog): {cosine_similarity(embeddings[0], embeddings[1]):.4f}")
print(f"Similarity (Cat vs Python): {cosine_similarity(embeddings[0], embeddings[2]):.4f}")
