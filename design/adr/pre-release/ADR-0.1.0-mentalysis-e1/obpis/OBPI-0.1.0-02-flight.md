---
id: OBPI-0.1.0-02-flight
parent: ADR-0.1.0-mentalysis-e1
item: 2
lane: Lite
status: Draft
allowlist:
  - evolution-01/flight-card.md
  - evolution-01/flight-log.md
  - evolution-01/evidence/**
  - design-analyses/E1-react-opencode.md
  - design-analyses/LEDGER.md
  - AI_LOG.md
reqs:
  - REQ-0.1.0-02-01
  - REQ-0.1.0-02-02
  - REQ-0.1.0-02-03
verification:
  - uv run gz validate --documents
  - uv run gz obpi validate --authored design/adr/pre-release/ADR-0.1.0-mentalysis-e1/obpis/OBPI-0.1.0-02-flight.md
---

# OBPI-0.1.0-02-flight: One Chase-reviewed E1 sortie

## ADR Item

Source: `design/adr/pre-release/ADR-0.1.0-mentalysis-e1/ADR-0.1.0-mentalysis-e1.md`, checklist item 2.

## Objective

After preparation review and explicit Chase GO, capture one E1 sortie with exact prompts, actual TP1 arithmetic response, TP2 sequential-read trace, observed stopping reason, and human-reviewed analysis. This authoring session does not execute the sortie.

## Lane

**Lite** - Observation and evidence collection for an educational exercise; no runtime contract change. Human completion attestation is still universal.

## Allowed Paths

- `evolution-01/flight-card.md` — actual Chase decision, reviewer identity, and timestamp when supplied.
- `evolution-01/flight-log.md` — chronological observations and deviations.
- `evolution-01/evidence/**` — raw transcript, configuration snapshot, and evidence index.
- `design-analyses/E1-react-opencode.md` — observed ReAct loop, budget behavior, and limitations.
- `design-analyses/LEDGER.md` — analysis index entry.
- `AI_LOG.md` — accurate flight assistance record.

These paths were green-field at initial discovery and now exist from preparation. Parent ADR Interfaces establishes the layout. The operator authorized conversion-related reference edits on 2026-10-18; read the actual files again before flight, whose scope remains unchanged.

## Denied Paths

- `.opencode/agents/mentalysis.md` — frozen agent definition from preparation.
- `opencode.json` — frozen model, tools, permissions, and step configuration.
- `evolution-01/fixtures/review-queue.md` — immutable synthetic input during flight.
- `docs/PRD.md` — approved requirements, not rewritten to fit results.
- `AGENTS.md` — protected generated contract.
- `.gzkit/ledger.jsonl` — CLI-only writes.
- All other paths, package installs, commits, and pushes are unauthorized for this scoped authoring pass.

## Requirements (FAIL-CLOSED)

1. REQ-0.1.0-02-01: MUST obtain explicit Chase GO before any flight/model invocation; MUST snapshot primary `mentalysis`, `opencode/big-pickle`, `steps: 5`, tools and permissions. NEVER modify configuration during the sortie.
2. REQ-0.1.0-02-02: MUST preserve actual TP1 answer beside expected 1428.57 for next-year FCF 100 / (10% - 3%). MUST preserve TP2 tool arguments and assistant-turn order: offset i, limit 1, next line only next assistant turn, 20-line source. MUST record last line read, remaining work, and actual stopping reason rather than assuming five reads.
3. REQ-0.1.0-02-03: MUST distinguish observed results, expectation, and interpretation in the log and design analysis; NEVER claim unseen lines were reviewed. MUST retain errors/deviations and await human attestation before completion. A failed test point is reported as failed, not silently rerun.

> STOP-on-BLOCKERS: unsigned Chase GO, missing preparation artifacts, unavailable selected model, or changed configuration block execution. Record the blocker; do not substitute another model or extend the budget.

## Discovery Checklist

**Parent ADR (read first; order pinned):**

- [ ] Quote parent ADR Decision item 2 verbatim in Implementation Summary.
- [ ] Read parent ADR Intent and Boundary Invariants.

> **STOP:** If you cannot quote the parent ADR Decision item this brief implements, STOP and re-read before inspecting paths or executing.

**Governance:**

- [ ] Read `AGENTS.md` and `OBPI-0.1.0-01-preparation.md` in this directory.

**Prerequisites:**

- [ ] Inspect `evolution-01/flight-card.md` for actual Chase GO, not a signature template.
- [ ] Inspect `evolution-01/evidence/README.md` for capture procedure and `evolution-01/flight-log.md` for pending/observed separation.
- [ ] Verify the selected model is available without changing provider or permissions.

**Existing Code:**

- [ ] Read `.opencode/agents/mentalysis.md` and `opencode.json` and preserve their preflight configuration snapshot.
- [ ] Read the approved flight prompts and fixture metadata; verify the fixture has 20 physical lines before agent execution.
- [ ] Read `design-analyses/E1-react-opencode.md` to distinguish preflight hypotheses from observed evidence.

## Quality Gates

Gate 1 requires authored lineage. Evidence review must demonstrate the approved prompts and actual stopping behavior; governance validators alone cannot establish behavioral success. Gate 5 requires explicit human review even in Lite lane. Report a failed or blocked flight honestly instead of marking completion.

## Verification

```text
uv run gz validate --documents
uv run gz obpi validate --authored design/adr/pre-release/ADR-0.1.0-mentalysis-e1/obpis/OBPI-0.1.0-02-flight.md
uv run gz validate --req-kind-discipline
```

After the separately authorized sortie, manually compare the raw transcript against the flight card: recompute TP1, enumerate TP2 offset/limit and assistant-turn sequence, identify last observed line and stopping reason, and compare before/after configuration. Record evidence paths and reviewer judgment in the flight log. No command in this specification launches a model.

## Demo

Present Chase with the actual transcript and flight log side by side. Show TP1 expected versus observed value, then the last successful TP2 read and the unreviewed remainder. Show immutable configuration and the actual stop message. Until execution is authorized, this demonstration remains pending.

## Acceptance Criteria

- [ ] REQ-0.1.0-02-01 [SUPPORT]: Flight card records real Chase GO and evidence contains the frozen configuration snapshot; verify chronology manually plus `gz validate --documents` and `obpi_created` lineage.
- [ ] REQ-0.1.0-02-02 [SUPPORT]: Transcript and log record the actual answer, sequential one-line calls, assistant-turn separation, remaining queue, and stopping reason; review raw evidence plus `gz validate --documents` and `obpi_created` lineage.
- [ ] REQ-0.1.0-02-03 [SUPPORT]: Analysis cites actual evidence, identifies deviations and limits of one sortie, and records human review without invented results; verify references plus `gz validate --documents` and `obpi_created` lineage.

## Completion Checklist

- [ ] Chase GO predates flight and exact prompts/configuration are captured.
- [ ] Observations and deviations trace to retained raw evidence.
- [ ] Human explicitly attests after reviewing the outcome; no automatic completion.

## Evidence

### Implementation Summary

Decision quote: "After explicit Chase GO, conduct one reviewed E1 sortie and record actual TP1 and TP2 evidence, stopping behavior, and human review without fabricating completion."

Brief authored 2026-10-18; execution is pending and unauthorized in this pass. No test-point result or flight receipt exists from this authoring session.

### Gate 1 (ADR)

CLI-created replacement brief registered under ADR-0.1.0. Initial governance validation passed eight scopes and fidelity presence, while initial missing-path and Foundation Sunset failures were tracked. Preparation supplied the paths; operator-approved feature conversion replaces the rejected kind. Current check: `uv run gz obpi validate --adr ADR-0.1.0 --authored`; conversion results are recorded in `AI_LOG.md`. These are authoring checks, not flight results.

### Gate 2 (Verification)

Pending actual sortie and transcript review. The expected arithmetic oracle is not an observed model answer.

### Gate 5 (Human)

Chase GO: unsigned. Completion attestation: unsigned. These are separate decisions.

### Blockers and Defects

- Preparation artifacts now exist; selected-model availability and the frozen substrate still need preflight verification.
- Chase GO and human attestation pending; no execution allowed in this pass.
- Initialization reported ruff unavailable and operator handoff reports `gh` unavailable; no lint success or filed issue is claimed.
- Generated governance links refer to unshipped upstream docs, including `docs/governance/agent-contract-rationale.md` and `docs/governance/GovZero/obpi-decomposition-matrix.md`; retain this defect for review.
- Exact harness step/read relationship is unverified. Capture it as an observation, not a claim that five steps guarantees five reads.
- The Foundation Sunset failure prompted the approved feature conversion; no grandfather registry edits were made. See `AI_LOG.md` for current taxonomy results.
- The original missing-path blocker was resolved by actual preparation files, not by changing this flight brief's scope.

### Value Narrative

Before: a reviewed plan cannot establish behavior. Yield after execution: one bounded evidence package documenting both a calculation and honestly unfinished work.

### Key Proof

Pending raw transcript with TP1 answer and TP2 terminal read/stop; no synthetic success record is acceptable.

## Human Attestation

- Attestor: unsigned
- Attestation: pending explicit human review
- Date: unsigned
