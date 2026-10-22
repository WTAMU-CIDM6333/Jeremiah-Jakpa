# E1 — Mentalysis on OpenCode

Current phase: preparation, before Chase review and flight.

1. Product requirements were attested in `docs/PRD.md` on 2026-10-21.
2. Review the current feature plan `design/adr/pre-release/ADR-0.1.0-mentalysis-e1/`
   and its preparation/flight briefs. The previous Foundation Sunset blocker is
   resolved: taxonomy and eight other governance scopes passed on 2026-10-21.
   Review the remaining tooling and approval blockers before freezing the card.
3. Quit and restart OpenCode from the `Jeremiah-Jakpa` repository root so it loads
   the project configuration and `mentalysis` primary agent. Inspect effective
   configuration locally; do not publish secrets from global settings.
4. Review and commit preparation changes with their gzkit ledger events. Fill
   the flight card's pending substrate fields using the preparation commit SHA,
   then commit the frozen card and send it to your Chase.
5. Chase commits a dated GO before either test point runs. A NO-GO returns the
   card to preparation.
6. Run the two exact prompts on the card in fresh sessions. Export each session
   using `opencode export <sessionID> --sanitize`, without manual editing.
7. Fill the flight log with observed counts, evidence identifiers, hashes, and
   PASS/FAIL/ABORT. Commit log and sanitized evidence with ledger events.
8. Ask Chase to review the evidence and append the required CHASE verdict.

E2 starts after the E1 evidence/review cycle. No flight result is claimed here.

## Preparation verification — 2026-10-21

- `opencode --version`: `1.18.21`.
- `opencode export --help`: `--sanitize` is supported.
- `opencode debug agent mentalysis`: primary, provider `opencode`, model
  `big-pickle`, steps 5, read tool enabled.
- `opencode debug config`: default agent `mentalysis`, sharing disabled, no
  configured plugins/MCP servers or explicit top-level permission override.
- `uv run gz validate --documents --ledger --taxonomy --decomposition --brief-structure --req-kind-discipline --brief-command-shape --kind-invariance --persona-witness`:
  all nine scopes passed.
- `uv run gz obpi validate --adr ADR-0.1.0 --authored`: both briefs passed.
- Fixture review: exactly 20 numbered physical lines, 01 through 20.
- Oracle: `100 / (0.10 - 0.03)` rounds to `1428.57`; the numerator is already
  next-year FCF and must not be multiplied by growth a second time.

These are preparation checks, not flight evidence or a model-availability test.
The existing nine-component design analysis and judgment loop are in
`design-analyses/E1-react-opencode.md`, with its E1 ledger row already present.

## Remaining release and human gates

1. PRD attestation and commit/push authorization were supplied on 2026-10-21.
   Preparation completion remains a separate governed acceptance decision.
2. Review/stage the intended E1 and governance files, commit preparation with
   the required ledger events, then record its immutable SHA in the card. The
   current E1 package is untracked; an E0 HEAD SHA cannot stand in for it.
3. Commit the frozen card and make it available to the assigned Chase. Chase
   appends the actual dated GO in the repository before either test runs.
4. Run TP1 and TP2, capture unedited sanitized exports, inspect the actual
   iteration records, and fill the flight log. Obtain Chase's evidence verdict.
5. Push the reviewed work to GitHub main and verify that the expected commits
   are visible there.

The flight brief's older references to a "raw transcript" mean underlying
observations, not permission to commit raw exports: the assignment requires
sanitized OpenCode exports only, as specified in `evidence/README.md`.

## Publication blocker — 2026-10-21

The nine scoped governance checks and both authored briefs pass, but the full
`uv run gz check` required before sync fails. The installed pre-push hook invokes
this same full check. Commit/push authorization has been received; publication
is blocked, not completed.

Observed failures include missing `ruff`, `ty`, `unittest-parallel`, and
`behave`; a chore cannot import `gzkit` from the project interpreter. The
generated scaffold also requires absent `docs/AGENTS.md`, orientation scripts,
an ADR index, and `.gitattributes`. Sixteen shipped skills exceed the 90-day
review limit. Several checks require gzkit-maintainer artifacts such as
`src/gzkit/templates/obpi.md`, `docs/design/prd/PRD-GZKIT-1.0.0.md`, the dispatch
absorption pool ADR, and waiver/gate/exemption registries. Lifecycle coherence
reports both current briefs unresolved despite their authored validation passing.

The operator approved development-environment and setup repair on 2026-10-21.
`pyproject.toml` and `uv.lock` now provision the required tools; `.gitattributes`
fixes the line-ending policy. `uv sync --locked` succeeds, and ten scoped checks
pass. The full check still reports 42 passed and 16 failed: the installed
release has adopter-path and maintainer-only artifact defects, plus scaffold
quality/review issues. Source inspection of latest release 0.34.9 found the
same principal defects. Actual control-surface sync stops on stale skill reviews.

See [the detailed publication-policy report](../docs/governance/e1-publication-blocker.md)
for repair results, source locations, reproduction commands, and the explicit
operator decision to replace the unsuitable full pre-push check with an E1
preparation gate. Run `uv run python scripts/check_e1.py` to verify preparation.
This is not an instructor approval or flight verdict. The upstream failures
remain disclosed. Chase review and flight remain pending.
