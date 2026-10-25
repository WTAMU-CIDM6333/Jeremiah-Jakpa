# E1 — Sortie 1 flight log

Status: NOT FLOWN. No verdict has been earned. No test entries or session exports
exist yet. This is a recording template, not evidence of a flight.

## Administrative deferral — 2026-10-25 (not a flight event)

The operator reports that the Chase partner is unavailable. Chase review, GO,
the E1 sortie, and evidence review are deferred and will be revisited when the
partner becomes available. No test point has run; no PASS, FAIL, or runtime
ABORT is claimed. The existing unsigned GO requirement remains in force.

The operator requested proceeding with E2 preparation while this dependency is
pending. This is a recorded sequencing deviation from the assignment's in-order
review cycle, not evidence that E1 is complete or an instructor-approved waiver.
Before returning to E1, review the frozen preparation baseline, obtain the
Chase's committed GO, and then run the two original test points in fresh sessions.

## Preflight record (complete only after committed Chase GO)

- Pilot / Chase / UTC start time: pending.
- Preparation SHA / card-freeze SHA / GO SHA / actual flight SHA: pending.
- OpenCode version / model / effective steps: pending observation.
- Clean worktree and frozen configuration confirmation: pending observation.

## Test-point observations

| Test | Session / timestamps | Sanitized export / SHA-256 | Iterations / tool calls / terminal record | Observation / verdict |
| --- | --- | --- | --- | --- |
| TP1 | Not run | Not generated | Not observed | Pending |
| TP2 | Not run | Not generated | Not observed | Pending |

After flight, report the runtime's iteration-count convention, exact record IDs,
and whether TP2 actually reached the configured boundary. Quote any error text
and identify remaining review items. Keep retries visible.

## Sortie verdict

Pending flight — replace with PASS, FAIL, or ABORT based on evidence and every
pre-registered falsifier. Lack of a flight is not an observed runtime ABORT.

## Chase evidence review

Unsigned — after reviewing only the evidence, Chase appends:
`CHASE — <name> — <date> — PASS or FAIL — <falsifier quoted>`.
