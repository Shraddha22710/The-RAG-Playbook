# 02 — Chunking Strategies

## 📌 Why Chunking Matters
Large documents (contracts, invoices, KYC forms, research papers) are too big to embed at once.  
So we split them into **chunks** → smaller, meaningful pieces for embeddings and retrieval.

Good chunking = better retrieval = more accurate RAG answers.  
Bad chunking = broken context or missed info.

---

## 🔎 Common Strategies

### 1. Fixed-Size Chunking
- Split by a fixed number of tokens/words.
- Example: 500-token chunks with 50-token overlap.
- ✅ Simple & fast
- ❌ May break sentences/clauses in the middle.

[Words 0–500] → Chunk 1
[Words 450–950] → Chunk 2 (overlap)
[Words 900–1400] → Chunk 3 …

---

### 2. Semantic Chunking
- Split on **natural boundaries**: sentences, paragraphs, or contract clauses.
- ✅ Preserves meaning
- ❌ Variable length, may create imbalanced chunks

Example:

Clause 1: Definitions → Chunk 1
Clause 2: Responsibilities → Chunk 2
Clause 3: Termination → Chunk 3

---

### 3. Overlapping Chunks
- Add overlap between chunks so edge context is preserved.
- ✅ Better recall during retrieval
- ❌ Increases storage & compute slightly

Chunk 1: Sentences 1–5
Chunk 2: Sentences 5–10 (overlap on sentence 5)
Chunk 3: Sentences 10–15 …


---

### 4. Table-Aware Chunking
- For invoices/contracts, each **row in a table** can be treated as a chunk.
- Add **header context** for better search.
- Example:  
Row 1 | Headers: Item | Qty | Amount | Values: Pen | 10 | 500
Row 2 | Headers: Item | Qty | Amount | Values: Paper | 20 | 1000


---

## ⚖️ Choosing a Strategy
| Strategy       | Best For                 | Trade-offs |
|----------------|--------------------------|------------|
| Fixed Size     | Short texts, quick demos | May split semantic units |
| Semantic       | Legal docs, research     | Uneven size, complex |
| Overlapping    | Most RAG systems         | Extra storage |
| Table-Aware    | Invoices, KYC, contracts | Needs table parsing |

---

## 🧪 Practical Defaults
- Chunk size: **200–400 tokens**  
- Overlap: **30–50 tokens**  
- Semantic for clauses/paragraphs, fixed+overlap for long plain text.  
- Table rows as separate chunks with headers.  

---

## 🧠 FAQ
- *“Why not just embed the whole doc?”*  
  Embedding models + vector DBs have input limits. Large docs → poor retrieval quality.

- *“What happens if chunks are too small?”*  
  You lose context → retrieval may miss meaning.

- *“Why overlap?”*  
  To avoid cutting off important info at boundaries (e.g., “₹10 lakh” might be split).

---

## 💻 Code Example
```python
from chunking import fixed_chunking, semantic_chunking

text = "This is a demo document. It has several sentences. Each may form part of a chunk."
fixed_chunks = fixed_chunking(text, max_tokens=20, overlap=5)
semantic_chunks = semantic_chunking(text, max_tokens=30, overlap_tokens=5)

print("Fixed chunks:", fixed_chunks)
print("Semantic chunks:", semantic_chunks)


🎯 Key Takeaway

Chunking is not just splitting text — it’s about preserving meaning while fitting into the model’s context window.

Next → Retrievers
