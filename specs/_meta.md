# Project Chimera: Master Meta Specification

## Purpose
Define the high-level vision, non-negotiable constraints, and success criteria for Project Chimera. This document anchors all downstream specs and provides the basis for traceability.

## Vision
Build a factory for Autonomous Influencer Agents: persistent, goal-directed digital entities that perceive trends, generate multimodal content, engage audiences, and manage on-chain commerce autonomously. Shift from scripted bots to a swarm-orchestrated network using the FastRender pattern (Planner–Worker–Judge), MCP for external connectivity, hierarchical memory, and Coinbase AgentKit wallets.

## Scope
- Defines vision, constraints, business models, and architectural pillars.
- Does not include implementation details.

## Core Constraints
- **Spec-Driven Development (SDD):** No implementation code until specs are ratified and tests are written (failing TDD).
- **Traceability:** All code must link back to these specs via comments or PR descriptions.
- **Scalability Target:** Support 1,000+ concurrent agents with auto-scaling.
- **Security:** Multi-tenancy isolation; non-custodial wallets encrypted via secrets manager.
- **Compliance:** EU AI Act self-disclosure; HITL for sensitive topics.
- **Cost Control:** Resource Governor to cap inference/media generation spend.

## Business Models Supported
- In-house Digital Talent Agency
- PaaS for brands/agencies
- Hybrid ecosystem with OpenClaw/Moltbook integration potential

## Key Architectural Pillars
- FastRender Swarm (Planner → TaskQueue → Workers → Judge with OCC)
- MCP Hub-and-Spoke integration model
- Hybrid Persistence (Weaviate semantic + PostgreSQL transactional + Redis queues)
- Agentic Commerce via Coinbase AgentKit

## Acceptance Criteria
- All new features reference a spec in specs/ and cite the relevant section.
- All planned components map to one or more architectural pillars.
- Non-negotiable constraints are verified in tests or review checklists before merge.

## Out of Scope
- UI/UX design details
- Vendor-specific implementation choices
- Production deployment details
