flowchart TD
  U[User Query] --> R[Retriever]
  R -->|top-k passages| G[Generator (LLM)]
  G --> A[Answer + Citations]
  subgraph KB["Knowledge Base"]
    D1[Doc chunk 1]
    D2[Doc chunk 2]
    D3[Doc chunk n]
  end
  R --- KB
