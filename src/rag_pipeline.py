# src/rag_pipeline.py
"""
RAGPipeline: class wrapper that connects retriever + LLM prompt generation.
This file demonstrates how to format retrieved passages into a prompt and call an LLM.
Replace `call_llm` with your Azure/OpenAI or other LLM API call.
"""

import os
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

from src.simple_rag import load_index, retrieve  # reuse simple_rag utilities

# LLM call placeholder: implement with azure/openai SDK in production
def call_llm(prompt: str) -> str:
    """
    Replace this with actual call to Azure OpenAI (or OpenAI) model.
    For PoC you can return a dummy response or call OpenAI if you have an API key.
    """
    # Example (uncomment & configure if using openai package):
    # import openai, os
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # resp = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
    # return resp.choices[0].message.content
    return "LLM response placeholder. Replace call_llm with real API call."

class RAGPipeline:
    def __init__(self, model_name: str = "all-mpnet-base-v2", index_dir: str = "data/embeddings"):
        self.model_name = model_name
        self.index_dir = index_dir
        self.model, self.index, self.metadata = load_index(index_dir, model_name)

    def retrieve_topk(self, query: str, k: int = 5):
        return retrieve(query, self.model, self.index, self.metadata, k=k)

    def build_prompt(self, query: str, retrieved: List[Dict], max_chars: int = 3000) -> str:
        """
        Build a prompt that provides retrieved passages as sources and asks the model
        to answer using those sources only. Include small instructions for citations.
        """
        pieces = []
        for i, r in enumerate(retrieved):
            pieces.append(f"[SRC_{i+1}] (Doc:{r['doc_id']}, Chunk:{r['chunk_id']})\n{r['text']}\n")
        context = "\n\n".join(pieces)
        prompt = (
            "You are a compliance assistant. Use only the provided sources to answer the question. "
            "Cite sources by label (e.g., [SRC_1]). If answer is not present in sources, say 'INSUFFICIENT DATA'.\n\n"
            f"SOURCES:\n{context}\n\n"
            f"QUESTION: {query}\n\n"
            "Answer concisely, provide YES/NO if applicable, short explanation, and cite sources."
        )
        # Trim if too long (naive)
        if len(prompt) > max_chars:
            prompt = prompt[:max_chars]
        return prompt

    def answer(self, query: str, k: int = 5) -> Dict:
        retrieved = self.retrieve_topk(query, k=k)
        prompt = self.build_prompt(query, retrieved)
        llm_out = call_llm(prompt)
        return {"query": query, "retrieved": retrieved, "prompt": prompt, "llm_out": llm_out}
