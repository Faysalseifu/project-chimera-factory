# Acceptance Criteria – Task 3 Baseline

This document defines the minimum acceptable outcomes to consider the Chimera foundation “end‑to‑end ready” for Task 3.

## Scope
- Applies to repo scaffolding, specs, contracts, tests, containerization, and CI.
- Focuses on deterministic verification via tests, checks, and CI gates.

## Required Outcomes
1) **Spec Coverage**
   - All top‑level specs are present: meta, functional, technical, integration.
   - Each skill contract maps to a `task_type` in [specs/technical.md](specs/technical.md).

2) **Contracts & Schemas**
   - Each skill README includes input/output schemas with required fields.
   - Task payload and judge output schema are unambiguous and validated by tests.

3) **Tests & TDD**
   - Unit tests validate all schema contracts under [tests/](tests/).
   - `pytest` completes with exit code 0 in CI.

4) **Containerization & CI**
   - Docker build succeeds without manual steps.
   - CI runs lint/test steps and fails on schema violations.

5) **Traceability**
   - Each implemented function/class includes a comment linking to a spec section.
   - Changes include references to spec sections in PR description.

## Stretch (Recommended)
- Live MCP connectivity tests in a sandbox environment.
- Telemetry dashboards for queue throughput and HITL latency.

Last updated: 2026-02-06
