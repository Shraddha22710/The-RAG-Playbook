# Glossary — quick definitions

**Embeddings**  
Numeric vector representations of text (or images) that capture semantic meaning. Similar items have similar vectors.

**Retriever**  
Component that finds relevant chunks from a vector store or index given a query embedding.

**RAG (Retrieval-Augmented Generation)**  
A pipeline that combines retrieval of external documents with a generative model (LLM) to produce grounded answers.

**Chunk / Chunking**  
Splitting a document into smaller pieces (chunks) suitable for embedding and retrieval. Strategies: fixed, semantic, overlapping, table-aware.

**Vector Database / Vector Store**  
A system optimized to store high-dimensional vectors and perform nearest-neighbor search (FAISS, Pinecone, Qdrant, Weaviate).

**FAISS**  
Facebook AI Similarity Search — an efficient library for similarity search and clustering of dense vectors (common for local PoCs).

**Recall@k**  
Metric: fraction of queries where the correct/expected passage appears in the top-k retrieved results.

**Precision@k**  
Metric: how many of the top-k retrieved passages are relevant.

**Hybrid Retrieval**  
Combining vector (semantic) search with lexical/keyword search (e.g., BM25) for better precision.

**Reranker / Cross-encoder**  
A model that re-scores top candidate passages returned by the vector retriever to improve precision.

**Agentic RAG / Multi-Agent**  
A system where multiple LLM-driven agents (DocumentAgent, RegulationAgent, GovernanceAgent) perform specialized tasks and coordinate.

**Multimodal RAG**  
RAG that operates across modalities: text, images (signatures, seals), audio. Typically uses CLIP or other multimodal encoders.

**Hallucination**  
When an LLM generates plausible-sounding but factually incorrect or unsupported statements.

**Provenance / Citation**  
The original source metadata (document id, page, chunk id) associated with a retrieved passage — important for auditability.

**A/B Testing (for RAG)**  
Experimentation framework to compare two system variants (different embeddings, chunking, rerankers) using split traffic and significance testing.

**GDPR / HIPAA / SOC2**  
Examples of compliance frameworks that affect how you must design RAG systems when handling personal or sensitive data.

**Vector leakage**  
Risk that embeddings may reveal sensitive info; treat embeddings as sensitive data.

**Index Sharding**  
Splitting an index across multiple machines to scale search.

**Multi-hop Retrieval**  
Iterative retrieval process: use initial results to form follow-up queries and retrieve further relevant passages.

**Semantic Search**  
Search based on meaning (embeddings), not exact keyword matches.

**BM25**  
A popular lexical ranking algorithm used in keyword-based search systems.

