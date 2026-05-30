import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Make sure your API key is set in your environment variables
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"

print("--- PHASE A: INGESTION ---")

# 1. The Private Data (Usually loaded from PDFs, Notion, or SQL)
private_text = """
Welcome to the company! Here are some key details for 2026:
- The Q4 refund policy requires manager approval for amounts over $500.
- The secret passcode for Project Nebula is ORION-77.
- The office WiFi password is 'keepitsecret123'.
"""
# We wrap it in a LangChain Document object
documents = [Document(page_content=private_text)]

# 2. Chunking
# We split the text into 50-character chunks with a 10-character overlap
# Overlap ensures we don't accidentally chop a sentence in half and lose context.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
chunks = text_splitter.split_documents(documents)
print(f"Split document into {len(chunks)} chunks.")

# 3. Embedding & Storage (The Vector DB)
# This converts our text chunks into vectors and saves them in ChromaDB in memory.
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=OpenAIEmbeddings() # The model that turns text into numbers
)
print("Chunks embedded and stored in Vector DB.\n")


print("--- PHASE B: RETRIEVAL & GENERATION ---")

# 4. The Retriever
# We configure the database to act as a search engine, returning the top 2 closest chunks.
retriever = vector_db.as_retriever(search_kwargs={"k": 2})

# 5. The Augmented Prompt Template
# This is where we force the LLM to take an "Open-Book Test"
prompt_template = PromptTemplate.from_template("""
You are a helpful company assistant. Answer the question based ONLY on the following context. 
If the answer is not in the context, say "I don't know."

Context: 
{context}

Question: 
{question}
""")

# 6. The LLM (The Brain)
llm = ChatOpenAI(model="gpt-4o", temperature=0) # Temperature 0 = strict, factual

# 7. Building the Chain (LCEL - LangChain Expression Language)
# This defines the exact flow of data from the user to the LLM.
rag_chain = (
    # Step 1: Take the user's question, run it through the retriever, and assign it to "context"
    {"context": retriever, "question": RunnablePassthrough()}
    # Step 2: Pass the context and question into our prompt template
    | prompt_template
    # Step 3: Pass the formatted prompt to the LLM
    | llm
    # Step 4: Extract just the string output from the LLM's response object
    | StrOutputParser()
)

# --- EXECUTION ---
user_question = "What is the passcode for Project Nebula?"
print(f"User Asked: {user_question}\n")

# Run the chain!
answer = rag_chain.invoke(user_question)
print(f"AI Answer: {answer}")
