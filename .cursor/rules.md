# Project Chimera Rules for Cursor / AI Co-pilot

## Project Context
This is Project Chimera: a spec-driven factory for autonomous AI influencers using FastRender swarm, MCP, hierarchical memory, and agentic commerce.

## Prime Directive
NEVER generate or suggest implementation code without first referencing and linking to specs/*.md files.
Always explain your plan in comments before writing code.
If specs are ambiguous, ask for clarification or propose spec updates via PR.

## Key Behaviors
- **Traceability:** Every code suggestion must include: “This implements FR X from functional.md” or “Aligns with schema in technical.md”.
- **TDD First:** Write failing tests before implementation.
- **Spec Alignment:** Before any change, read relevant specs.
- **No Vibe Coding:** No quick hacks; everything must be traceable, testable, scalable.

## Acceptance Criteria
- Any AI-generated change references a spec and provides traceability.
- Tests precede implementation changes.
