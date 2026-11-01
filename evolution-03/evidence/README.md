# E3 evidence

This directory holds sanitized evidence from the E3 sortie. It is empty until a
GO-authorized flight runs. Do not create placeholder exports.

## Rules

- Evidence is `opencode export <sessionID> --sanitize` output, captured as
  written. Never commit a raw export and never hand-edit a sanitized one.
- Record each file's SHA-256 in `../flight-log.md` and in the commit message or
  log entry that adds it.
- If a sanitized export still contains a secret, stop publication. Do not edit
  the file to remove it.
- Capture `git status --short` before TP1 and after each test; record the output
  in the log, not as an invented claim.
- The JSON stream printed by `opencode run --format json` is a working aid. The
  committed evidence is the sanitized export.

## Expected files after flight

- `preflight-agent.txt` — `opencode debug agent mentalysis-e3`.
- `preflight-config.txt` — `opencode debug config`.
- `tp1-parent.sanitized.json` — TP1 session export.
- `tp2-parent.sanitized.json` — TP2 session export.
- `tp3-parent.sanitized.json` — TP3 session export.
- `tp4-parent.sanitized.json` — TP4 session export.

A missing file is recorded as missing. It is never replaced with a summary or a
reconstruction.
