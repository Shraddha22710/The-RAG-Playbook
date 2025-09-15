# src/simple_rag.py
"""
Minimal RAG demo:
- Build embeddings from plain-text documents (data/documents/*.txt)
- Create FAISS index and metadata (saved in data/embeddings/)
- Query index and print top-k chunks

Usage:
    python src/simple_rag.py --build-index --data-dir data/documents
    python src/simple_rag.py --query "What is RBI KYC limit?"
"""

import os
import glob
import json
import argparse
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from tqdm import tqdm

EMBED_MODEL = "all-mpnet-base-v2"
INDEX_DIR = "data/embeddings"
INDEX_PATH = os.path.join(INDEX_DIR, "faiss.index")
META_PATH = os.path.join(INDEX_DIR, "metadata.json")

def load_documents(data_dir: str) -> List[Dict]:
    docs = []
    for path in glob.glob(os.path.join(data_dir, "*.txt")):
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        docs.append({"id": os.path.basename(path), "text": text})
    return docs

def chunk_text_semantic(text: str, max_tokens: int = 400, overlap: int = 50) -> List[str]:
    # simple sentence splitter chunker — replace with chunking.chunking functions if present
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    chunks = []
    cur = []
    cur_len = 0
    for s in sentences:
        tcount = len(s.split())
        if cur and (cur_len + tcount > max_tokens):
            chunks.append(" ".join(cur).strip())
            if overlap > 0:
                # keep last 'overlap' words as overlap context
                ow = " ".join(" ".join(cur).split()[-overlap:])
                cur = [ow] if ow else []
                cur_len = len(ow.split()) if ow else 0
            else:
                cur = []
                cur_len = 0
        cur.append(s)
        cur_len += tcount
    if cur:
        chunks.append(" ".join(cur).strip())
    return chunks

def build_index(docs: List[Dict], model_name: str = EMBED_MODEL, out_dir: str = INDEX_DIR):
    os.makedirs(out_dir, exist_ok=True)
    model = SentenceTransformer(model_name)
    chunks = []
    metadata = []
    for doc in docs:
        doc_id = doc["id"]
        doc_chunks = chunk_text_semantic(doc["text"])
        for i, c in enumerate(doc_chunks):
            chunks.append(c)
            metadata.append({"doc_id": doc_id, "chunk_id": i, "text": c})
    print(f"[build_index] total chunks: {len(chunks)}")
    embeddings = model.encode(chunks, convert_to_numpy=True, show_progress_bar=True)
    # normalize for cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    embeddings = embeddings / (norms + 1e-10)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype("float32"))
    faiss.write_index(index, os.path.join(out_dir, "faiss.index"))
    with open(os.path.join(out_dir, "metadata.json"), "w", encoding="utf-8") as fh:
        json.dump(metadata, fh, ensure_ascii=False, indent=2)
    print(f"[build_index] index and metadata saved to {out_dir}")

def load_index(index_dir: str = INDEX_DIR, model_name: str = EMBED_MODEL):
    model = SentenceTransformer(model_name)
    index_path = os.path.join(index_dir, "faiss.index")
    meta_path = os.path.join(index_dir, "metadata.json")
    if not os.path.exists(index_path) or not os.path.exists(meta_path):
        raise FileNotFoundError("Index or metadata not found. Run with --build-index first.")
    index = faiss.read_index(index_path)
    with open(meta_path, "r", encoding="utf-8") as fh:
        metadata = json.load(fh)
    return model, index, metadata

def retrieve(query: str, model: SentenceTransformer, index: faiss.Index, metadata: List[Dict], k: int = 5):
    qv = model.encode([query], convert_to_numpy=True)
    qv = qv / (np.linalg.norm(qv, axis=1, keepdims=True) + 1e-10)
    D, I = index.search(qv.astype("float32"), k)
    results = []
    for score, idx in zip(D[0], I[0]):
        meta = metadata[idx]
        results.append({"score": float(score), "doc_id": meta["doc_id"], "chunk_id": meta["chunk_id"], "text": meta["text"]})
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-index", action="store_true")
    parser.add_argument("--data-dir", type=str, default="data/documents")
    parser.add_argument("--query", type=str, default=None)
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args()

    if args.build_index:
        docs = load_documents(args.data_dir)
        build_index(docs)
        return

    if args.query:
        model, index, metadata = load_index()
        res = retrieve(args.query, model, index, metadata, k=args.k)
        print("Top results:")
        for r in res:
            print(f"[{r['score']:.3f}] {r['doc_id']} / chunk {r['chunk_id']}\n{r['text']}\n---")

if __name__ == "__main__":
    main()
