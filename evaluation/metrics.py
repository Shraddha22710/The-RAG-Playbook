# evaluation/metrics.py
"""
Utility functions to compute basic retrieval metrics for RAG experiments.
- recall_at_k
- precision_at_k

Input format expectations:
- results: List[List[str]] where results[i] is the list of doc/chunk ids retrieved for query i (ordered)
- ground_truth: List[Set[str]] where ground_truth[i] is the set of correct doc/chunk ids for query i
"""

from typing import List, Set

def recall_at_k(results: List[List[str]], ground_truth: List[Set[str]], k: int = 5) -> float:
    assert len(results) == len(ground_truth)
    hits = 0
    for res, gt in zip(results, ground_truth):
        topk = res[:k]
        if any(r in gt for r in topk):
            hits += 1
    return hits / len(results) if results else 0.0

def precision_at_k(results: List[List[str]], ground_truth: List[Set[str]], k: int = 5) -> float:
    assert len(results) == len(ground_truth)
    precisions = []
    for res, gt in zip(results, ground_truth):
        topk = res[:k]
        if not topk:
            precisions.append(0.0)
            continue
        p = sum(1 for r in topk if r in gt) / len(topk)
        precisions.append(p)
    return sum(precisions) / len(precisions) if precisions else 0.0

def mean_reciprocal_rank(results: List[List[str]], ground_truth: List[Set[str]]) -> float:
    """
    MRR: average of 1/rank for first relevant result.
    """
    assert len(results) == len(ground_truth)
    rr_sum = 0.0
    for res, gt in zip(results, ground_truth):
        rank = None
        for i, r in enumerate(res, start=1):
            if r in gt:
                rank = i
                break
        rr_sum += (1.0 / rank) if rank else 0.0
    return rr_sum / len(results) if results else 0.0

if __name__ == "__main__":
    # quick sanity check
    results = [["doc1#0", "doc2#3", "doc3#0"], ["doc4#1", "doc2#0"]]
    gt = [set(["doc2#3"]), set(["doc4#1"])]
    print("Recall@3:", recall_at_k(results, gt, k=3))
    print("Precision@3:", precision_at_k(results, gt, k=3))
    print("MRR:", mean_reciprocal_rank(results, gt))

