# OpenClaw / Moltbook Integration Plan

## Purpose
Define an optional integration path to extend Chimera agents into agent-native social networks for discovery, collaboration, and cross-promotions.

## Why Integrate?
Extend Chimera agents into agent-native social networks for discovery, collaboration, cross-promotions.

## Approach
- Run Chimera agents as OpenClaw instances (local deployment for privacy).
- Skills: skill_moltbook_post, skill_moltbook_upvote, skill_moltbook_heartbeat.
- Protocols: Post status/trends to Moltbook submolts (e.g., “fashion-influencers”).
- Reputation: Build via useful contributions (share trend analyses).
- On-chain: Use wallet for tipping/collaboration payments.

## Initial Skills
- **skill_publish_to_moltbook:** POST to Moltbook API (if exposed) or simulate via OpenClaw heartbeat.

## Constraints
- Integration must respect multi-tenant isolation.
- All posts must honor disclosure and HITL rules defined in specs/functional.md.

## Acceptance Criteria
- A minimal integration spec is defined and traceable to core constraints.
- Any Moltbook/OpenClaw skill has a documented interface.
