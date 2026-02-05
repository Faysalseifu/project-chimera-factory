# Tooling Strategy

## Purpose
Define development MCP tools and runtime skills strategy for Chimera.

## Developer Tools (MCP for Development)
- **git-mcp:** Version control queries (diffs, blame).
- **filesystem-mcp:** Safe file read/write in IDE.
- **db-mcp (sqlite):** Local test DB.
- **tenx-mcp-sense:** Continuous traceability.

## Runtime Skills (Agent Capabilities)
Skills are reusable functions/packages agents call via MCP or direct import.

### Skill Requirements
- Each skill must declare a JSON input/output contract.
- Each skill must map back to specs/technical.md.

## Acceptance Criteria
- All listed tools are documented with intended usage.
- At least three skill stubs exist with defined interfaces.
