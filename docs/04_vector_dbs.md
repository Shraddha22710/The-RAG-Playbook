# 04 — Vector Databases

## 📌 What is a Vector Database?
A **vector database** is a storage and search system designed for **high-dimensional embeddings**.  
Unlike traditional databases (which store rows and columns), vector DBs specialize in **similarity search** — finding the closest vectors to a query embedding.

These are essential for RAG because they let us perform **semantic search** across large document collections.

---

## 🛠️ Why Vector DBs Matter for RAG
- **Performance** → optimized for vector math (dot products, cosine similarity).
- **Scalability** → handle millions or billions of embeddings efficiently.
- **Filtering** → combine semantic search with metadata filters (e.g., doc type = invoice, date > 2021).
- **Flexibility** → support hybrid search (keyword + vector).

---

## ⚖️ Popular Vector DB Options

| Option      | Type        | Pros | Cons | Best For |
|-------------|------------|------|------|----------|
| **FAISS**   | Self-hosted lib | Fast, free, good for prototyping | Not distributed | Local PoC, research |
| **Chroma**  | Open-source DB | Easy API, Python-first | Early-stage | Learning, small projects |
| **Qdrant**  | Open-source/cloud | Metadata filters, hybrid search | Needs infra setup | Mid-scale apps |
| **Weaviate**| Cloud/open-source | GraphQL API, hybrid, multi-modal | Complex setup | Rich semantic apps |
| **Pinecone**| Managed SaaS | Scalable, no ops | Paid, vendor lock-in | Enterprise SaaS |
| **Azure Cognitive Search** | Managed | Hybrid (BM25 + vectors), enterprise ready | Azure-only | Enterprise deployments |

---

## 💻 Example: FAISS (local prototyping)
```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Example docs
docs = ["RBI requires KYC for transactions above ₹10 lakh.",
        "GDPR mandates explicit consent for personal data."]

# Create embeddings
model = SentenceTransformer("all-mpnet-base-v2")
vecs = model.encode(docs)
vecs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)

# Build index
index = faiss.IndexFlatIP(vecs.shape[1])
index.add(vecs.astype("float32"))

# Search
query = "What is the KYC limit for high-value transactions?"
qv = model.encode([query])
qv = qv / np.linalg.norm(qv, axis=1, keepdims=True)
D, I = index.search(qv.astype("float32"), k=1)

print("Best match:", docs[I[0][0]])


🧠 FAQ

“Why not use a normal SQL database?”
SQL handles structured queries, but isn’t optimized for vector similarity search.

“Which vector DB should I choose?”

PoC → FAISS/Chroma

Scale-up → Qdrant/Weaviate

Enterprise → Pinecone / Azure Cognitive Search

“Can I combine keyword and vector search?”
Yes → that’s called hybrid retrieval (supported in Weaviate, Qdrant, Azure).

🎯 Key Takeaway

The vector database is the memory of a RAG system.
Pick the right one based on scale:

Small project → FAISS

Mid-scale → Qdrant/Weaviate

Enterprise → Pinecone/Azure
