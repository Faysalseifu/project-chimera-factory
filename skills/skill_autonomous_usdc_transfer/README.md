# Skill: Autonomous USDC Transfer

## Purpose
Execute on-chain USDC transfers under CFO Judge controls.

## Input JSON Schema
```json
{
  "from_wallet": "string",
  "to_wallet": "string",
  "amount_usdc": 0.0,
  "chain": "base|ethereum",
  "memo": "string"
}
```

## Output JSON Schema
```json
{
  "tx_hash": "string",
  "status": "submitted|confirmed|failed"
}
```

Implementation later – this is contract only.
