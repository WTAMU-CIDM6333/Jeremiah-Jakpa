# E3 evidence

This directory holds the sanitized evidence from the E3 sortie. The flight ran on
2026-11-01 and 2026-11-02 after the AI-authored GO. All four test points were
INCONCLUSIVE because the local model made no tool call; no canonical `tpN-parent`
export was produced. The runs are preserved under `superseded/`.

## Rules

- Evidence is `opencode export <sessionID> --sanitize` output, captured as
  written. Never commit a raw export and never hand-edit a sanitized one.
- Record each file's SHA-256 in `../flight-log.md` and in the commit message or
  log entry that adds it.
- `.gitattributes` marks `evolution-03/evidence/**` as `-text` so the committed
  bytes match the recorded SHA-256. The captures keep the Windows CRLF endings
  they were written with, so `git diff --check` reports those lines as trailing
  whitespace. That is expected; do not rewrite the evidence to silence it.
- If a sanitized export still contains a secret, stop publication. Do not edit
  the file to remove it.
- Capture `git status --short` before TP1 and after each test; record the output
  in the log, not as an invented claim.
- The JSON stream printed by `opencode run --format json` is a working aid. The
  committed evidence is the sanitized export.
- `--sanitize` preserves the session id, agent, model, tool name, tool status,
  and error text, but redacts tool input/output, message text, title, and
  directory. Observed on the pre-flight probe exports and confirmed on these
  flight exports. The TP1 marker and the TP2 target path therefore belong in the
  flight log, not the sanitized export.

## Files

- `preflight-agent.txt` — `opencode debug agent mentalysis-e3`, captured before
  TP1 at commit `663d7a1`.
- `preflight-config.txt` — `opencode debug config`, captured before TP1 at commit
  `663d7a1`. Scanned for credential strings; none found.
- `superseded/` — the six sanitized exports from the frozen flight and its
  instrumentation checks, each recorded in `../flight-log.md` with its session
  id, SHA-256, and verdict. None of them contains a tool part.

A missing file is recorded as missing. It is never replaced with a summary or a
reconstruction.

## Why there is no canonical tpN export

The card defines `tpN-parent.sanitized.json` as the export of a test point that
produced the required tool or permission record. No frozen-flight session
produced such a record: the model emitted pseudo-calls as text in every case.
Committing those exports under the canonical names would imply a test point ran
as designed. They are kept under `superseded/` instead, and the log states the
INCONCLUSIVE verdict for each.
