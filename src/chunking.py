"""
chunking.py
------------
Utility functions for splitting text into chunks for RAG.

Supports:
- Fixed-size chunking
- Overlapping chunking
- Semantic chunking (sentence-based)
"""

import re
from typing import List

def fixed_chunking(text: str, chunk_size: int = 500) -> List[str]:
    """
    Split text into fixed-size chunks (by words).
    """
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]

def overlapping_chunking(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Split text into overlapping chunks.
    Overlap helps preserve context across boundaries.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        if i + chunk_size >= len(words):
            break
    return chunks

def semantic_chunking(text: str, max_len: int = 300) -> List[str]:
    """
    Split text by sentences and group into semantic chunks.
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) > max_len:
            chunks.append(current.strip())
            current = sentence
        else:
            current += " " + sentence
    if current:
        chunks.append(current.strip())
    return chunks

if __name__ == "__main__":
    sample_text = (
        "The Reserve Bank of India requires strict KYC checks. "
        "Contracts must include clear terms. Fake seals can lead to fraud. "
        "GDPR mandates user consent for personal data usage."
    )

    print("Fixed chunks:", fixed_chunking(sample_text, 10))
    print("Overlapping chunks:", overlapping_chunking(sample_text, 10, 3))
    print("Semantic chunks:", semantic_chunking(sample_text, 50))

