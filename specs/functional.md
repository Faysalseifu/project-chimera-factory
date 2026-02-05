# Functional Requirements – Chimera Agents

## As Network Operator
- Define natural-language campaign goals ("Promote Ethiopian fashion trends to Gen-Z")
- Monitor fleet dashboard: wallet balances, HITL queue, daily spend, agent states
- Approve/reject escalated items quickly

## As Autonomous Agent – I must be able to:
1. **Perceive**  
   Poll MCP resources → filter relevance (>0.75) → detect trends → create tasks

2. **Plan**  
   Decompose goal into task DAG → re-plan on changes (news, budget, viral events)

3. **Create content**  
   Text: Gemini/Claude  
   Image: consistent character (reference ID / LoRA)  
   Video: tiered (cheap motion vs expensive full gen)

4. **Act**  
   Publish/reply via MCP tools with AI label  
   Execute transfers after CFO approval

5. **Govern self**  
   Check balance before spend  
   Auto-disclose AI identity when asked  
   Store successful interactions in memory

## HITL & Confidence Tiers
- ≥ 0.92 → auto-publish  
- 0.75–0.91 → async HITL (agent continues)  
- < 0.75 or politics/health/finance/legal → block + HITL
