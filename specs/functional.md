# Functional Requirements Specification

## Purpose
Define user stories and functional capabilities for Autonomous Influencer Agents, including acceptance criteria and escalation rules.

## User Roles
- **Network Operator:** Sets high-level goals (e.g., “Promote sneaker drop to Gen‑Z in Ethiopia”).
- **HITL Moderator:** Reviews escalated content/transactions.
- **Developer:** Extends MCP servers, skills, prompts.

## Agent Capabilities (User Stories)
- **As an Agent, I need to perceive trends and mentions so that I can react timely.**
  - Acceptance Criteria:
    - Poll MCP Resources (twitter://mentions, news://ethiopia/fashion).
    - Apply semantic filter.
    - If relevance $> 0.75$, create a task in the queue.

- **As an Agent, I need to decompose goals into executable tasks so that complex campaigns are parallelized.**
  - Acceptance Criteria:
    - Planner reads goal.
    - Outputs a DAG of tasks.
    - Pushes tasks to Redis TaskQueue.

- **As an Agent, I need to generate consistent multimodal content so that persona is maintained.**
  - Acceptance Criteria:
    - Worker uses MCP Tools (text: Gemini/Claude, image: Ideogram with character_reference_id, video: tiered strategy).
    - Judge validates consistency (Vision API check).

- **As an Agent, I need to engage bi-directionally so that interactions feel natural.**
  - Acceptance Criteria:
    - Full loop: Ingest → Plan → Generate → Act (via MCP) → Judge.

- **As an Agent, I need to manage finances autonomously so that I can self-sustain.**
  - Acceptance Criteria:
    - Non-custodial wallet.
    - Check balance before spend.
    - CFO Judge enforces daily limits.
    - On-chain transfers recorded.

- **As an Agent, I need to disclose AI nature when asked so that compliance is met.**
  - Acceptance Criteria:
    - Honesty Directive overrides persona on direct queries.

## HITL Escalation Rules
- Confidence $> 0.90$: Auto-approve
- $0.70 \leq$ Confidence $\leq 0.90$: Async pending
- Confidence $< 0.70$ or sensitive topic: Mandatory HITL

## Constraints
- All behaviors must be traceable to specs/_meta.md.
- No implementation code before tests are written (TDD-first).

## Acceptance Criteria (Spec-Level)
- All functional stories include measurable acceptance criteria.
- Escalation rules are enforced for all content and finance actions.
