# E5 AGENTS.md (revised from 09/17 lab base)

Never imply that code, tests, or automated enforcement exist in this repository when they do not.

## Run and test
- ALWAYS run tests via `uv run python -m unittest discover -s tests` (enforced by pre-commit hook `test-discovery`).
- NEVER skip pre-commit checks (enforced by `.pre-commit-config.yaml`).
- Budget check: `wc -c AGENTS.md` must stay under 4000 (enforced by CI check `agents-budget`).

## Conventions
- ALWAYS use PowerShell 5.1 syntax on Windows (enforced by shell policy in environment).
- NEVER commit secrets (enforced by pre-commit secret scanner).
- ALWAYS record AI interactions in `AI_LOG.md` in the same change (enforced by review checklist).

## Skills
Multi-step procedures moved to skills:
- Testing: see `.opencode/skills/test-runner/SKILL.md`
- Committing: see `.opencode/skills/git-commit/SKILL.md`
- Flight operations: see `.opencode/skills/flight-ops/SKILL.md`

## Truth
- Interaction history: `AI_LOG.md`
- Harness: `choices.md`
- Evidence: `evolution-*/flight-log.md`
