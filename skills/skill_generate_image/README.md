# Skill: Generate Image

## Purpose
Generate persona-consistent images for campaigns.

## Interface
**Input**
```json
{
  "prompt": "string",
  "character_reference_id": "string",
  "style": "string",
  "aspect_ratio": "string"
}
```

**Output**
```json
{
  "image_url": "string",
  "provider": "string",
  "content_hash": "string"
}
```

## Constraints
- Must enforce character consistency (reference id required).
- All outputs must be auditable and cached.

## Acceptance Criteria
- Input/output schema is documented and versioned.
