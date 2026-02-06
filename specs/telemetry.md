# Telemetry & Observability

This document defines minimum telemetry required for agentic runtime visibility.

## Signals
- Task queue depth and throughput.
- Judge decisions by category and confidence.
- HITL queue latency and outcomes.
- Spend per agent per day.
- MCP tool call latency and error rate.

## Required Metrics (Names are illustrative)
- `chimera.task.queue_depth`
- `chimera.task.throughput`
- `chimera.judge.decision_rate`
- `chimera.hitl.latency_ms`
- `chimera.spend.usd_daily`
- `chimera.mcp.error_rate`

## Logs
- Structured JSON logs for task execution.
- Correlate `task_id` across Planner → Worker → Judge.

## Tracing
- Include `trace_id` in all task payloads and logs.

Last updated: 2026-02-06
