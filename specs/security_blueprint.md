# Security Blueprint

Security is mandatory for all agent actions, storage, and on‑chain operations.

## Objectives
- Prevent unauthorized tool/resource access.
- Protect secrets and wallet material.
- Ensure auditable, reversible operations where possible.

## Trust Boundaries
- **Agent Runtime**: untrusted inputs, no direct API access.
- **MCP Layer**: enforced allow‑lists and rate limits.
- **Storage**: segregated networks and least‑privilege roles.

## Controls
1) **Secrets Management**
   - No secrets in repo or specs.
   - Use environment variables or secret manager.

2) **Wallet Safety**
   - Non‑custodial wallets only.
   - Multi‑sig for treasury or high‑value transfers.
   - Daily spend limit enforced by Judge.

3) **Tool Access**
   - MCP allow‑list must be explicit.
   - Deny‑by‑default policy for new tools/resources.

4) **Data Protection**
   - Encrypt at rest for Postgres and Weaviate.
   - TLS for all MCP transport.

5) **Auditability**
   - Append‑only logs for task execution and approvals.
   - HITL decisions stored with timestamps and rationale.

Last updated: 2026-02-06
