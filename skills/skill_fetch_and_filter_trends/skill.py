"""Contract-first stub for the fetch and filter trends skill."""

from __future__ import annotations

from typing import Iterable


def fetch_and_filter_trends(
    region: str,
    niches: Iterable[str],
    hours: int,
    threshold: float,
) -> dict:
    """Return a minimal contract-compliant trends payload.

    Implements task_type 'perceive_trends' from specs/technical.md.
    """

    topics = list(niches) or ["general"]
    return {
        "trends": [
            {
                "topic": f"{topics[0]} trend in {region}",
                "relevance_score": float(threshold),
                "volume": max(hours, 1),
                "sources": [],
            }
        ]
    }
