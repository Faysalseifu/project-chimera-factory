# MCP Configuration Blueprint

This document specifies required MCP configuration structure for local and CI environments. It does **not** include secrets.

## Goals
- Centralize MCP endpoints, tool allow‑lists, and resource allow‑lists.
- Provide a deterministic contract for agent runtime configuration.

## Config Layout (Example)
```yaml
mcp:
  servers:
    filesystem:
      url: "mcp://filesystem"
      allow_paths:
        - "/data/inputs"
        - "/data/outputs"
    git:
      url: "mcp://git"
    redis:
      url: "mcp://redis"
  tools:
    allow_list:
      - "ideogram_generate"
      - "twitter_post"
      - "openclaw_heartbeat"
  resources:
    allow_list:
      - "twitter://mentions"
      - "news://fashion"
```

## Required Fields
- `mcp.servers` for each server the runtime expects.
- `mcp.tools.allow_list` to constrain tool invocation.
- `mcp.resources.allow_list` to constrain resource access.

## Environment Binding
- Use environment variables for secrets only.
- Runtime must fail closed if required MCP servers are missing.

Last updated: 2026-02-06
