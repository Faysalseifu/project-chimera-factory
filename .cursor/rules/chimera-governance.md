---
description: Core governance rules for Project Chimera – enforce spec-first development
type: alwaysApply
---

# Chimera Project Rules – Enforce Discipline

## Project Identity
This is **Project Chimera**: spec-driven factory building autonomous AI influencer agents using FastRender swarm, MCP-only external access, Weaviate memory, and Coinbase AgentKit wallets.

## Prime Directive – Break this and you fail
1. **NEVER** write Python code, JSON schemas, Dockerfile lines, or any implementation unless you first quote/link the exact section from /specs/
2. If specs are unclear/missing → **propose spec update** (never bypass)
3. Start every answer with:
   - Relevant spec file(s):
   - Key requirements / acceptance criteria:
   - Step-by-step plan (English first):

## Mandatory Patterns
- TDD first: suggest failing test → then implementation
- Link back: # Implements generate_image from specs/technical.md
- Strict typing: always use Pydantic for inputs/outputs
- MCP only: no direct requests.get(), coinbase sdk calls, etc.
- Async Python + docstrings everywhere

## Forbidden
- Global variables outside Redis/DB
- Hard-coded keys/secrets
- Vibe-coding quick hacks

Follow these always in this project.
