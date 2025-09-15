# src/app.py
"""
Streamlit demo app (minimal).
- Upload a .txt file or paste text
- Ask a compliance question
- App runs DocumentAgent -> RegulationAgent/GovernanceAgent and shows retrieved sources + LLM output

Note: For demo, call_llm in rag_pipeline returns a placeholder. Configure it to call Azure/OpenAI.
"""

import streamlit as st
from src.agents import DocumentAgent, RegulationAgent, GovernanceAgent
from src.rag_pipeline import RAGPipeline

st.set_page_config(page_title="Governance-Aware Compliance Copilot", layout="wide")

st.title("Governance-Aware Compliance Copilot — Demo")

with st.sidebar:
    st.header("Controls")
    data_dir = st.text_input("Data directory (embeddings index)", "data/embeddings")
    model_name = st.text_input("Embedding model", "all-mpnet-base-v2")
    if st.button("Load RAG index"):
        try:
            rag = RAGPipeline(model_name=model_name, index_dir=data_dir)
            st.success("RAG index loaded.")
            st.session_state["rag"] = rag
        except Exception as e:
            st.error(f"Failed to load index: {e}")

col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("Document input")
    uploaded = st.file_uploader("Upload .txt file (or paste)", type=["txt"])
    text_area = st.text_area("Or paste document text here", height=200)

    if uploaded:
        raw = uploaded.read().decode("utf-8")
        doc_text = raw
    else:
        doc_text = text_area

    question = st.text_input("Compliance question (example: Does this contract require additional KYC?)")

    if st.button("Run analysis"):
        if not doc_text:
            st.warning("Please upload or paste a document text.")
        elif "rag" not in st.session_state:
            st.warning("Please load RAG index from sidebar first.")
        else:
            rag: RAGPipeline = st.session_state["rag"]
            doc_agent = DocumentAgent()
            gov_agent = GovernanceAgent(rag)
            doc = doc_agent.ingest_text(doc_text)
            with st.spinner("Running Governance Agent..."):
                result = gov_agent.validate(doc["text"], question)
            st.session_state["last_result"] = result
            st.success("Analysis complete. See results on the right.")

with col2:
    st.subheader("Results")
    if "last_result" in st.session_state:
        res = st.session_state["last_result"]
        st.markdown("**LLM Output**")
        st.write(res["llm_out"])

        st.markdown("**Retrieved Sources (top-k)**")
        for i, r in enumerate(res["retrieved"]):
            st.markdown(f"**[SRC_{i+1}]** Doc: `{r['doc_id']}` Chunk: `{r['chunk_id']}` — Score: {r['score']:.3f}")
            st.write(r["text"])
            st.markdown("---")
    else:
        st.info("No results to show. Run the analysis to populate results.")
