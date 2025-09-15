# src/agents.py
"""
Simple agent scaffolding:
- DocumentAgent: Accepts uploaded text/PDF, returns extracted text chunks (uses OCR externally)
- RegulationAgent: Uses RAGPipeline to fetch relevant regulations
- GovernanceAgent: Applies business rules and composes final explanation (calls LLM via RAGPipeline)

This is intentionally simple to keep the capstone scope reasonable.
"""

from typing import Dict, List
from src.rag_pipeline import RAGPipeline

class DocumentAgent:
    def __init__(self):
        pass

    def ingest_text(self, text: str) -> Dict:
        """
        For PoC we accept plain text (from .txt or OCRed PDF).
        Returns a dict with 'text' and potential extracted fields (stub).
        """
        # In real system: call Azure Document Intelligence -> extract tables, bbox, metadata
        return {"text": text, "fields": {}}

class RegulationAgent:
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag = rag_pipeline

    def find_relevant(self, query: str, k: int = 5):
        return self.rag.retrieve_topk(query, k=k)

class GovernanceAgent:
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag = rag_pipeline

    def validate(self, contract_snippet: str, compliance_question: str) -> Dict:
        """
        Validate contract snippet against compliance question using RAG pipeline.
        Returns a structured response with citations and LLM explanation.
        """
        # Build a combined query for retrieval (could be more sophisticated)
        combined_query = f"{compliance_question}\nContract snippet: {contract_snippet}"
        return self.rag.answer(combined_query, k=5)

# Example usage (for local testing)
if __name__ == "__main__":
    # requires pre-built index
    rag = RAGPipeline()
    doc_agent = DocumentAgent()
    reg_agent = RegulationAgent(rag)
    gov_agent = GovernanceAgent(rag)

    # simulate ingest
    doc = doc_agent.ingest_text("Sample contract text mentioning KYC threshold ₹10 lakh and AML checks.")
    out = gov_agent.validate(doc["text"], "Does this contract comply with RBI KYC rules for high-value transactions?")
    print("GovernanceAgent output:")
    print(out["llm_out"])
