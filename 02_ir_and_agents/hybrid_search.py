import chromadb
import json

chroma_client = chromadb.Client()
collection = chromadb.Client().create_collection(name="hybrid_search_db")

# 1. Insert documents WITH metadata
collection.add(
    documents=[
        "The new electric sedan has a 400-mile range.",
        "Our latest smartphone features a titanium body.",
        "This electric truck can tow 10,000 lbs.",
        "The upcoming smartwatch tracks blood oxygen."
    ],
    metadatas=[
        {"category": "automotive", "year": 2024},
        {"category": "electronics", "year": 2024},
        {"category": "automotive", "year": 2025},
        {"category": "electronics", "year": 2025}
    ],
    ids=["doc1", "doc2", "doc3", "doc4"]
)

# 2. Perform a Hybrid Query
# The user wants an electric vehicle, but STRICTLY from the year 2025.
results = collection.query(
    query_texts=["Tell me about electric vehicles"],
    n_results=2,
    where={"year": 2025} # This is the Metadata Pre-Filter!
)

print("Results for 'Tell me about electric vehicles' (Year 2025 ONLY):")
print(json.dumps(results, indent=2))
for i, doc in enumerate(results['documents'][0]):
    print(f"- {doc}")
