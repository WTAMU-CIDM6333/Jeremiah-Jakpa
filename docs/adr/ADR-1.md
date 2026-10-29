# ADR-1 — Mentalysis orchestration on OpenCode

Date: 2026-10-25. Status: proposed implementation; flight evidence pending.
Governance: [ADR-0.2.0](../../design/adr/pre-release/ADR-0.2.0-mentalysis-e2/ADR-0.2.0-mentalysis-e2.md).
Product: [PRD](../PRD.md). Course label ADR-1 is distinct from gzkit's versioned ID.

## Context

A finance student needs a traceable arithmetic check followed by a review of
the assumptions making that calculation meaningful. E1 already supplies a
bounded educational agent. Its Chase is unavailable, so E1 has NOT FLOWN.
The operator requested E2 preparation before revisiting that review dependency.
This ordering deviation does not supply instructor approval or flight evidence.

## Decision and declared call order

Use OpenCode's **orchestrator–workers** pattern, with a fixed sequential
two-worker route for this bounded question:

1. Primary `mentalysis-e2` calls `mentalysis-calculation` once.
2. Only after that call returns, the primary calls `mentalysis-assumptions`
   once with the original question and the first worker's result.
3. Only after the second return, the primary produces a final text synthesis.

The task tool and child sessions are the implementation. There are no custom
commands for this chosen pattern. The sequencing is prompted behavior that the
sortie must observe, **not a deterministic graph enforced by the runtime**.

All agents explicitly use `opencode/big-pickle`. Primary steps: 5; worker steps:
3 each. These are per-agent budgets, not a shared five-step or five-call budget.
For the E1 question, the oracle remains `100 / (0.10 - 0.03) = 1428.57` currency
units, subject to WACC > g and constant perpetual growth.

The E2 primary's `permission.task` has `"*": deny` first, then exact allows for
`mentalysis-calculation` and `mentalysis-assumptions`. This excludes built-ins,
unknown future workers, and the registered negative-control
`mentalysis-e2-probe`. Workers cannot delegate. The primary and workers deny
edits and bash; E3 will separately test its required ask/local-model policy.
The original E1 primary and `opencode.json` remain unchanged. Start E2 with
explicit agent selection; do not assume the project default selects E2.

## Alternatives and scorecard

Scores: 1 = substantial project work/poor fit, 3 = workable with integration,
5 = strong direct support for this exercise. These are design judgments from
the cited documentation, not measured benchmark results. Weighted total is
the sum of score times weight; maximum 100.

| Criterion | Weight | OpenCode agents | LangGraph | Pydantic AI |
| --- | ---: | ---: | ---: | ---: |
| Fit to required OpenCode flight/export substrate | 6 | 5 | 1 | 1 |
| Named delegate permissions supplied by chosen runtime | 4 | 5 | 2 | 3 |
| Code-enforced sequential control and branching | 4 | 2 | 5 | 5 |
| Typed inter-stage contracts | 3 | 2 | 4 | 5 |
| Setup effort for this two-worker educational slice | 3 | 5 | 2 | 3 |
| **Weighted total / 100** | **20** | **79** | **52** | **62** |

### OpenCode

Provides agent files, Task delegation, session evidence, and a per-primary
allowlist without writing a dispatcher or provider integration. Worker output
schemas are text conventions; the model may omit or reorder stages. The runtime
can reject a delegate, but the prompt alone cannot guarantee the route.

### LangGraph

Its documented graph nodes, edges, conditional edges, and `Send` API can encode
worker routing and state handoff in application code. A graph can make the
assumption-review node unreachable until calculation finishes: **something
this prompt-directed OpenCode pattern does not mechanically guarantee**.
Persistence/checkpoint support is valuable for longer workflows. Adopting it
here would add Python workflow/provider code and require an integration back
into the course's required OpenCode evidence substrate. An allowlisted route
is application logic, not automatically OpenCode's `permission.task` policy.

### Pydantic AI

Supports tool-based delegation, programmatic hand-off, typed outputs, and
usage accounting. Python can sequence calls and validate worker results rather
than trusting field labels in generated text. Its current docs also describe
subagent and approval capabilities; this ADR does not claim those are absent.
The extra application/integration code does not replace the assignment's
OpenCode agents and exports, so it is deferred for this layer.

## Consequences and failure modes

- Each worker's responsibility and handoff are visible in the tool trace.
- More model calls increase latency and may repeat a shared model error;
  two workers using the same model are not independent statistical witnesses.
- A fluent final answer can conceal missing delegation; inspect calls, not prose.
- Task deny rules remove a denied target from the Task tool description, so a
  compliant primary may never attempt the call. Enforcement evidence therefore
  combines the frozen deny rule, confirmed non-execution (no probe child session
  or marker), and either the absence of an attempt or an attempted call rejected
  by the runtime. A bare textual refusal is insufficient.
- Direct user `@` invocation is a documented separate path; the claim concerns
  the primary's Task calls, not a global ban on users invoking agents.
- Agent-file additions change discovery. Revisit E1 using its frozen baseline
  in a separate checkout/worktree when its Chase returns.

## Verification and decision revision

TP1 must show calculation return before assumptions dispatch, both child
identities, the data handoff, and the correct bounded result. TP2 must show the
registered probe blocked through the primary's Task permission boundary: the
frozen preflight proves the probe exists and the primary's task rules deny it,
and the export proves non-execution. Because OpenCode removes denied targets
from the Task tool description, either no attempt or an attempted runtime
rejection satisfies the observation. A bare textual refusal without that
configuration and non-execution evidence is inconclusive (record TP2
INCONCLUSIVE, not PASS). Missing/unavailable model means ABORT. Keep failed
attempts visible and revise the card with a new GO before any reflight.

Reconsider a code framework if repeat sorties show order violations, if schema
validation becomes necessary, or if resumable multi-stage workflows become a
product requirement. Do not silently loosen permissions to obtain a pass.

## Sources checked — 2026-10-25; permission behavior rechecked 2026-10-29

- [OpenCode agents and task permissions](https://opencode.ai/docs/agents/#task-permissions):
  rule order, denied-target omission, and the direct-user-invocation distinction.
- [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents):
  code edges, routing, orchestrator-workers, and state handoff.
- [Pydantic AI multi-agent applications](https://ai.pydantic.dev/multi-agent-applications/):
  delegation, programmatic hand-off, typed output, and shared usage accounting.

Documentation is design evidence; actual behavior of installed OpenCode remains
unverified until the signed sortie. No completion attestation is supplied here.
