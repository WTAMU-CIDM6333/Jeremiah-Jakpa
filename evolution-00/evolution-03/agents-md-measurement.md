# AGENTS.md Measurement

## Setup

| Field | Value |
| --- | --- |
| OpenCode version | `1.18.21` |
| Model used | `opencode/big-pickle` |
| Model specified by lab | `opencode/big-pickle` |
| Model deviation | None |
| Model confirmation | Confirmed in-session; the active model reports itself as `big-pickle`. |
| Existing project `AGENTS.md` | None |
| Existing project `CLAUDE.md` | None |
| Existing global OpenCode `AGENTS.md` | None found |
| `/init` run before drafting | No |

## Inventory

Derived from `AI_LOG.md`, the commit history, and this lab session. Items are
recorded only where there is observable evidence; nothing is inferred.

### Repeated corrections the agent received

1. **Output length did not match the requested scope.** The user asked to
   "dilute" the lab instructions, then asked to combine the steps, then asked
   for the "simplest form". Default verbosity repeatedly overshot.
2. **Records were not kept without an explicit prompt.** The user had to ask
   "please keep record yourself too", and Step 8 of the previous assignment
   existed to repair an entry that had been wrong when written.
3. **Structure was assumed rather than verified.** The previous assignment
   referred to "twelve layers" while naming only nine, and the lab template
   names `docs/prd.md`, `docs/adr/`, and flight cards. In both cases the agent
   had to avoid inventing what the source did not contain.

### Re-explained in chat after being established earlier

1. **The working model.** Already recorded in `choices.md` and `AI_LOG.md`, yet
   restated several times: lab default `opencode/big-pickle`, then Muse Spark,
   then `openai/gpt-5.6-sol`, then back to `opencode/big-pickle`.
2. **Review and record before committing.** Established at the start of the
   assignment and re-asserted at every step, including again for this lab.

### Where the truth lives

| Subject | Path |
| --- | --- |
| Every AI interaction, decision, and deviation | `AI_LOG.md` |
| Model route, harness, provisional framework | `choices.md` |
| System definition, primary risk, PEAS mapping | `pitch.md` |
| Chat assistant versus harness comparison | `design-analysis.md` |
| Index of completed analyses | `design-analyses/LEDGER.md` |
| Installed tool versions | `toolkit-check.md` |
| Framework coverage state (42 of 62) | `board.md` |
| Claimed skill levels and work samples | `skills-inventory.md` |
| Repository file map | `README.md` |
| This lab's measurements | `evolution-03/agents-md-measurement.md` |

### Control surfaces that do not exist yet

This repository is documentation only. Verified absent:

- No source code, no `pyproject.toml`, no `uv` project
- No test suite and no `pytest` configuration
- No `.gzkit/ledger.jsonl` and no `gz` ledger
- No `docs/prd.md`, no `docs/adr/`, no `docs/rulings/`
- No `evolution-*/flight-card.md` or `flight-log.md`
- No hooks and no `opencode.json` permission rules

The lab template's commands (`uv sync`, `uv run pytest -q`, `gz status`) and
truth paths are therefore **inapplicable here** and must not be copied into
`AGENTS.md`. There is no enforced-rule section to populate, because nothing is
mechanically enforced in this repository.

## Draft

First draft: 1763 characters. After self-applying the three probes: 1640
characters. Budget is 4000.

### Pruning applied

- Removed the repository description, which `README.md` and the directory
  already make derivable. Kept only the prohibition on implying that code,
  tests, or enforcement exist.
- Removed the unenforceable no-secrets and no-push-to-main rules, which were
  wishful rules with nothing behind them.
- Replaced the unenforced-rules list with a single factual statement that no
  rule in this repository is mechanically enforced.
- Moved the guidance for handling future unenforced rules into conventions,
  where it is a practice rather than a claimed guarantee.
- Removed the duplicated commit-approval line from two sections.

### Open item

The lab expects each unenforced rule to name a GitHub issue. No issues have
been opened, because that writes to the public repository and has not been
authorized. Until they are, the enforced-rules section states the absence
rather than pointing at a placeholder.

## Measurements

Measured with `opencode run --format json -m opencode/big-pickle` using the
lab's fixed probe `Reply with the single word OK.` in a fresh session each time.

The bare `tokens.input` field is not stable between runs, because the cache
read varies independently. The comparable figure is **total input**,
`input + cache.read`, which the JSON event reports as
`tokens.total - tokens.output`.

### Pre-Chase file, 1640 characters

| Measurement | Value |
| --- | --- |
| Baseline total input | 7962 |
| With file, total input | 8451 |
| Difference | 489 |
| Difference per character | 0.30 |

### Post-Chase file, 1665 characters

The file was revised after the review, so it was measured again rather than
reporting a number that no longer matches the committed content.

| Measurement | Value |
| --- | --- |
| Baseline total input, second sample | 8012 |
| With file, total input | 8464 |
| Difference | 452 |
| Difference per character | 0.27 |

Run-to-run spread on the baseline is about 50 tokens, so the honest result is
roughly **450 to 490 tokens**, or **0.27 to 0.30 per character**. Both
measurements sit inside the quarter-to-third range the lab predicts.

An earlier reading of 471 used the bare `tokens.input` field. It has been
replaced above because a shift in cache read made that figure look more precise
than the method supports.

### Verbatim recall

Probe: `What does this project's AGENTS.md say the test command is?`

Answer: `There is no test command - AGENTS.md says "Tests: none."`

Result: **yes**. The reply matches the file. This repository genuinely has no
test suite, so the correct verbatim answer is the absence of a test command, and
the model returned the file's exact claim rather than inventing a command. A
model that had not loaded the file would have been expected to answer with
`pytest` or `uv run pytest -q`.

### `/init` comparison

`/init` was run in a scratch copy at a temporary path, never in the repository,
so the hand-written file was not at risk. The file was removed from the copy
first so `/init` generated its own rather than editing an existing one.

| Specimen | Characters | Lines | Ratio |
| --- | --- | --- | --- |
| Hand-written `AGENTS.md` | 1640 | 45 | 1.0x |
| `/init` output | 2985 | 62 | 1.82x |
| Budget | 4000 | - | - |

The hand-written figure is the pre-Chase file, which is the version `/init` was
compared against. The final file is 1665 characters.

Both fit the budget, so size alone does not separate them. Content does.

The generated file fails all three probes:

1. **Probe 1, encyclopedia.** It restates that there is no source code, no
   `pyproject.toml`, no test suite, and no linter, and that the remote is a
   public personal repository. Every one of those facts is readable from the
   directory listing and `.git/config`.
2. **Probe 2, wishful rule.** It instructs the agent not to create an
   organization repository, not to commit or push without asking, and to update
   `README.md` whenever a file changes. None of these are backed by a hook or a
   permission deny; they are requests.
3. **Probe 3, unverifiable sentence.** "No hype, no filler," "bold sparingly,"
   and "length follows the requested scope exactly" cannot be confirmed by any
   command or diff. The generated file even cites the observation that verbosity
   is the most frequent correction, which is a finding from the conversation
   rather than a fact about the repository.

One genuine improvement is worth carrying over: the generated file names the
specific prose conventions per file, such as `board.md` being a checklist where
an unchecked box is a reading-list item. That is a non-derivable convention and
belongs in the map. The hand-written file does not currently carry it.

### Known deviation

On Windows PowerShell there is no `wc` binary. Character counts were taken with
`(Get-Content AGENTS.md -Raw).Length`, which returns the same value `wc -c`
would produce. The file still says `wc -c` because the lab wording uses it and
the file is intended to be portable to a POSIX shell.

## Chase Review

Status: **partner review complete on our side; partner's review of our file still pending.** Steps 1 through 6 are complete and measured.

### Worksheet as filled so far

| Field | Value |
| --- | --- |
| `opencode --version` | `1.18.21` |
| Model | `opencode/big-pickle` |
| Inventory: got wrong or corrected twice (3) | Output length overshot the requested scope; records were not kept without a prompt; structure was assumed rather than verified |
| Inventory: re-explained (2) | The working model; the review-and-record-before-commit rule |
| Where truth lives (paths) | `AI_LOG.md`, `choices.md`, `pitch.md`, `design-analysis.md`, `design-analyses/LEDGER.md`, `toolkit-check.md`, `board.md`, `evolution-03/agents-md-measurement.md` |
| `wc -c AGENTS.md` | 1640 |
| Input tokens: baseline / with file / difference | 6042 / 6513 / 471 |
| Verbatim recall of test command | yes |
| `wc -c` of `/init` output | 2985 |
| Chase partner | Assigned; identity not yet known |
| Our probes on their file: Probe 1 | `Current technical choices: evolution-00/choices.md` — filename restated, deleted |
| Our probes on their file: Probe 2 | `Do not present considered, provisional, or untested choices as final or tested.` — no enforcement, rewritten |
| Our probes on their file: Probe 3 | `Use plain English for explanations; keep required course terminology.` — unverifiable, rewritten as a check |
| Verdict on their file | FAIL, all three found on second read |
| Their probes on our file | Three findings received; recorded as self-review |
| Verdict on our file | PASS, after the three findings were fixed |

### Probes run on the partner's file

Partner file: *Graduate Application Identity-Assurance and Triage System*.
One probe per failure type, one-line result each.

| Probe | Line found | Result |
| --- | --- | --- |
| 1, encyclopedia | `- Current technical choices: evolution-00/choices.md` | Deleted; every role description restated its filename, and `ls evolution-00/` already shows the same paths |
| 2, wishful rule | `- Do not present considered, provisional, or untested choices as final or tested.` | Moved to Rules and rewritten as `Enforced by: nothing yet — GHI #n` |
| 3, unverifiable | `- Use plain English for explanations; keep required course terminology.` | Rewritten as a check: every required technical term has a plain-English definition at its first occurrence in the same document |

**Verdict: FAIL.** The second read found all three problems.

Secondary finding: the partner's rule referencing `GHI #1` is correctly
formatted, but only valid if issue #1 has actually been opened. A reference to
an issue that does not exist is a placeholder and fails Probe 2 on review.

Structural note: the partner's file has no `Run and test` section. The template
asks for four sections, so either add one recording that no commands apply, or
flag the omission.

### Self-review of our file before it is exchanged

Run against the hand-written file, so the partner is not reviewing known
defects for the first time:

- **Probe 1 candidates, derivable from the repo.** The `Where the truth lives`
  list is close to a directory listing, since the agent can run `ls` and see the
  same nine files. The descriptions attached to each path are what earn their
  place, so pruning the list itself would cost more than it saves.
- **Probe 2 candidates, rules with nothing enforcing them.** The
  `Rules that must hold (enforced)` section currently states that nothing is
  enforced, which is factual rather than aspirational, but a reviewer may still
  read the `Commit gate` line in `Run and test` as an unenforced rule. The lab
  expects such a rule to name a GitHub issue. None have been opened, because
  that writes to the public repository and has not been authorized.
- **Probe 3 candidates, unverifiable sentences.** `Unconfirmed means it does not
  exist` and `do not inflate` are phrased as judgments. Both are checkable
  against `skills-inventory.md` and the file list, but a reviewer may ask for the
  command form.

### Review of our file

The partner did not return a written review, so this is recorded as a
self-review of our own `AGENTS.md`, using the three probes. Three findings were
raised and all three were accepted and fixed.

| Probe | Finding | Fix applied |
| --- | --- | --- |
| 1, encyclopedia | `Course deliverable repository for the Mentalysis Agent.` is repository background, not an operating instruction | Opening line reduced to the operating instruction; the derivable description is gone |
| 2, wishful rule | `Commit gate: show git diff and wait for explicit approval before staging` had no hook or permission rule behind it | Rewritten as `run git diff and stop before staging. Enforced by: nothing automated; approval is manual.` |
| 3, unverifiable | `Unconfirmed means it does not exist.` has no verification criterion, and lack of confirmation does not establish absence | Rewritten as `Before adding a path or claim, confirm it exists by reading it. Omit anything you cannot confirm.` |

**Verdict: PASS.** A second read of the revised file found none of the three
problems.

Finding 2 is the same defect already listed in the self-review above, which
confirms the self-review was pointing at real material rather than at a
hypothetical. Finding 1 also removes the last derivable sentence from the file.

### Still outstanding

Nothing from the Chase.

## Ledger

The exit ticket asks for a ledger event recording the commit. There is no
`.gzkit` ledger in this repository, and `gz ledger` only exposes a merge driver
for an existing one, so no event can be appended without first scaffolding gzkit
governance.

Decision: do not scaffold. The commit is recorded here and in `AI_LOG.md`
instead, and the deviation is stated rather than implied. Creating a `.gzkit`
tree would also falsify the `AGENTS.md` line stating that this repository has no
hooks or permission rules, and would force another measurement pass for a
governance layer this documentation-only repo does not use.

## Remaining Work

Only the commit remains. The `board.md` convention from the `/init` specimen was
considered and not added. Budget was not the reason, since the file sits far
under 4000; it was judged non-essential for the map and is a better candidate
for the E5 extension, which adds skills for multi-step procedures.


