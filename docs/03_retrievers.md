# 03 — Retrievers

## 📌 What is a Retriever?
A **retriever** is the part of a RAG system that **finds the most relevant chunks** of text (or images, tables, etc.) from your knowledge base.  

Think of it as the **librarian**:  
- You ask a question → retriever looks up the best passages → passes them to the LLM.  

---

## 🔄 Retriever Workflow
1. Query embedding → vector representation of the user’s question.  
2. Vector search → compare query embedding with stored document embeddings.  
3. Top-k results → return the most semantically similar chunks.  
4. LLM → uses those chunks to generate an answer.  

---

## 🧩 Types of Retrievers

### 1. Vector Retriever (semantic search)
- Uses embeddings + vector database (FAISS, Pinecone, Qdrant).
- Finds chunks with similar meaning, not just matching keywords.
- ✅ Best for natural language queries.

---

### 2. Keyword Retriever (lexical search)
- Simple keyword match (like BM25, ElasticSearch).
- ✅ Good for exact matching of terms, e.g., “Clause 12.3”
- ❌ Misses paraphrases (e.g., “terminate contract” vs “end agreement”).

---

### 3. Hybrid Retriever
- Combines vector + keyword search.
- ✅ More robust: semantic + exact match.
- Common in enterprise systems (Azure Cognitive Search, Weaviate).

---

## ⚖️ Comparison

| Retriever Type | Pros | Cons | Example Use |
|----------------|------|------|-------------|
| Vector         | Captures meaning, flexible | Needs embeddings, compute cost | “What’s the KYC rule for high-value?” |
| Keyword        | Fast, precise for exact terms | Fails on paraphrasing | “Find Clause 12.3” |
| Hybrid         | Best of both worlds | More infra complexity | Compliance + legal search |

---

## 💻 Code Example (FAISS Retriever)
```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
documents = ["Clause 1: The tenant shall pay rent monthly.",
             "Clause 2: Termination requires 30-day notice."]
embeddings = model.encode(documents)

# Normalize for cosine similarity
embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

# Build FAISS index
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings.astype("float32"))

# Query
query = "How to end the contract?"
q_emb = model.encode([query])
q_emb = q_emb / np.linalg.norm(q_emb, axis=1, keepdims=True)

D, I = index.search(q_emb.astype("float32"), k=1)
print("Best match:", documents[I[0][0]])
```



🧠 FAQ

“Is the retriever part of the LLM?”
No. It’s separate. The retriever searches your external knowledge base, then passes context to the LLM.

“What if the retriever brings wrong info?”
Then the LLM generates poor answers. Garbage in → garbage out.

“How many chunks should I retrieve?”
Typical: 3–5 chunks. Too few → miss info, too many → exceed context window.

🎯 Key Takeaway

The retriever is the backbone of RAG.
A great LLM with poor retrieval = useless.
A solid retriever with a decent LLM = reliable system.

Next → Vector Databases


