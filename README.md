![banner](docs/1.svg)

---

## 🚀 Overview
The RAG Playbook is a practical guide and starter kit for **Retrieval-Augmented Generation (RAG)**.  
It combines **conceptual docs, hands-on code, case studies, and production best practices** to help you learn and build reliable RAG systems.

This repo is for:
- 🧑‍🎓 **Students & Newbies** → step-by-step explanations, FAQs, and demos.  
- 👩‍💻 **Engineers** → reusable Python modules (chunking, retrievers, FAISS).  
- 🏢 **Industry/Consultants** → business framing, compliance use-cases, enterprise readiness.

---

## 📂 Repo Map
```
The-RAG-Playbook/
├── README.md               <- You are here
├── requirements.txt        <- Python dependencies
│
├── data/                   <- Documents & built embeddings
│   ├── documents/          <- Sample contracts, regulations, invoices
│   └── embeddings/         <- FAISS index + metadata
│
├── docs/                   <- Learning modules
│   ├── 01_intro_to_rag.md
│   ├── 02_chunking.md
│   ├── 03_retrievers.md
│   ├── 04_vector_dbs.md
│   ├── 05_advanced_rag.md
│   ├── 06_production_rag.md
│   └── glossary.md
│
├── src/                    <- Core Python modules
│   ├── chunking.py
│   ├── simple_rag.py
│   ├── rag_pipeline.py
│   ├── agents.py
│   └── app.py
│
├── notebooks/              <- Interactive experiments
│   ├── 01_basic_rag.ipynb
│   ├── 02_chunking_demo.ipynb
│   ├── 03_faiss_demo.ipynb
│   ├── 04_multi_agent_rag.ipynb
│   └── 05_advanced_patterns.ipynb
│
└── evaluation/             <- Metrics & reports
    ├── metrics.py
    └── evaluation_report.md
```


---

## ⚡ Quickstart

> Requirements: Python 3.10+, git, internet for dependencies.

1. **Clone repository**
```yaml
git clone https://github.com/<yourname>/awesome-rag-playbook.git
cd awesome-rag-playbook
```

2. Create virtual environment & install
   ```python
   python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows
.venv\Scripts\activate

pip install -r requirements.txt

```
3. Add sample documents
Put .txt files into data/documents/ (regulation snippets, contracts, invoices).

4. Build index & test retrieval
```python
python src/simple_rag.py --build-index --data-dir data/documents
python src/simple_rag.py --query "Does this contract mention GDPR data transfers?"
```

5. Run demo app
   ```python
   streamlit run src/app.py
```

## 🎓 Learning Roadmap

- **Step 1** → Intro to RAG (GenAI vs RAG vs Agents).  
- **Step 2** → Chunking Strategies + try `src/chunking.py`.  
- **Step 3** → Build FAISS index with `src/simple_rag.py`.  
- **Step 4** → Study Retrievers & `rag_pipeline.py`.  
- **Step 5** → Explore Advanced RAG (multi-hop, multimodal).  
- **Step 6** → Production RAG: A/B testing, security, privacy.  
- **Step 7** → Run notebooks to compare LLM vs RAG and experiment with agent flows.  

---

## 🔑 Core Concepts Covered

- Chunking strategies: fixed, semantic, overlapping, table-aware.  
- Embeddings & models: MiniLM, MPNet, OpenAI ADA embeddings.  
- Vector DBs: FAISS, Pinecone, Qdrant, Azure Cognitive Search.  
- Retrieval pipeline & prompt patterns for RAG.  
- Advanced RAG: multi-hop, hierarchical, multimodal, graph-based.  
- Agentic RAG: orchestrating Document, Regulation, and Governance agents.  
- Production concerns: A/B testing, resilience, privacy (GDPR, HIPAA), scaling.  

---

## 🧪 Suggested Experiments

- 🔹 Compare plain LLM vs RAG answers on the same query.  
- 🔹 Test chunk sizes & overlap, measure Recall@5.  
- 🔹 Try different embedding models for retrieval quality.  
- 🔹 Build a 3-agent flow for compliance checks.  
- 🔹 Add OCR + images (logos/seals) for multimodal retrieval.

---





## Visualizations

### A. RAG Pipeline
```mermaid
flowchart TD
  U[User Query] --> R[Retriever]
  R -->|top-k passages| G[Generator (LLM)]
  G --> A[Answer + Citations]

subgraph KB [Knowledge Base]
    D1[Chunk 1]
    D2[Chunk 2]
    D3[Chunk n]
  end

R --- KB
```


