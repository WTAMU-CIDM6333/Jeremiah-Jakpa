# AI interaction log

Historical entries are preserved in `evolution-00/AI_LOG.md`.

## 2026-10-18 — E1 preparation

- **Asked:** Continue Evolution 0 in WTAMU-CIDM6333/Jeremiah-Jakpa; start E1 of
  the four-layer OpenCode assignment, with gzkit governance and Chase review.
- **Model and harness:** Authoring assistant `openai/gpt-6-astra` through OpenCode;
  installed CLI `1.18.21`. Governance delegated through the task tool as required
  by the generated gzkit skills; no separate subagent model ID was exposed.
  Flight model configured as `opencode/big-pickle`, not yet flown.
- **Accepted:** User authorized gzkit initialization including local Git merge
  driver configuration, chose foundation kind, and approved five steps, the
  proposed model, synthetic tests, and two preparation/flight briefs.
- **Modified:** Work uses a new course-repository clone with E0 already nested
  under `evolution-00/`. Root PRD and E1 artifacts distinguish drafts from flight
  evidence and human signatures. The original checkout's uncommitted log remains
  there.
- **Rejected:** Treating an assistant assertion as flight evidence; signing for
  the owner or Chase; claiming the model is available merely because it is listed.
- **Claim checked:** OpenCode's `steps` setting limits agentic iterations before
  a text-only response. Checked against
  https://opencode.ai/docs/agents/#max-steps on 2026-10-18. The documentation
  confirms the setting; runtime proof remains TP2's job.
- **Observed tooling:** `opencode --version` returned `1.18.21`; export help lists
  `--sanitize`; model listing includes `opencode/big-pickle`; `gz --version`
  returned `0.34.7`. `gz init --no-skeleton --mode lite` succeeded but warned
  that `ruff` was unavailable. `gh` is unavailable on PATH.
- **Governance blockers:** Installed gzkit accepts foundation creation but its
  taxonomy validator rejects new foundations under Foundation Sunset. Resolve
  this with the operator before committing; no grandfather exemption fabricated.
- **Outcome:** E1 preparation authored; PRD attestation, frozen substrate, Chase
  GO, flight, evidence review, and commits remain pending.
- **Validation:** `opencode agent list` loaded `mentalysis (primary)` successfully.
  Both briefs passed `uv run gz obpi validate --adr ADR-0.0.1 --authored` after
  the E1 files were created. Documents, ledger, decomposition, brief structure,
  REQ kinds, command shape, kind invariance, and persona witness passed together.
  Taxonomy still fails with: `The foundation kind is CLOSED to new authoring`.
  `git diff --check` produced no errors, but the new files are untracked and
   therefore that command alone does not validate their whitespace.

## 2026-10-21 — E1 preparation reconciliation and preflight checks

- **Asked:** Finish the remaining E1 work.
- **Authoring model:** `openai/gpt-6-astra` through OpenCode. Flight model remains
  `opencode/big-pickle`; no flight/model invocation was made in this pass.
- **Found:** Existing operator-approved conversion created feature
  `ADR-0.1.0-mentalysis-e1`; the card and root README still referenced the
  previous foundation. Updated those live pointers and the E1 runbook.
- **Claim checked:** The installed runtime loads Mentalysis as a primary agent
  with five steps and the specified model. Checked against actual output of
  `opencode debug agent mentalysis`, not only YAML. `opencode --version` returned
  `1.18.21`; `opencode export --help` explicitly lists `--sanitize`.
- **Observed configuration:** Resolved default agent `mentalysis`, sharing
  disabled, no configured plugins/MCP servers, no explicit top-level permission
  override; read enabled. The card records a non-secret configuration summary.
- **Verification:** Documents, ledger, taxonomy, decomposition, brief structure,
  REQ kinds, command shape, kind invariance, and persona witness all passed
  together (nine scopes). Authored validation passed both ADR-0.1.0 briefs.
  Read the complete 20-line synthetic fixture and reviewed the existing
  nine-component analysis, judgment loop, and analysis-ledger row.
- **Remaining:** PRD and preparation acceptance, intended-file commit and
  commit-ledger events, frozen preparation SHA, assigned Chase's committed GO,
  actual flight/export observations, Chase verdict, and publication to main.
  Git reports E1/governance files untracked. No completion, signature, model
  availability, successful flight, or submission is claimed.

## 2026-10-21 — Product attestation and authorized publication attempt

- **Operator statement (verbatim):** "I have reviewed and approve the Mentalysis PRD’s user, problem, scope, and acceptance criteria, And authorize a commit and push"
- **Model:** `openai/gpt-6-astra` through OpenCode; no flight model invoked.
- **Action:** Recorded the operator's dated PRD attestation and updated current
  preparation status. Reviewed Git status, diff, recent commits, remote, sync
  help/dry-run, installed hooks, and the packaged commit-ledger recorder.
- **Checked claim:** The repository's pre-push hook is declared to invoke
  `uv run gz check` in `.pre-commit-config.yaml`. Running that full command
  exposes failures not covered by the previously passing nine scoped checks.
- **Observed:** Full check fails for unavailable tools (`ruff`, `ty`,
  `unittest-parallel`, `behave`), missing generated surfaces and upstream-only
  artifacts, stale skill reviews, lifecycle resolution, and further scaffold
  fidelity/enforcement checks. Detailed categories and repair boundary are
  recorded in `evolution-01/README.md` under Publication blocker.
- **Outcome:** Product approval is recorded locally. Full publication gate is
  blocked; no commit, push, ledger commit event, or flight result is claimed.
  The E1 brief prohibits dependency/CI changes and other paths needed for a
  broad scaffold repair. No hooks or validators were disabled.

## 2026-10-21 — Authorized toolchain repair and upstream diagnosis

- **Authorization:** The operator replied "yes" to repairing gzkit setup,
  installing required development tools, and then retrying publication. Updated
  the preparation brief to record the approved environment/diagnostic paths.
- **Model:** `openai/gpt-6-astra` through OpenCode. Used an exploration subagent
  for independent installed-source comparison; its underlying model ID was not
  exposed. Independently read the decisive source and ran the lifecycle checks.
- **Claim checked:** Lifecycle audit ignores configured `paths.adrs`. Verified
  `governance/trust_audits/taxonomy.py` lines 619, 652, and 692 in 0.34.7 and
  reproduced its two failures while authored validation passes both briefs.
- **Release check:** PyPI reported 0.34.9. Installed it in an isolated temporary
  environment for comparison; its dispatch audit still requires gzkit's own
  historical ADR. No unverified global upgrade or package-source patch applied.
- **Installed:** Project-local development dependencies and `uv.lock`; `uv sync`
  installed 78 packages and `uv sync --locked` subsequently succeeded. Added LF
  normalization policy. No Mentalysis runtime dependency was introduced.
- **Full verification:** `uv run gz check --json` exceeded the first 120-second
  limit; the 600-second retry completed: 42 passed, 16 failed. Typecheck,
  module-size, QC binding, enforcement floor, and line endings now pass.
  Ten scoped governance checks and both authored brief checks pass. Tests still
  fail because E1 has no importable `tests` suite or Behave `features` steps.
- **Sync:** Dry-run identified required generated files. Actual sync preflight
  rejected 16 expired skill reviews, so generated-file repair remains blocked.
- **Handoff:** `docs/governance/e1-publication-blocker.md` records reproducible
  defects and a message for the instructor/maintainer. No blank suites, forged
  skill reviews, upstream historical artifacts, or gate exclusions were added.
- **Outcome:** Local tooling repaired; complete publication remains blocked.
  No commit/push, frozen preparation SHA, Chase GO, or flight evidence is claimed.

## 2026-10-22 — Explicit E1 publication-policy decision

- **Operator decision:** "Approve project-specific gate", after disclosure
  that replacing the unsuitable full gzkit pre-push command changes repository
  policy and may need instructor acceptance. Commit/push authorization remains
  active. This is not permission to fly without Chase GO.
- **Model:** `openai/gpt-6-astra` through OpenCode.
- **Change:** Added `scripts/check_e1.py` and negative-control tests; the
  pre-push hook now runs the E1 preparation gate. Full upstream check failures
  remain documented; no claim that all gzkit checks pass is made.
- **Scope:** Structural preparation, ten applicable governance scopes, authored
  briefs, and tests/lint for the new gate. Filename checks do not establish
  sanitization provenance or runtime behavior; those remain human-reviewed.
- **Checked claim:** Nine unit tests passed on the first run; Ruff then caught
  the wrong exception type for malformed YAML mappings. Corrected that defect
  before retrying the gate. Final publication outcome is recorded by Git history.
- **Verification after repair:** The complete E1 preparation gate passed: nine
  unit tests, scoped Ruff lint, ten governance validation scopes, and both
  authored briefs. This is preparation verification only.
- **Preparation commit:** `d0743be8acf896b6a1fd1af97a172f53475f22d2`.
  The packaged `uv run python -m gzkit.hooks.commit_ledger` emitted seven
  governance artifact-edit events. Card-freeze follow-up records this baseline.
  OpenCode 1.18.21 again resolved the primary agent/model/five-step setting on
  2026-10-22. No flight model invocation or Chase signature was fabricated.
