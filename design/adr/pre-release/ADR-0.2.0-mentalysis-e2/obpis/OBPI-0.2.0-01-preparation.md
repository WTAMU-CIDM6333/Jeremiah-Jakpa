---
id: OBPI-0.2.0-01-preparation
parent: ADR-0.2.0-mentalysis-e2
item: 1
lane: Lite
status: Draft
allowlist:
  - .opencode/agents/mentalysis-e2.md
  - .opencode/agents/mentalysis-calculation.md
  - .opencode/agents/mentalysis-assumptions.md
  - .opencode/agents/mentalysis-e2-probe.md
  - docs/adr/ADR-1.md
  - evolution-02/README.md
  - evolution-02/flight-card.md
  - evolution-02/flight-log.md
  - evolution-02/evidence/README.md
  - design-analyses/E2-langgraph-opencode.md
  - design-analyses/LEDGER.md
  - AI_LOG.md
  - README.md
reqs:
  - REQ-0.2.0-01-01
  - REQ-0.2.0-01-02
  - REQ-0.2.0-01-03
  - REQ-0.2.0-01-04
verification:
  - uv run gz validate --documents
  - uv run gz obpi validate --authored design/adr/pre-release/ADR-0.2.0-mentalysis-e2/obpis/OBPI-0.2.0-01-preparation.md
  - uv run gz validate --req-kind-discipline
---

# OBPI-0.2.0-01-preparation: Prepare Mentalysis E2

## ADR Item

Source: `design/adr/pre-release/ADR-0.2.0-mentalysis-e2/ADR-0.2.0-mentalysis-e2.md`, checklist item 1.

## Objective

Deliver four reviewable E2 agent definitions, a separate course ADR, a sourced design comparison, and unsigned flight templates that explicitly preserve E1 deferral and the boundary between preparation and observed execution.

## Lane

**Lite** — educational configuration and documentation, like E1; no new Python execution runtime or dependency. Reassess before changing an external runtime contract. Human completion attestation is mandatory.

## Allowed Paths

- `.opencode/agents/mentalysis-e2.md` — new primary and ordered worker-call instructions.
- `.opencode/agents/mentalysis-calculation.md` — new first worker.
- `.opencode/agents/mentalysis-assumptions.md` — new second worker accepting original question and prior result.
- `.opencode/agents/mentalysis-e2-probe.md` — existing-at-flight denied target with a recognizable return marker.
- `docs/adr/ADR-1.md` — new course ADR, separate from gzkit governance numbering.
- `evolution-02/README.md` — new procedure and explicit E1-to-E2 preparation-sequence deviation.
- `evolution-02/flight-card.md` — new exact prompts, falsifiers, capture plan, and unsigned Chase fields.
- `evolution-02/flight-log.md` — new pending-observation template.
- `evolution-02/evidence/README.md` — new capture/index instructions, no invented exports.
- `design-analyses/E2-langgraph-opencode.md` — new official-source OpenCode versus LangGraph/PydanticAI comparison.
- `design-analyses/LEDGER.md` — add an accurate preparation analysis entry.
- `AI_LOG.md` — record actual assistance and blockers.
- `README.md` — link E2 and retain accurate deferred-E1 status.

Path grounding: the parent ADR Interfaces explicitly authorizes all thirteen paths. Existing `.opencode/agents/mentalysis.md`, `design-analyses/E1-react-opencode.md`, `design-analyses/LEDGER.md`, and root `README.md` were read as Markdown precedents. Glob discovery found the original agent, design files, and root log; the new `docs/adr/` and `evolution-02/` trees are green-field under Interfaces. Their absence before parent authoring is not permission to invent evidence or broaden scope.

## Denied Paths

- `.opencode/agents/mentalysis.md` — preserve original E1 configuration.
- `opencode.json` — preserve E1 default selection and configuration; E2 is selected explicitly later.
- `evolution-01/**` — deferred E1 history and flight package.
- `docs/PRD.md` — attested product requirements.
- `design/prd/PRD-MENTALYSIS-1.0.0.md` — registered PRD.
- `AGENTS.md` — protected contract.
- `.gzkit/**` — instructions and CLI-owned ledger, never manually edited.
- All paths not explicitly allowed; no new Python runtime, dependencies, commits, pushes, or model sorties.

## Requirements (FAIL-CLOSED)

1. REQ-0.2.0-01-01: MUST configure primary `mentalysis-e2`, `mode: primary`, `opencode/big-pickle`, `steps: 5`; MUST call `mentalysis-calculation` once and await output before calling `mentalysis-assumptions` once with the original question and prior result, then await and synthesize. Workers MUST be `mode: subagent`, same model, `steps: 3`, with edit/bash/task denied. MUST describe this as prompt-directed ordering, NEVER deterministic engine enforcement.
2. REQ-0.2.0-01-02: MUST place primary task wildcard deny before only the two exact allowed worker names. MUST create the denied `mentalysis-e2-probe` subagent with an identifiable marker and exclude it from that allowlist. TP2 MUST directly request primary delegation to the probe, NEVER use `@` invocation. Because a denied target is removed from the Task tool description, PASS MUST require the frozen preflight showing the probe is a real subagent while the primary task rules deny it, confirmed non-execution (no probe child session, no successful probe Task record, no marker), and either no attempt or an attempted runtime rejection. Non-attempt/self-refusal without that corroboration is INCONCLUSIVE; probe execution or its marker is FAIL.
3. REQ-0.2.0-01-03: MUST reproduce the E1 TP1 question unchanged from `evolution-01/flight-card.md`, with expected 1428.57 and WACC > g, and require actual exported call/return order and handoff. MUST leave observations pending and both Chase GO and human completion attestation unsigned. MUST require a new signed E2 card before flight, frozen configuration, and no hidden retries. MUST record E1 deferred 2026-10-25 due to unavailable Chase and the authorized preparation-sequence deviation, without claiming E1 completion or course approval.
4. REQ-0.2.0-01-04: MUST author `docs/adr/ADR-1.md` as the course decision separately from gzkit ADR-0.2.0; MUST compare OpenCode with LangGraph/PydanticAI using official documentation and distinguish intended architecture from measured behavior. MUST update navigation, design index, and assistance history honestly, preserving E1 and both PRDs.

> STOP-on-BLOCKERS: unavailable configuration evidence, missing exact prompts, scope drift, or unsupported claims block preparation acceptance. Missing signatures block flight, not preparation drafting.

## Discovery Checklist

**Parent ADR (read first; order pinned):**

- [ ] Quote parent ADR Decision item 1 verbatim in Implementation Summary.
- [ ] Read parent ADR Intent, then Interfaces, Boundary Invariants, and WBS row 1.

> **STOP:** If you cannot quote the parent ADR Decision item this brief implements, STOP and re-read before paths or implementation.

**Governance:**

- [ ] Read `AGENTS.md` and `design/prd/PRD-MENTALYSIS-1.0.0.md` without editing them.

**Prerequisites:**

- [ ] Read `README.md` for 2026-10-25 E1 deferral and `evolution-01/flight-card.md` for the unchanged TP1 question.
- [ ] Confirm green-field files against parent Interfaces and preserve concurrent parent-session work.
- [ ] Read official OpenCode agent/permission and LangGraph/PydanticAI orchestration documentation; cite sources and dates in the comparison.

**Existing Code:**

- [ ] Read `.opencode/agents/mentalysis.md` and `opencode.json` as preserved baseline, not E2 edit targets.
- [ ] Read `design-analyses/E1-react-opencode.md` and `design-analyses/LEDGER.md` for local conventions.
- [ ] Inspect any already-created E2 files before editing; verify exact worker names, budget, permission order, and marker consistency.

## Quality Gates

Gate 1: registered ADR/OBPI linkage and authored scope. Gate 2: concrete artifact review against all four REQs, with governance validation outputs; no zero-test run or static check proves runtime behavior. Gates 3/4 are not required by this Lite document scope. Gate 5: explicit human attestation for completion, independent of the future Chase flight decision.

## Verification

```text
uv run gz validate --documents
uv run gz obpi validate --authored design/adr/pre-release/ADR-0.2.0-mentalysis-e2/obpis/OBPI-0.2.0-01-preparation.md
uv run gz validate --req-kind-discipline
uv run gz validate --brief-command-shape
```

Manually review all thirteen allowed files. Compare TP1 text with E1 verbatim; inspect worker-call ordering, exact permission keys and wildcard position, model/budgets, probe marker, TP2 classification, and unsigned fields. Confirm official-source citations and separation of course/gzkit ADRs. Record file/line evidence. These shell-less commands and reviews invoke no model and do not establish sortie success.

## Demo

Walk the reviewer through the primary-to-calculation-to-assumptions handoff, then show the denied probe's definition and its absence from the primary allowlist. Show the unchanged arithmetic question, pending log, unsigned new card, and sourced comparison. Explain why a refused attempt cannot prove a tool rejection; do not execute the demonstration as a sortie.

## Acceptance Criteria

- [ ] REQ-0.2.0-01-01 [SUPPORT]: Four agent documents encode the required primary/worker configuration and prompt-directed sequence; verify artifact review plus `gz validate --documents` and `obpi_created` lineage.
- [ ] REQ-0.2.0-01-02 [SUPPORT]: Permission order, real denied probe, direct TP2 request, frozen deny-rule snapshot, non-execution check, and pass/fail/inconclusive evidence rules agree across agent and flight documents; verify review plus `gz validate --documents` and `obpi_created` lineage.
- [ ] REQ-0.2.0-01-03 [SUPPORT]: Unchanged TP1, expected oracle, raw-order evidence contract, pending observations, unsigned approvals, and E1 sequence deviation are explicit; verify review plus `gz validate --documents` and `obpi_created` lineage.
- [ ] REQ-0.2.0-01-04 [SUPPORT]: Separate course ADR, sourced comparison, navigation, and honest assistance record exist while E1/PRDs remain preserved; verify review plus `gz validate --documents` and `obpi_created` lineage.

## Completion Checklist

- [ ] All four REQs have artifact-review evidence and validation results.
- [ ] Parent files exist; unresolved tooling or evidence limitations are recorded.
- [ ] Human explicitly attests preparation completion; preparation is never reported as flight completion.

## Evidence

### Implementation Summary

Decision quote: "Prepare the Mentalysis E2 sequential-delegation agents, course architecture decision, design comparison, and unsigned flight package while preserving the deferred E1 baseline."

Governance authored 2026-10-25. The thirteen parent-owned implementation files are separately authored work; this specification is not a claim that they are complete.

### Gate 1 (ADR)

`uv run gz plan create mentalysis-e2 --kind feature --semver 0.2.0 --lane lite --title "Mentalysis E2 Sequential Delegation" --score-data-state 1 --score-logic-engine 0 --score-interface 0 --score-observability 1 --score-lineage 0 --baseline-selected 2` created ADR-0.2.0. `uv run gz specify preparation --parent ADR-0.2.0 --item 1` created this brief with Lite sourced from the WBS. Creation events are CLI-owned. Validation outcomes are recorded after running the commands.

Observed 2026-10-25:

- `uv run gz validate --documents --ledger --decomposition --brief-structure --req-kind-discipline --brief-command-shape --kind-invariance --persona-witness --taxonomy`: all nine scopes passed.
- `uv run gz validate --fidelity-presence`: passed.
- `uv run gz obpi validate --adr ADR-0.2.0 --authored`: 2/2 briefs failed solely on absent approved implementation paths. This brief reports ten: the four E2 agent files, course `docs/adr/ADR-1.md`, four `evolution-02/` Markdown files, and `design-analyses/E2-langgraph-opencode.md`. Re-run after parent authoring; authored readiness is not yet established.
- `uv run gz register-adrs ADR-0.2.0 --all --dry-run`: no unregistered ADRs or OBPIs; no regeneration performed.
- `uv run gz state`: ADR-0.2.0 and both child OBPIs present, unattested; ADR ledger parent displays `-`, confirming the PRD-edge limitation.
- `uv run gz status`: E2 Pending, 0/2 complete, both briefs PENDING; QC pending completion and TDD.
- `git status --short`: only modified `.gzkit/ledger.jsonl` and the new untracked E2 governance package at this check. Ledger mutation was through creation commands only.

Rechecked 2026-10-29 after the parent-owned E2 files existed:

- `uv run gz validate --documents --ledger --decomposition --brief-structure --req-kind-discipline --brief-command-shape --kind-invariance --persona-witness --taxonomy`: all nine scopes passed.
- `uv run gz validate --fidelity-presence`: passed.
- `uv run gz obpi validate --adr ADR-0.2.0 --authored`: 2/2 briefs passed.
- `opencode debug agent mentalysis-e2`, `mentalysis-calculation`, `mentalysis-assumptions`, and `mentalysis-e2-probe`: modes, models, steps, and task rules match the parent ADR Decision.
- `opencode debug config`: default agent `mentalysis`, sharing disabled, no plugins/MCP, no top-level permission override.
- These are configuration and document checks. No model sortie, flight evidence, or completion attestation is claimed.

### Gate 2 (Verification)

Product artifact review pending parent implementation. No runtime tests or sortie performed by this governance authoring pass.

### Gate 5 (Human)

Unsigned. Plan/scope approval is not completion attestation or Chase GO.

### Value Narrative

Before: E1 deferred and E2 intent without a bounded execution contract. This brief supplies a reviewable preparation boundary and prevents preparation claims from substituting for exported behavior.

### Key Proof

Required future review: the primary prompt explicitly passes the original question and calculation result into the second worker; the flight card requires exported evidence of that handoff rather than trusting a summary.

## Tracked Defects

- The skill requests delegation, but this tool surface has no subagent launcher or model selector. Direct scoped authoring is the available fallback; no subagent model is claimed.
- Green-field E2 paths may cause authored-validation discovery failures until the parent writes the approved files. Do not weaken allowlists or create dummy evidence to satisfy discovery.
- `plan create` exposes an OBPI-parent option, not a PRD-parent option; the authored PRD linkage must not be represented as a verified ledger ancestry edge.
- E1 Chase unavailable as of 2026-10-25; E2 flight and completion signatures remain pending.

## Human Attestation

- Attestor: unsigned
- Attestation: pending explicit human review
- Date: unsigned
