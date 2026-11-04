# E6 design analysis — Context engineering: budget, compaction, handoff, ledger

Date: 2026-11-04. System: Context engineering loop.

## Why (paragraph)

Thursday's lab measured OpenCode's window; E6 measures the system's own loop. By adding a budget meter per model call, a compactor that preserves declared keep-list items, a handoff writer and resume loader, and an append-only ledger recording all four events, the system can resume a fresh session from handoff + L1 files + ledger tail with no transcript and no loss of intent.

## Nine components

| Component | Challenge | E6 design |
|---|---|---|
| Foundation | No visibility into token usage | Budget meter records turn_budget per model call with provider token counts and declared budget |
| Perception | Context grows unbounded | Compactor reduces context while preserving keep-list items word for word |
| Planning and reasoning | Intent lost across sessions | Handoff captures seven sections with explicit next step; resume loads from handoff |
| Tools and orchestration | No continuity mechanism | Handoff writer and resume loader provide session continuity |
| Memory and context | No audit trail | Append-only ledger (var/ledger.jsonl) records all events |
| Coordination | Fresh sessions start empty | Resume loads handoff, L1 files, and ledger tail with no transcript |
| Evaluation and feedback | Can't verify continuity | Tests prove budget tracking, compaction preservation, handoff structure, resume loading |
| Governance and human interface | Truth precedence unclear | README defines Layers of truth (L1/L2/L3) with precedence L2 > L1 > L3 |
| Runtime and operations | Corrections to history | Ledger is append-only; corrections recorded as new events |

## Judgment loop

**Decision:** Implement budget meter, compactor with explicit keep list, handoff/resume with no transcript, append-only ledger as single audit trail.

**Privileged characteristics:** Measurable resource usage, preserved intent through compaction, resumable sessions, auditable event log.

**Cost:** Additional overhead for tracking, compaction logic complexity.

**Failure mode:** Keep list incomplete leads to lost intent; ledger tampering; resume missing critical L1 files.

**Preservation:** Tests verify all requirements; handoff has seven sections with next step 1 as single action; resume uses handoff + L1 files + ledger tail with no transcript; ledger events are append-only.

**Feedback:** Tests and flight evidence confirm fresh session resumes with no loss of intent.
