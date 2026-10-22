---
id: OBPI-0.1.0-01-preparation
parent: ADR-0.1.0-mentalysis-e1
item: 1
lane: Lite
status: Draft
allowlist:
  - .opencode/agents/mentalysis.md
  - opencode.json
  - docs/PRD.md
  - evolution-01/flight-card.md
  - evolution-01/flight-log.md
  - evolution-01/README.md
  - evolution-01/fixtures/review-queue.md
  - evolution-01/evidence/README.md
  - design-analyses/E1-react-opencode.md
  - design-analyses/LEDGER.md
  - AI_LOG.md
  - README.md
  - pyproject.toml
  - uv.lock
  - .gitattributes
  - docs/governance/e1-publication-blocker.md
  - .pre-commit-config.yaml
  - scripts/check_e1.py
  - tests/test_e1_preparation.py
reqs:
  - REQ-0.1.0-01-01
  - REQ-0.1.0-01-02
  - REQ-0.1.0-01-03
verification:
  - uv run gz validate --documents
  - uv run gz obpi validate --authored design/adr/pre-release/ADR-0.1.0-mentalysis-e1/obpis/OBPI-0.1.0-01-preparation.md
---

# OBPI-0.1.0-01-preparation: Prepare Mentalysis E1

## ADR Item

Source: `design/adr/pre-release/ADR-0.1.0-mentalysis-e1/ADR-0.1.0-mentalysis-e1.md`, checklist item 1.

## Objective

Deliver a reviewable educational DCF E1 package with a primary agent, canonical PRD, design analysis, fixed synthetic fixture, and unsigned flight templates; preparation itself produces no flight observations.

## Lane

**Lite** - Educational configuration and supporting documents. Reassess the lane before adding an external runtime contract. Human attestation remains mandatory for completion.

## Allowed Paths

- `.opencode/agents/mentalysis.md` — primary-agent instructions, model, five-step budget.
- `opencode.json` — project agent selection/configuration.
- `docs/PRD.md` — **CREATE** canonical user-facing requirements.
- `evolution-01/flight-card.md` — TP1/TP2 prompts, expected outcomes, unsigned Chase review.
- `evolution-01/flight-log.md` — clearly pending observation template.
- `evolution-01/README.md` — execution and review procedure.
- `evolution-01/fixtures/review-queue.md` — exactly 20 synthetic physical lines.
- `evolution-01/evidence/README.md` — evidence capture instructions with no invented receipt.
- `design-analyses/E1-react-opencode.md` — preflight ReAct design analysis and pending observation fields.
- `design-analyses/LEDGER.md` — design-analysis index, distinct from the gzkit event ledger.
- `AI_LOG.md` — honest preparation record.
- `README.md` — project navigation and educational purpose.
- `pyproject.toml`, `uv.lock` — development-only tooling for reproducible checks.
- `.gitattributes` — cross-platform LF normalization policy.
- `docs/governance/e1-publication-blocker.md` — observed upstream defects and reproduction commands.
- `.pre-commit-config.yaml`, `scripts/check_e1.py`, `tests/test_e1_preparation.py`
  — explicitly approved preparation publication policy and negative controls.

These parent-session implementation paths now exist. They were initially green-field under the approved parent ADR Interfaces layout. Conversion-related reference edits were explicitly authorized on 2026-10-18; this does not authorize changes to flight scope or signatures.

## Denied Paths

- `AGENTS.md` — generated root contract, explicitly protected.
- `design/adr/pre-release/ADR-0.1.0-mentalysis-e1/obpis/OBPI-0.1.0-02-flight.md` — separate flight work unit.
- `.gzkit/ledger.jsonl` — CLI-owned, never hand-edited.
- All paths not explicitly allowed. On 2026-10-21 the operator approved the
  proposed repair of gzkit setup and installation of required development tools
  with "yes". That authorizes the development environment and lockfile above,
  plus CLI-regenerated control surfaces needed for the existing scaffold. It
  does not authorize disabling checks, inventing upstream history, or changing
  the frozen flight tools/model/steps. Subsequently the operator explicitly
  selected "Approve project-specific gate", authorizing replacement of the
  full pre-push check with the E1 preparation gate. This policy decision is
  documented in `docs/governance/e1-publication-blocker.md`; it is not a flight
  approval or an assertion of instructor acceptance.

## Requirements (FAIL-CLOSED)

1. REQ-0.1.0-01-01: MUST describe educational synthetic DCF, primary `mentalysis`, `opencode/big-pickle`, and `steps: 5` consistently across configuration, PRD, and design analysis.
2. REQ-0.1.0-01-02: MUST specify TP1 as next-year FCF 100 divided by 0.10 minus 0.03, expected 1428.57; MUST specify TP2 as offset i / limit 1, next line only next assistant turn, against exactly 20 lines. NEVER assume tool-read count equals steps.
3. REQ-0.1.0-01-03: MUST leave flight observations pending and Chase GO/human attestation unsigned; MUST document fixed tools and permissions throughout flight. NEVER run a model, flight, commit, or push as preparation evidence.

> STOP-on-BLOCKERS: missing approved configuration, fixture, or review instructions block flight readiness; report them rather than fabricating results.

## Discovery Checklist

**Parent ADR (read first; order pinned):**

- [ ] Quote parent ADR Decision item 1 verbatim in Implementation Summary.
- [ ] Read parent ADR Intent, then Interfaces and Boundary Invariants.

> **STOP:** If you cannot quote the parent ADR Decision item this brief implements, STOP and re-read before proceeding to paths or implementation.

**Governance:**

- [ ] Read `AGENTS.md` and the registered `design/prd/PRD-MENTALYSIS-1.0.0.md`.

**Prerequisites:**

- [ ] Confirm operator approval of E1 scope and green-field layout in the parent ADR.
- [ ] Check `docs/PRD.md` ownership with the parent session and preserve concurrent edits.

**Existing Code:**

- [ ] Inspect `.opencode/agents/mentalysis.md` and `opencode.json` if the parent has created them; otherwise use the approved new-file contract.
- [ ] Inspect `evolution-01/fixtures/review-queue.md` if present and count physical lines; do not replace user-authored content without review.

## Quality Gates

Gate 1 requires registered lineage and authored briefs. Gate 2 requires checking the package against REQs, not treating a zero-test run as behavioral proof. No runtime code is implemented by governance authoring. Gate 5 always requires explicit human attestation. Lint availability is an open blocker, not a clean result.

## Verification

```text
uv run gz validate --documents
uv run gz obpi validate --authored design/adr/pre-release/ADR-0.1.0-mentalysis-e1/obpis/OBPI-0.1.0-01-preparation.md
uv run gz validate --req-kind-discipline
```

Manual product verification: inspect all twelve preparation files, compare model/steps and prompts across surfaces, count queue lines, and confirm every observation/signature field remains pending. Record file/line evidence in the preparation record. Governance checks do not prove model behavior.

## Demo

Walk Chase through `docs/PRD.md`, the agent configuration, and the unsigned flight card. Recompute `100 / (0.10 - 0.03)` independently as the oracle. Show the 20-line fixture and the next-turn restriction without executing the agent.

## Acceptance Criteria

- [ ] REQ-0.1.0-01-01 [SUPPORT]: PRD, agent configuration, and design analysis agree on educational scope/model/steps; prove by artifact review plus `gz validate --documents` and the `obpi_created` registration event.
- [ ] REQ-0.1.0-01-02 [SUPPORT]: Flight card and 20-line fixture encode the exact TP1 oracle and TP2 turn restriction; prove by line-count/prompt review plus `gz validate --documents` and `obpi_created` lineage.
- [ ] REQ-0.1.0-01-03 [SUPPORT]: Templates clearly distinguish expectations from pending observations, retain unsigned approvals, and freeze flight configuration; prove by review plus `gz validate --documents` and `obpi_created` lineage.

## Completion Checklist

- [ ] All REQs have concrete artifact-review evidence.
- [ ] Validation outputs and tooling blockers recorded.
- [ ] Human reviews preparation; completion attestation recorded only when explicitly supplied.

## Evidence

### Implementation Summary

Decision quote: "Prepare the Mentalysis E1 requirements, primary-agent configuration, design analysis, and unsigned flight package under the approved five-step contract."

Governance brief authored on 2026-10-18; parent-owned preparation artifacts are separate work. This is a specification, not an implementation-completion claim.

### Gate 1 (ADR)

PRD, ADR, and OBPI created through `uv run gz` with automatic registration. Observed 2026-10-18:

- `uv run gz validate --documents --ledger --decomposition --brief-structure --req-kind-discipline --brief-command-shape --kind-invariance --persona-witness`: all validations passed (8 scopes).
- `uv run gz validate --fidelity-presence`: every non-pool ADR Decision carries a Fidelity Assertions block.
- Initial authored validation failed for absent parent-owned paths; that path-discovery blocker was resolved when preparation files were created. Current validation command: `uv run gz obpi validate --adr ADR-0.1.0 --authored`.
- `uv run gz validate --taxonomy`: one error, foundation ADR not declared in `data/foundation_grandfather.json`.
- Initial registration dry-run found no unregistered artifacts. Current registration check: `uv run gz register-adrs ADR-0.1.0 --all --dry-run`.
- `uv run gz status`: ADR Pending, 0/2 complete, both briefs PENDING, QC readiness pending OBPI completion and TDD.
- `git diff --check`: no output; files are untracked, so this is not a content-validation substitute.

An initial combined validation including `--fidelity-presence` was rejected because that scope must run alone; the corrected separate commands above passed. Initial `gz specify` reported default lane because the WBS heading/columns were not parseable; the ADR now uses the installed parser's `OBPI Decomposition` heading and numbered five-column schema, and both brief lanes explicitly match Lite.

### Gate 2 (Verification)

The parent-authored package exists; acceptance review and actual flight remain pending. No flight test or model call has occurred in this conversion pass.

### Gate 5 (Human)

Pending and unsigned. Plan approval is not completion attestation.

### Blockers and Defects

- 2026-10-21 repair scope: user authorized setup repair and development-tool
  installation. Tools are development dependencies, not product runtime
  dependencies: stdlib cannot supply the external lint/typecheck/BDD commands
  that gzkit invokes. `py-gzkit` must also be importable by project-interpreter
  chores. `uv.lock` records the resolved environment. Full-check outcomes and
  upstream applicability defects are tracked in
  `docs/governance/e1-publication-blocker.md`; no Gate 2 success is implied.
- Initialization reported ruff unavailable; lint success cannot be claimed. No package installation authorized.
- `gh` unavailable per operator handoff; issue filing unavailable, so defects are tracked here.
- Generated governance instructions link upstream documentation not shipped locally, including `docs/governance/agent-contract-rationale.md` and `docs/governance/GovZero/obpi-decomposition-matrix.md`. Do not invent local copies or claim these references resolve.
- Human attestation and Chase GO pending. Parent-owned E1 files now exist; this resolves the initial missing-path blocker, not human acceptance.
- Skills request delegation, but this execution surface exposes no subagent launcher/model selector; direct scoped authoring is the available fallback, with no Opus claim.
- The original Foundation Sunset blocker prompted operator-approved conversion to feature 0.1.0. No grandfather exemption was added. Conversion validation is recorded in `AI_LOG.md`.
- The installed creates-marker parser excludes several approved E1 roots, but the actual files now exist; no placeholder or allowlist weakening was used.
- ADR frontmatter links `PRD-MENTALYSIS-1.0.0`, but `gz state` shows no ADR ledger parent: `plan create` offered only `--obpi`, not a PRD-parent option, and registration preceded semantic authoring. `register-adrs --dry-run` finds no missing registrations. The document linkage exists; ledger-level PRD ancestry is not claimed or hand-patched.

### Commit-Ledger Mechanism Investigation

Installed gzkit 0.34.7 provides `gzkit.hooks.commit_ledger`, whose module entry point calls `record_committed_artifact_edits(Path.cwd())` for HEAD. It emits deduplicated `artifact_edited` events carrying the commit SHA via `Ledger.append`; governance path matching covers `design/prd/*.md` and `design/adr/**/*.md`. It observes committed edits only, not this uncommitted work. The repository `.pre-commit-config.yaml` declares only a pre-push check, not this post-commit recorder. No hook configuration was changed.

`uv run gz ledger --help` exposes only `merge-driver`, not a generic event-append or commit-record command. `uv run gz git-sync --help` describes commit/fetch/rebase/push execution; it was not executed. `uv run python -c "import gzkit; print(gzkit.__file__)"` failed with ModuleNotFoundError: the uv project interpreter does not import the uv-tool installation. `uv tool list` confirms `py-gzkit v0.34.7`; the installed module was inspected read-only. A future authorized commit can use the packaged post-commit recorder with the tool environment's interpreter; invocation was not tested because it writes ledger events against HEAD. No ledger was hand-edited and no new commit event was fabricated.

### Value Narrative

Before: approved intent without execution boundaries. Yield: a reviewable preparation contract that cannot be mistaken for flight evidence.

### Key Proof

The arithmetic oracle is 1428.57; all observed-answer fields remain pending until the flight brief executes.

## Human Attestation

- Attestor: unsigned
- Attestation: pending explicit human review
- Date: unsigned
