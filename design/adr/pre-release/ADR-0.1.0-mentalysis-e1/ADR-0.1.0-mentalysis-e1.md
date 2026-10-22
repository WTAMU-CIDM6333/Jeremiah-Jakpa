---
id: ADR-0.1.0-mentalysis-e1
status: Draft
kind: feature
semver: 0.1.0
lane: lite
parent: PRD-MENTALYSIS-1.0.0
date: 2026-10-18
---

# ADR-0.1.0-mentalysis-e1: Mentalysis E1 Educational DCF

## Persona

Main-session: craftsperson, governance-aware, whole-file-reasoning, direct. Preserve the distinction between planned, observed, and human-attested evidence.

## Why feature tier?

This release carries the named E1 educational DCF exercise and its preparation/flight package. The operator explicitly approved conversion to feature 0.1.0 with "go ahead and make the conversion" after the installed Foundation Sunset validator rejected the original kind. Educational and evidence-honesty constraints remain intact; kind changes do not authorize flight or completion.

## Conversion Lineage

The CLI demoted the original foundation into `ADR-pool.mentalysis-e1-foundation` and parked its historical briefs. This replacement feature was then created and registered through `gz plan create`, avoiding promotion's automatic unpark of obsolete brief IDs. The pool record links the replacement. No completion or supersession attestation was emitted; original ledger events remain unchanged. Active brief and REQ identifiers use 0.1.0.

## Intent

Establish Mentalysis as an educational DCF agent and make the five-step stopping boundary observable. The approved exercise pairs a small synthetic calculation with an intentionally unfinished document review. No flight evidence exists yet. Preparation must be reviewable without implying permission to fly.

## Decision

1. Prepare the Mentalysis E1 requirements, primary-agent configuration, design analysis, and unsigned flight package under the approved five-step contract.
2. After explicit Chase GO, conduct one reviewed E1 sortie and record actual TP1 and TP2 evidence, stopping behavior, and human review without fabricating completion.

Primary agent: `mentalysis`; model: `opencode/big-pickle`; `steps: 5`. TP1 asks Gordon-growth terminal value for next-year FCF 100, WACC 10%, g 3%; expected answer 1428.57 in the input units. TP2 reads a synthetic 20-line queue with offset i, limit 1, requesting the next line only in the next assistant turn. The budget deliberately leaves work unfinished. Tool calls are not assumed to equal harness steps. Tools and permissions stay fixed during the sortie.

## Boundary Invariants

- Preparation does not authorize flight; Chase GO and human completion attestation are distinct and unsigned until supplied.
- Synthetic educational analysis excludes real investment advice and live financial data.
- Evidence preserves original observations, failures, and unfinished work; expectations never substitute for measurements.
- Preparation owns the reviewable package; flight owns observed evidence. Configuration is frozen during flight.

## Interfaces

The operator approved this green-field layout: `.opencode/agents/mentalysis.md`, `opencode.json`, `docs/PRD.md`, `evolution-01/flight-card.md`, `evolution-01/flight-log.md` (pending template), `evolution-01/README.md`, `evolution-01/fixtures/review-queue.md`, `evolution-01/evidence/README.md`, `design-analyses/E1-react-opencode.md`, `design-analyses/LEDGER.md`, `AI_LOG.md`, and `README.md`. The parent session authors those preparation files. Flight later populates logs, evidence, and analysis with observations. Governance authoring owns this ADR package and `design/prd/PRD-MENTALYSIS-1.0.0.md`; CLI commands own ledger writes. Root AGENTS.md is not edited.

## Consequences

### Positive

The two briefs establish an explicit review boundary. Two test points distinguish financial reasoning from bounded tool use using a reproducible arithmetic oracle.

### Negative

The small budget prevents complete document review. Human review and tooling blockers can delay completion. One sortie is illustrative evidence, not statistical reliability measurement.

## Fidelity Assertions

These prove governance readiness only; flight behavior requires transcript review.

| Claim | Command | Expected exit |
|-------|---------|---------------|
| The two-unit decomposition is coherent. | uv run gz validate --decomposition | 0 |
| Both briefs carry authored execution boundaries. | uv run gz obpi validate --adr ADR-0.1.0 --authored | 0 |

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

The two-unit baseline separates the approval-state anchor and evidence surface. Preparation has one narrative (reviewable package); flight has one narrative (observed sortie). Each is independently verifiable. This planning package introduces no new runtime implementation or dependency, so lane is lite; a changed external runtime contract requires lane reassessment.

## Checklist

- [ ] OBPI-0.1.0-01: Prepare the approved Mentalysis E1 package with unsigned review fields.
- [ ] OBPI-0.1.0-02: Conduct and document one Chase-reviewed sortie after explicit GO.

## OBPI Decomposition

| # | OBPI | Specification Summary | Lane | Status |
|---|------|-----------------------|------|--------|
| 1 | OBPI-0.1.0-01-preparation | Prepare the approved Mentalysis E1 package with unsigned review fields. | Lite | Draft |
| 2 | OBPI-0.1.0-02-flight | Conduct and document one Chase-reviewed sortie after explicit GO. | Lite | Draft |

## Q&A Transcript

Operator context: initialization and E1 scope approved; the original foundation choice was subsequently replaced by explicit approval of feature 0.1.0: "go ahead and make the conversion". The two-brief boundary is unchanged. Human attestation and Chase GO remain pending. This pass authorizes no flight, model calls, commits, pushes, or installations.

## Evidence

Governance PRD: `design/prd/PRD-MENTALYSIS-1.0.0.md`; canonical product PRD: parent-authored `docs/PRD.md`. Interface paths are evidence destinations, not execution proof. Blockers are tracked in the briefs.

## Alternatives Considered

The closest alternative was one combined brief, rejected because it erases the preparation/flight review boundary. Live-market valuation introduces uncontrolled inputs. Increasing steps to finish the queue defeats the approved unfinished-work observation.

## Forcing Functions

### Pre-Mortem

A pending template is mistaken for successful flight evidence. Separate briefs, unsigned fields, and raw transcript inspection prevent preparation from proving flight completion.

### What Would Have to Be True

The model must be available and the harness must honor the budget. Both remain unverified until reviewed execution; exact stopping semantics are the weakest assumption.

### Constraint Archaeology

The model, five steps, synthetic inputs, and two briefs are approved constraints. Upstream documentation references are inherited scaffold links, not proof that the documents ship locally.

### Assumption Surfacing

Five steps need not mean five successful reads. Preserve early stops and unexpected behavior instead of silently changing configuration.

### The 2am Operator Question

Retain exact prompts, configuration snapshot, transcript, stopping reason, and last observed line so reviewers can reconstruct execution.

### Reversibility

Preparation documents are reversible. Flight evidence is historical and requires additive correction rather than rewriting to match expectations.

### Scope Minimization

One arithmetic question and one fixed queue suffice. Additional models, live sources, UI work, and repeat sorties require new approved scope.

### Downstream Decisions Forced

Chase decides GO before execution; a human reviews evidence before completion. Later runtime changes require a new contract/lane assessment.

## Attestation Block

| Term | Status | Attested By | Date | Reason |
|------|--------|-------------|------|--------|
| 0.1.0 | Pending | | | |
