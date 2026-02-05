# Skill: Send USDC Payment

## Purpose
Execute on-chain USDC transfers under CFO Judge controls.

## Interface
**Input**
```json
{
  "from_wallet": "string",
  "to_wallet": "string",
  "amount_usdc": 0.0,
  "chain": "base|ethereum",
  "memo": "string"
}
```

**Output**
```json
{
  "tx_hash": "string",
  "status": "submitted|confirmed|failed"
}
```

## Constraints
- Must validate daily spend limits before submission.
- Non-custodial keys must remain in secrets manager.

## Acceptance Criteria
- Input/output schema is documented and versioned.
