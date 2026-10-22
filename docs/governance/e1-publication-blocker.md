# E1 publication gate: gzkit adopter defects

Date: 2026-10-21. Status: upstream defects remain open; operator approved an
E1-specific publication gate in place of the full gzkit gate.
Parent: `ADR-0.1.0-mentalysis-e1`, preparation brief `OBPI-0.1.0-01-preparation`.

## Authorization and boundary

The operator approved PRD publication, then explicitly authorized repair of the
gzkit setup and installation of required development tools. `pyproject.toml`
and `uv.lock` provide that environment without product runtime dependencies.
The original full-gate failures below remain recorded. No flight has run.

## Explicit publication-policy decision

On 2026-10-22, after disclosure that replacing the gate is a policy change that
may need instructor acceptance, the operator selected **"Approve project-specific
gate"**. The authorized choice was: "Explicitly authorize replacing the
unsuitable pre-push gate, then validate, commit, and push E1 preparation."

`.pre-commit-config.yaml` now invokes `uv run python scripts/check_e1.py`.
That check validates the required preparation artifacts, agent identity and step
budget, project JSON, dated PRD approval, the fixed 20-line fixture, flight-card
sections and falsifier, and the separation between unsigned preparation and
flight observations. It runs negative-control unit tests, lint on the gate code,
ten applicable gzkit governance scopes, and authored validation of both briefs.

This intentionally replaces the full gzkit publication policy; it does not
claim to fix or pass all 58 upstream checks. It is an operator decision, not an
instructor approval. Reassess the publication gate for later layers. Model/tool
permissions and the E1 five-step contract are unchanged. Export names/JSON are
checked structurally; sanitization provenance, actual stopping behavior, and
Chase chronology still require evidence review. No E1 PASS is awarded by this
gate. A real Chase GO must precede flight.

## Confirmed dependency defects

Installed package: `py-gzkit==0.34.7`. PyPI's latest release on inspection was
`0.34.9`; it was installed in an isolated temporary environment for source
comparison, not adopted as a purported fix.

| Check | Source in the installed gzkit package | Observation |
| --- | --- | --- |
| Lifecycle coherence | `governance/trust_audits/taxonomy.py`, lines 619, 652, 692 | Searches `docs/design/adr` instead of the project's configured `design/adr`. Both current briefs exist and pass authored validation. |
| Full check selection | `commands/quality.py`, lines 576–637 | Unconditionally includes maintainer-oriented readiness, registry, and dispatch checks. |
| Configuration | `config.py`, lines 173–184, 216–224 | No adopter profile exists in root configuration; inventing one would be ignored. |
| Dispatch absorption | `quality.py`, `run_dispatch_absorption_marker_audit` | Requires gzkit's own `ADR-pool.obpi-pipeline-dispatch-attestation.md` and its `ADR-0.0.73` history. This project never made that decision. |
| Readiness | `commands/readiness.py`, specification checks | Requires `src/gzkit/templates/obpi.md`, which is a gzkit development-tree resource, not a Mentalysis source file. |

Source comparison of 0.34.9 found the same hard-coded lifecycle roots and
maintainer-only artifact requirements. That release adds step-scope exclusions;
excluding these checks would not repair their applicability or path handling.
No skip list was introduced.

## Reproduction from this repository

```text
uv sync --locked
uv run gz --version
uv run gz obpi validate --adr ADR-0.1.0 --authored
uv run gz validate --obpi-lifecycle-coherence
uv run gz check
```

Expected distinction: authored validation resolves both briefs under the
configured path; the lifecycle audit reports those same briefs unresolved.
Do not park, rename, or falsely complete them to silence this finding.

## Required upstream correction

1. Make lifecycle discovery honor the project `paths.adrs` configuration.
2. Apply gzkit-maintainer history checks only where that history is applicable.
3. Resolve reusable template resources from the project or installed package.
4. Supply an adopter-ready scaffold with coherent generated references and
   reviewed skills, rather than requiring copies of unrelated upstream history.

The earlier full run also identified unavailable tools, missing generated files,
stale skills, and absent upstream references. Local remediation and its observed
results are recorded in the AI log. A passing subset is not a passing full gate.

## Repair results — 2026-10-21

- Added a project-local development environment with `py-gzkit==0.34.7`, Ruff,
  ty, unittest-parallel, Behave, PyMarkdown, MkDocs Material, and pre-commit.
  `uv sync` installed 78 packages; `uv sync --locked` subsequently succeeded.
  The global gzkit installation was not replaced.
- Added `.gitattributes` with `* text=auto eol=lf`; the line-ending check passes.
- The full `uv run gz check --json` initially exceeded a 120-second runner
  limit. A second invocation with a 600-second limit completed and reported
  `success: false`, `scope: full`: 42 checks passed, 16 failed.
- Typecheck, module-size, QC binding, enforcement-floor, and line-ending checks
  now pass. This is not a claim of successful flight or a complete test suite.
- `uv run gz validate --documents --ledger --taxonomy --decomposition --brief-structure --req-kind-discipline --brief-command-shape --kind-invariance --persona-witness --line-endings`
  passed all ten scopes. Both authored briefs also passed.
- Control-surface sync dry-run planned 103 paths, including missing
  `docs/AGENTS.md` and `docs/governance/AGENTS.md`. The actual sync stopped at
  preflight because 16 bundled skills have expired review dates. No generated
  surfaces were manually substituted and no review dates were fabricated.

Remaining full-check failures:

| Category | Failed checks / observed cause |
| --- | --- |
| Bundled file quality | Lint: 40 findings; Format: 22 files need formatting, including generated mirrors and canonical scaffold content. |
| Test applicability | Test: `ImportError: Start directory is not importable: 'tests'`; Behave: no steps directory in `features`. E1 currently defines harness sorties, not a Python product suite. |
| Generated surfaces and skills | Validate default scopes, Skill audit, Orientation freshness, Surface fidelity; missing generated/upstream references and stale review dates. |
| Upstream-specific/path assumptions | Readiness audit, ADR status freshness, OBPI lifecycle coherence, Complexity-doctrine links, Waiver ratchet, Gate callers, Exemption controls, Dispatch absorption marker. |

No empty test suite, unrelated historical ADR, blanket ignore, or disabled hook
was introduced to turn these failures into a pass. The next actionable dependency
is an adopter-correct tool release or course-approved validation contract; the
handoff below includes the two smallest reproducible defects.

## Instructor / maintainer handoff

Mentalysis E1 preparation is blocked by `py-gzkit` adopter checks before its
Chase-reviewed flight. Please provide a corrected release or an explicit,
course-approved adopter validation procedure. The configuration uses
`paths.adrs = design/adr`; `gz obpi validate --adr ADR-0.1.0 --authored` passes,
but the lifecycle audit scans `docs/design/adr`. Full checks also require
gzkit's dispatch-absorption ADR and source-tree templates. No permission gate
has been loosened and no flight evidence has been manufactured.
