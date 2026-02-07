"""Contract-first stub for the fetch trends skill."""

from __future__ import annotations


def fetch_trends(region: str, niche: str, time_window: str) -> dict:
    """Return a minimal contract-compliant trends payload.

    Implements task_type 'perceive_trends' from specs/technical.md.
    """

    return {
        "trends": [
            {
                "topic": f"{niche} trend in {region}",
                "volume": 1,
                "sentiment": 0.0,
            }
        ]
    }
