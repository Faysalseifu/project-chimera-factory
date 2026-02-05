# Skill: Fetch Trends

## Purpose
Fetch regional/niche trend signals to seed planning tasks.

## Interface
**Input**
```json
{"region":"ethiopia","niche":"fashion","time_window":"24h"}
```

**Output**
```json
{"trends":[{"topic":"sneaker drop","volume":1200,"sentiment":0.8}]}
```

## Constraints
- Contract must align with specs/technical.md Task JSON Schema.
- No direct external API calls without MCP tooling.

## Acceptance Criteria
- Input/output schema is documented and versioned.
