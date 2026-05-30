from langchain_experimental.text_splitter import SemanticChunker
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# 1. We load the exact same local embedding model you used on Day 11!
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. We initialize the Semantic Chunker. 
# "percentile" means it will split when the distance between two sentences 
# is mathematically massive compared to the rest of the document.
text_splitter = SemanticChunker(embedder, breakpoint_threshold_type="percentile", buffer_size=1)

# A tricky document: It starts about AI, then abruptly switches to baking bread.
document = """
Artificial intelligence has revolutionized modern software engineering. 
Large language models can now write code, debug errors, and orchestrate complex systems.
This paradigm shift requires engineers to understand probabilistic workflows.
In completely unrelated news, baking sourdough bread requires high-hydration starter.
You must knead the dough carefully and let it ferment overnight in the fridge.
A hot Dutch oven is essential for a crispy crust.
"""

# 3. Perform the semantic split
chunks = text_splitter.split_text(document)

print(f"Total Chunks Created: {len(chunks)}\n")
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk.strip())
    print()
