# Evaluation Report — RAG Playbook 

## Purpose
This document captures evaluation plans and initial results for different RAG configurations used in the repo.

## Evaluation Goals
- Measure retrieval effectiveness (Recall@k, Precision@k, MRR)
- Compare embedding models (MiniLM vs MPNet vs OpenAI embeddings)
- Compare chunking strategies (fixed vs semantic vs overlapping)
- Evaluate downstream answer correctness (LLM + RAG) on compliance queries (binary / multi-class)

## Dataset
- Synthetic dataset: 50–200 documents combining sample contracts, invoices, and regulation snippets.
- Ground-truth mapping: small test set of queries with expected document/chunk ids and expected answer labels.

## Experiments (suggested)
1. **Embedding model comparison**
   - Build three indexes using `all-MiniLM-L6-v2`, `all-mpnet-base-v2`, and OpenAI embeddings.
   - Metric: Recall@5, Precision@5, build time, query latency.

2. **Chunking strategy comparison**
   - For a fixed embedding model, compare recall using fixed-chunk, semantic-chunk, and overlap-chunk strategies.

3. **Reranking vs no-reranking**
   - Apply cross-encoder reranker on top-10 candidates from FAISS; measure precision improvement.

4. **Downstream correctness**
   - Feed top-k retrieved passages to LLM (RAG prompt) and evaluate final answer correctness against labeled answers.

## Metrics
- Recall@k, Precision@k, MRR for retrieval.
- Accuracy / F1 for final answer classification.
- Latency (ms) per query.
- Cost estimates (if using managed embeddings / LLM APIs).
