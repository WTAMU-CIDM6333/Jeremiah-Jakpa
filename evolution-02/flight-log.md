# E2 — Sortie 2 flight log

Status: NOT FLOWN. Preparation frozen for Chase review; no runtime verdict earned.
Administrative note, 2026-10-25: Chase unavailable; GO and flight await review.

## Preparation freeze — 2026-10-29 (not a flight event)

Preparation was frozen for Chase review. No model sortie ran; no PASS, FAIL, or
runtime ABORT is claimed.

- OpenCode `1.18.21`; `opencode/big-pickle` listed on 2026-10-29; availability
  during flight remains untested.
- Resolved with `opencode debug agent`: primary `mentalysis-e2` is
  `mode: primary`, steps 5, `permission.task` wildcard deny then exact allows for
  `mentalysis-calculation` and `mentalysis-assumptions`; workers are subagents,
  steps 3, edit/bash/task denied; probe is a subagent, steps 1, edit/bash/task
  denied.
- `opencode debug config`: default agent `mentalysis`, sharing disabled, no
  configured plugins or MCP servers, no top-level permission override.
- Host: Windows 11 `10.0.26200`, PowerShell `5.1.26100.9711`, Git
  `2.52.0.windows.1`, gzkit `0.34.7`, uv `0.12.17`.
- Validation: nine governance scopes, fidelity-presence, and both authored
  briefs passed. These checks prove document structure and resolved
  configuration, not runtime behavior.
- Preparation commit: `d429e179154db0b8ab8a6cb7594646594121d0cb`; its
  artifact-edit ledger events were committed in `681f88b`. This card-freeze
  commit follows both and is the baseline Chase reviews.

## Preflight record (after committed GO)

- Pilot / Chase / UTC start: pending.
- Preparation / card-freeze / GO / actual flight commit: pending.
- OpenCode version / effective primary and worker models / budgets: pending.
- Frozen permission/tool snapshot and clean-worktree observation: pending.

## Test-point observations

| Test | Parent/child sessions and timestamps | Evidence and SHA-256 | Actual Task records/order/status | Verdict |
| --- | --- | --- | --- | --- |
| TP1 ordered calculation and assumptions | Not run | Not generated | Not observed | Pending |
| TP2 denied probe | Not run | Not generated | Not observed | Pending |

For TP1 cite both worker dispatch/return records and the calculation-result
handoff to assumptions. For TP2 record the frozen deny rule, whether any probe
Task call was attempted, any rejection record, the absence of a probe child
session, and the absence/presence of the `E2_DENIED_DELEGATE_EXECUTED` marker.
A non-attempt passes only with the frozen deny rule and confirmed non-execution;
a bare refusal or a target-not-found error alone is inconclusive. Record
parent/child iterations separately, deviations, and retries.

## Sortie verdict

Pending flight. Enter PASS, FAIL, or ABORT only from actual evidence. Individual
test points may be recorded as PASS, FAIL, or INCONCLUSIVE; any non-PASS test
point prevents a sortie PASS. A correct numerical answer alone does not prove the
pattern or its task permission gate.

## Chase evidence review

Unsigned. After reviewing evidence, append:
`CHASE — <name> — <date> — PASS or FAIL — <falsifier quoted>`.
