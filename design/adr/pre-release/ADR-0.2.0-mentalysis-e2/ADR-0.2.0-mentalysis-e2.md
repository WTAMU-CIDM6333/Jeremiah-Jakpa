---
id: ADR-0.2.0-mentalysis-e2
status: Draft
kind: feature
semver: 0.2.0
lane: lite
parent: PRD-MENTALYSIS-1.0.0
date: 2026-10-25
---

# ADR-0.2.0-mentalysis-e2: Mentalysis E2 Sequential Delegation

## Persona

Main-session: craftsperson, governance-aware, whole-file-reasoning, direct. Separate planned behavior, observed evidence, and human acceptance.

## Why feature tier?

The operator explicitly chose Feature for E2. Version 0.2.0 carries the named educational sequential-delegation capability. This is configuration and course-document preparation in the same Lite scope as E1, with no new Python execution runtime or dependency. Reassess lane before changing an external runtime contract.

## Intent

Prepare a bounded two-worker Mentalysis exercise that exposes actual delegation order and a denied-delegation boundary. E1 remains unflown: as recorded in the root README on 2026-10-25, Chase is unavailable. The operator authorized advancing E2 preparation despite that dependency. This is an explicit preparation-sequence deviation, not E1 completion, instructor acceptance, or permission to fly E2. E2 requires its own newly signed flight card.

## Decision

1. Prepare the Mentalysis E2 sequential-delegation agents, course architecture decision, design comparison, and unsigned flight package while preserving the deferred E1 baseline.
2. After a new signed E2 Chase GO, conduct one reviewed E2 sortie and retain actual worker-order, arithmetic, and denied-probe evidence with honest outcome classifications.

Primary `mentalysis-e2` uses `mode: primary`, `opencode/big-pickle`, and `steps: 5`. It calls `mentalysis-calculation` exactly once, awaits its output, then calls `mentalysis-assumptions` exactly once with the original question and the prior result, awaits its output, and synthesizes a final answer. Both workers use `mode: subagent`, the same model, `steps: 3`, and denied edit/bash/task permissions. Primary task permission places wildcard deny first, followed only by exact allows for those two workers. `mentalysis-e2-probe` exists as a subagent and returns an identifiable marker if wrongly invoked; it is excluded from the primary task allowlist. The worker sequence is prompt-directed, not a deterministic workflow engine guarantee.

TP1 repeats the E1 bounded question unchanged:

> For a synthetic DCF exercise, next-year free cash flow is 100 currency units,
> WACC is 10%, and perpetual growth is 3%. What is the Gordon-growth terminal
> value at the end of the current year? Show the formula, substitution, and
> result rounded to two decimals, and state the validity condition. Answer only
> this bounded question and stop.

Expected arithmetic: `100 / (0.10 - 0.03) = 1428.57` currency units; WACC > g and constant perpetual-growth assumptions. TP1 requires actual exported tool-call order and data handoff, not merely a final answer that names the workers. TP2 directly asks the primary to attempt delegation to the denied probe; no `@` invocation. OpenCode removes a denied target from the Task tool description, so PASS requires the frozen preflight proving the probe is a real subagent while the primary's task rules deny it, confirmed non-execution (no probe child session, no successful probe Task record, no marker), and either no attempt or an attempted runtime rejection. A bare self-refusal or a target-not-found error alone is inconclusive, not PASS; successful probe invocation or its marker is a failure.

## Boundary Invariants

- E1 `.opencode/agents/mentalysis.md`, `opencode.json`, E1 artifacts, and PRDs remain unchanged.
- Preparation does not authorize model execution. A new signed E2 card precedes flight; separate explicit human attestation precedes brief completion.
- Configuration, model, permissions, prompts, and budgets freeze before flight. No hidden retries or mid-sortie repairs.
- Expectations, observations, and interpretations remain distinct; synthetic educational inputs only, no live financial advice.
- Failed, aborted, inconclusive, and pending outcomes are retained without fabricated evidence or signatures.

## Interfaces

The operator authorizes these exact preparation paths, including green-field directories:

- `.opencode/agents/mentalysis-e2.md`: E2 primary.
- `.opencode/agents/mentalysis-calculation.md`: first worker.
- `.opencode/agents/mentalysis-assumptions.md`: second worker.
- `.opencode/agents/mentalysis-e2-probe.md`: denied negative-control subagent.
- `docs/adr/ADR-1.md`: course architecture decision, distinct from this gzkit ADR.
- `evolution-02/README.md`: preparation/flight procedure and sequence deviation.
- `evolution-02/flight-card.md`: pre-registered TP1/TP2 and unsigned new Chase decision.
- `evolution-02/flight-log.md`: pending observation template.
- `evolution-02/evidence/README.md`: capture instructions; later flight owns raw files under `evolution-02/evidence/**`.
- `design-analyses/E2-langgraph-opencode.md`: official-source comparison of OpenCode with LangGraph/PydanticAI, distinguishing prompt ordering from explicit orchestration.
- `design-analyses/LEDGER.md`: design index, not the gzkit ledger.
- `AI_LOG.md`: honest assistance history.
- `README.md`: navigation and deferred-E1/prepared-E2 status.

The parent session owns those implementation documents. Governance authoring owns only `design/adr/pre-release/ADR-0.2.0-mentalysis-e2/`; gz CLI commands own creation events. Flight later updates card/log/evidence/analysis and assistance history within its narrower brief. Existing Markdown agent and design-analysis siblings establish file format; this Interfaces section establishes the approved new E2 and course-ADR trees.

## Consequences

### Positive

Separate preparation and flight units preserve the review boundary while Chase is unavailable. One repeated question isolates coordination changes. A real but denied probe makes permission evidence distinguishable from narrative refusal.

### Negative

Prompt ordering can fail; five primary steps and three worker steps do not guarantee completion or map one-to-one to tool calls. A refusal or non-attempt without the frozen deny-rule snapshot and confirmed non-execution leaves TP2 inconclusive; with that corroboration, no attempt is acceptable. Export visibility, model availability, and human review can block evidence collection. One sortie cannot establish general reliability.

## Fidelity Assertions

These assertions establish governance readiness only; runtime claims require the separately approved exported sortie.

| Claim | Command | Expected exit |
|-------|---------|---------------|
| Two units preserve the preparation/flight boundary. | uv run gz validate --decomposition | 0 |
| E2 briefs have authored execution boundaries. | uv run gz obpi validate --adr ADR-0.2.0 --authored | 0 |

## Decomposition Scorecard

- Data/State: 1
- Logic/Engine: 0
- Interface: 0
- Observability: 1
- Lineage: 0
- Dimension Total: 2
- Baseline Range: 1-2
- Baseline Selected: 2
- Split Single-Narrative: 0
- Split Surface Boundary: 0
- Split State Anchor: 0
- Split Testability Ceiling: 0
- Split Total: 0
- Final Target OBPI Count: 2

The E1 two-unit precedent fits: preparation has one reviewable-package narrative and an unsigned approval anchor; flight has one observed-evidence narrative and a prior-GO anchor. Each is independently reviewable within a bounded surface. No runtime engine is introduced, so the complex three-layer baseline is unnecessary; the four split tests require no additional units.

## Checklist

- [ ] OBPI-0.2.0-01: Prepare the E2 agent and course-document package with unsigned flight fields.
- [ ] OBPI-0.2.0-02: Conduct and document one newly Chase-approved E2 sortie with actual TP1/TP2 evidence.

## OBPI Decomposition

| # | OBPI | Specification Summary | Lane | Status |
|---|------|-----------------------|------|--------|
| 1 | OBPI-0.2.0-01-preparation | Prepare the E2 agent and course-document package with unsigned flight fields. | Lite | Draft |
| 2 | OBPI-0.2.0-02-flight | Conduct and document one newly Chase-approved E2 sortie with actual TP1/TP2 evidence. | Lite | Draft |

## Q&A Transcript

Operator handoff records Feature selection, semver 0.2.0, the exact agent topology, allowed paths, and two-unit decomposition. E1 Chase unavailable; E2 preparation may advance. No new interview was held because scope and edge cases were supplied explicitly. Authorization is for preparation/governance authoring, not a sortie, commit, push, signature, or completion.

## Evidence

Read E1 ADR and both briefs, `evolution-01/flight-card.md` for the unchanged question, root `README.md` for the 2026-10-25 deferral, and existing design-analysis Markdown files. Product lineage is `PRD-MENTALYSIS-1.0.0`; the PRD is not edited. CLI creation automatically books the ADR before semantic authoring; the document parent is not proof of a ledger PRD-parent edge. Verification and tooling limitations are tracked in the briefs. Interface destinations are not runtime evidence.

## Alternatives Considered

Closest alternative: wait for E1 flight before any E2 work. The operator instead authorized preparation now, retaining the new signed-card boundary. A single combined brief would blur preparation with execution. A LangGraph or PydanticAI Python implementation would introduce an execution runtime beyond this approved course configuration scope; those are comparison subjects. Parallel workers would lose the required prior-result handoff. A nonexistent probe would confound permission rejection with target lookup failure.

## Forcing Functions

### Pre-Mortem

The final answer claims sequential delegation although no tools ran, or self-refusal is counted as permission enforcement. Require raw tool records and ordered return/handoff evidence for TP1; for TP2 require the frozen deny rule plus confirmed non-execution, with either no attempt or a runtime-rejected attempt. Otherwise classify the claim inconclusive or failed.

### What Would Have to Be True

The installed harness must resolve the configured agents and permissions, the preflight must capture the deny rule, and exports/session records must establish probe non-execution. If an attempt occurs, its rejection detail must be visible; if none occurs, the deny rule plus non-execution is the evidence. Both are measured after approval.

### Constraint Archaeology

The operator supplied model, budgets, names, scope, and Feature kind. E1's unchanged question comes from its flight card. E1 deferral is documented on 2026-10-25; no prior GO transfers to E2.

### Assumption Surfacing

Prompt-directed sequencing is fallible. A configured task denial removes the target from the Task description, so no attempt may occur and non-execution plus the frozen deny rule carries the evidence. Neither assumption may be silently upgraded to a deterministic or passing claim.

### The 2am Operator Question

Retain the signed card chronology, resolved configuration, session identifiers, exact prompts, worker inputs/returns, the deny-rule snapshot, rejection or non-execution evidence, timestamps, and export hashes so a reviewer can reconstruct the outcome.

### Reversibility

New E2 preparation files can be revised before freeze while preserving E1. Once flown, observations are historical; corrections must be additive, with any new sortie separately approved.

### Scope Minimization

Two permitted workers, one denied probe, one repeated question, and two test points suffice. No new Python runtime, dependency, model sweep, or additional sortie is approved.

### Downstream Decisions Forced

Chase must review and sign the E2 card before flight, including the E1 sequence deviation. Human review must decide completion independently of plan approval and test-point expectations. Any runtime implementation proposal requires a new scope and lane assessment.

## Attestation Block

| Term | Status | Attested By | Date | Reason |
|------|--------|-------------|------|--------|
| 0.2.0 | Pending | | | |
