import chromadb
import json

# 1. Initialize an in-memory local Vector Database
chroma_client = chromadb.Client()

# 2. Create a "Collection" (Think of this like an SQL Table)
collection = chroma_client.create_collection(name="my_first_vector_db")

# 3. Insert our documents
# ChromaDB is smart enough to automatically download an embedding model
# (all-MiniLM-L6-v2) and convert these strings into vectors under the hood!
collection.add(
    documents=[
        "The cat sits outside.",
        "A dog is playing in the yard.",
        "I love playing fetch with Fido",
        "I love programming in Python.",
        "The sun is our nearest star",
        "I have 3 parrots and 2 parakeets in my backyard"
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"]
)

print("Documents successfully embedded and indexed into the DB!\n")

# 4. Perform a Semantic Search
query_text = "Tell me about pets"
print(f"Query: '{query_text}'\n")

results = collection.query(
    query_texts=[query_text],
    n_results=10 # We want the Top 2 closest matches
)

print(json.dumps(results, indent=4))

# 5. Print the results
for i in range(len(results['documents'][0])):
    doc = results['documents'][0][i]
    distance = results['distances'][0][i]
    print(f"Match {i+1}: {doc} (Distance: {distance:.4f})")
