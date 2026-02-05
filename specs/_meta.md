# Project Chimera – Meta Specification

## Vision
Factory for **autonomous AI influencers**: persistent agents that research trends, plan content, generate multimodal posts (text/image/video), engage audiences naturally, and manage on-chain wallets/transactions with almost no human input.

## Core Decisions (aligned with SRS 2026)
- Architecture: FastRender swarm → Planner (decomposes goals), Workers (execute atomic tasks), Judge (quality + HITL gating + OCC)
- External world access: **Only via MCP** (no direct API calls in agent logic)
- Memory: Redis (short-term episodic) + Weaviate (long-term semantic RAG)
- Commerce: Coinbase AgentKit → non-custodial wallets on Base
- Safety: Confidence scoring + CFO Judge + mandatory HITL on sensitive topics
- Scalability: Kubernetes auto-scaling, target 1,000+ agents

## Hard Rules / Constraints
- Spec-Driven: No code until specs + failing tests exist
- Traceability: Every code change must link to a spec section
- No vibe coding: Follow TDD + strict schemas
- Compliance: Auto AI disclosure on posts + honesty directive on "are you AI?" questions
- Cost: Hard per-agent daily budget enforced by Judge

Last updated: 2026-02-05
