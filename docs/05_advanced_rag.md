# 05 — Advanced RAG Architectures

So far, we covered **basic RAG** → Query → Retriever → LLM.  
In practice, complex tasks need more advanced designs.  
This section covers **multi-hop, hierarchical, multimodal, graph, and agentic RAG**.

---

## 🔄 1. Multi-hop RAG
**Problem:** Some questions require combining info from multiple docs.  

**How it works:**
1. Retrieve → LLM asks clarifying sub-questions.  
2. Retrieve again with refined queries.  
3. Combine results into final answer.  

**Example:**
- Q: *“Compare KYC rules of RBI and GDPR data processing rules.”*  
- Hop 1 → retrieve RBI rule.  
- Hop 2 → retrieve GDPR rule.  
- Hop 3 → combine into comparative answer.  


Query → Retriever → LLM (sub-query) → Retriever → Final Answer


**FAQ:**  
- *Why not just one retrieval?* → Because context windows are limited, multi-hop ensures each step is focused.  
- *When to use?* → Multi-doc reasoning, comparisons, long chains of logic.  

---

## 🗂️ 2. Hierarchical RAG
**Problem:** Large docs (contracts, reports) overwhelm retrievers.  

**How it works:**
- Use **document hierarchies**: section → clause → sentence.  
- Retrieval works in levels.  

**Example:**  
- First retrieve section "Termination."  
- Then retrieve relevant clauses.  
- Then retrieve sentences.  


**FAQ:**  
- *Why hierarchical?* → Cuts noise, improves precision.  
- *When to use?* → Long reports, research papers, 100+ page contracts.  

---

## 🖼️ 3. Multimodal RAG
**Problem:** Compliance docs have images, seals, logos, tables.  
**Solution:** Combine **text + vision models**.  

**How it works:**
- Use OCR → extract text.  
- Use vision embeddings (e.g., CLIP, GPT-4o vision) → embed images/logos.  
- Store both in a **multi-modal index**.  

**Example:**  
- Query: “Check if the seal on this invoice is valid.”  
- Retriever pulls **image embedding** of the seal + text context.  
- LLM validates both.  

**FAQ:**  
- *Why not text-only?* → Fraud risk → fake seals, altered tables.  
- *When to use?* → Invoices, KYC forms, contracts with signatures.  

---

## 🌐 4. Graph-Enhanced RAG
**Problem:** Plain vectors capture similarity, but not **relationships**.  

**Solution:** Add a **knowledge graph** (entities + relationships).  

**How it works:**
- Step 1: Entity linking (map “RBI” → entity).  
- Step 2: Use graph traversal to expand context.  
- Step 3: Use hybrid retrieval (graph + vectors).  

**Example:**  
- Q: *“Which RBI regulations apply to foreign bank KYC?”*  
- Graph: [RBI] → [KYC] → [Foreign Banks]  
- Retriever finds the relevant section via graph.  

**FAQ:**  
- *Why add graphs?* → Improves reasoning beyond “semantic closeness.”  
- *When to use?* → Complex domains (law, compliance, pharma).  

---

## 🤖 5. Agentic RAG
**Problem:** A single LLM struggles with all tasks.  

**Solution:** Multi-agent orchestration.  

**Typical Agents:**
- **Document Agent** → parses docs, extracts fields.  
- **Regulation Agent** → retrieves relevant rules.  
- **Governance Agent** → validates and explains risks.  

**Flow Example (EY-style Compliance Copilot):**
1. DocAgent → OCR invoice, extract amounts.  
2. RegAgent → retrieve RBI circular on AML.  
3. GovAgent → explain “Amount exceeds AML threshold.”  

**FAQ:**  
- *Why multiple agents?* → Separation of roles = better interpretability.  
- *When to use?* → Workflows needing explainability & audit trail.  

---

## ⚖️ Architecture Comparison

| Architecture   | Best For | Trade-offs |
|----------------|----------|------------|
| Multi-hop RAG  | Reasoning across docs | More queries = higher cost |
| Hierarchical   | Long structured docs  | Needs doc parsing |
| Multimodal     | Docs with images/seals | Needs OCR + vision models |
| Graph RAG      | Entity relationships | Requires graph building |
| Agentic RAG    | Explainability, workflows | Orchestration overhead |

---

## 🎯 Key Takeaways
- **Multi-hop** = better reasoning.  
- **Hierarchical** = precision in long docs.  
- **Multimodal** = handle images + text.  
- **Graph** = structured relationships.  
- **Agentic** = explainable, auditable workflows.  

Advanced RAG = tailor architecture to the **problem domain**.  
Compliance, law, and pharma often benefit from **multimodal + agentic RAG**.

---

Next → [Production RAG: Testing, Security, and Scaling](06_production_rag.md)





