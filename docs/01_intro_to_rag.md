
# 01 — Introduction to RAG

## 🤔 What is RAG?
**Retrieval-Augmented Generation (RAG)** is a technique that combines:
- **Retriever** → finds relevant information from an external knowledge base.
- **Generator (LLM)** → uses the retrieved context to generate an answer.

This makes LLMs *“grounded”* in facts instead of hallucinating.

---

## 🔄 RAG Workflow
1. **User Query** → "Does this contract meet GDPR rules?"
2. **Retriever** → searches regulations & contract text.
3. **Top-K Chunks** → most relevant passages are returned.
4. **LLM** → generates an answer *using those passages*.
5. **Output** → answer + citations for auditability.

---

## 🧩 Why not just fine-tune?
| Approach         | Pros | Cons | When to Use |
|------------------|------|------|-------------|
| **Fine-tuning**  | Learns domain style, specialized | Costly, needs lots of labeled data, retrain for updates | Stable, narrow tasks |
| **RAG**          | No retraining, easy to update, can cite sources | Dependent on retrieval quality | Dynamic domains, frequent updates (regulations) |

👉 For compliance & audit, **RAG is better** because laws/regulations change frequently.

---

## 🔑 Core Components
- **Embeddings** → convert text into vector representations.
- **Vector Database** → stores embeddings, enables semantic search.
- **Retriever** → finds top relevant chunks.
- **Generator (LLM)** → produces grounded output.

---

## 🧠 FAQ (Common Doubts)
- *“Is RAG post-training?”*  
  No — it’s a retrieval pipeline at inference time. The LLM weights stay frozen.

- *“Does RAG replace fine-tuning?”*  
  Not always. Fine-tuning = teach permanent skills. RAG = add external knowledge.

- *“Why does RAG reduce hallucinations?”*  
  Because the model is forced to use retrieved passages as context.

---

## 🎯 Example
**Without RAG:**  
Q: "What is the RBI KYC limit?"  
A: *“It is ₹20 lakh”* (hallucinated).  

**With RAG:**  
Retriever finds → "RBI circular: Transactions above ₹10 lakh require KYC."  
LLM Answer → *“RBI requires KYC for transactions above ₹10 lakh [RBI 2021 Circular].”*  

---

Next → [Chunking Strategies](02_chunking.md)
