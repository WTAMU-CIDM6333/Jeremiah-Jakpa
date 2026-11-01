# Evolution-0

Never imply that code, tests, or automated enforcement exist in this
documentation-only repository when they do not.

## Run and test

- Tests: none. Do not add a test runner or report tests as run.
- Pre-commit check: `git diff --check` for whitespace and conflict markers
- Budget check: `wc -c AGENTS.md` must stay under 4000
- Commit gate: run `git diff` and stop before staging. Enforced by: nothing
  automated; approval is manual.

## Conventions that differ from defaults

- Shell is Windows PowerShell 5.1. No `&&`; chain with `;` and `if ($?)`.
- LF-to-CRLF warnings on Windows are benign, not errors.
- Record each AI interaction in `AI_LOG.md` in the same change as the work it
  describes: asked, model and harness, accepted, modified, rejected.
- Before adding a path or claim, confirm it exists by reading it. Omit anything
  you cannot confirm.
- Skill-level claims must match `skills-inventory.md`.
- If a rule must hold regardless of what the model decides, surface it to the
  user as unenforced until a hook or permission deny exists.

## Rules that must hold (enforced)

- None. This repository has no hooks and no permission rules, so no rule in it
  is mechanically enforced. Do not describe one as enforced.

## Where the truth lives

- Interaction history and decisions: `AI_LOG.md`
- Model route, harness, framework choice: `choices.md`
- System definition, primary risk, PEAS: `pitch.md`
- Harness comparison: `design-analysis.md`, indexed by `design-analyses/LEDGER.md`
- Installed tool versions: `toolkit-check.md`
- Framework coverage state: `board.md`
- This lab's measurements: `evolution-03/agents-md-measurement.md`
