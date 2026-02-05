# Skill: Fetch & Filter Trends

## Purpose
Fetch news/social trends → semantic filter for agent goals → output relevant items

## Input JSON Schema
```json
{
  "region": "ethiopia",
  "niches": ["fashion", "sneakers"],
  "hours": 24,
  "threshold": 0.75
}
```

## Output JSON Schema
```json
{
  "trends": [
    {
      "topic": "summer collection drop",
      "relevance_score": 0.88,
      "volume": 4500,
      "sources": ["url1", "url2"]
    }
  ]
}
```

Implementation later – this is contract only.
