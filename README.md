# Project Chimera Factory

Spec-driven infrastructure for autonomous AI influencers.

## Important Development Rules (Manual Enforcement)
- ALWAYS read the relevant file in /specs/ before writing any code
- Write failing tests FIRST (in /tests/) before implementation
- Every function/class should have a comment linking back to specs:
  # Implements task_type 'generate_image' from specs/technical.md
- No direct API calls — everything must go through MCP
- Use strict typing (Pydantic preferred) for inputs/outputs
- Prefer async Python where appropriate
- Commit often with clear messages
