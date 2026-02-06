# Project Chimera Factory

Spec-driven infrastructure for autonomous AI influencers.

## New Coverage (Task 3 Gaps)
- Acceptance criteria: [specs/acceptance_criteria.md](specs/acceptance_criteria.md)
- MCP config blueprint: [specs/mcp_config.md](specs/mcp_config.md)
- Security blueprint: [specs/security_blueprint.md](specs/security_blueprint.md)
- Telemetry requirements: [specs/telemetry.md](specs/telemetry.md)
- Frontend intent: [docs/frontend_intent.md](docs/frontend_intent.md)
- Agentic telemetry (visible signals): [docs/agentic_telemetry.md](docs/agentic_telemetry.md)

## Important Development Rules (Manual Enforcement)
- ALWAYS read the relevant file in /specs/ before writing any code
- Write failing tests FIRST (in /tests/) before implementation
- Every function/class should have a comment linking back to specs:
  # Implements task_type 'generate_image' from specs/technical.md
- No direct API calls — everything must go through MCP
- Use strict typing (Pydantic preferred) for inputs/outputs
- Prefer async Python where appropriate
- Commit often with clear messages
