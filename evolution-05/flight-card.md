# E5 — Sprint 5 flight card

Status: PRE-FLIGHT — GO pending. Signed after card commit, before first log entry.
Prepared: 2026-11-04. Pilot: Jeremiah Jakpa. Chase: AI reviewer (Big Pickle), not a human.

## ENVELOPE

One sortie testing MCP server hardening. One client is hostile/adversarial. The sortie verifies scope enforcement via verified tokens, tool description pinning, and AGENTS.md re-measurement. Do not fly without this card's committed dated Chase GO.

## DESIGN CLAIM

An adversarial client cannot exceed the server's declared scope. A poisoned resource cannot cause a write. All scope checks derive from a single scope table. Tool descriptions are pinned and verified by pin.py. Refusals (401/403) are logged with sub and tool.

## SYSTEMS UNDER TEST

- `src/flights/` — hardened MCP server with token verification, scope enforcement
- `src/flights/scopes.py` — scope table mapping every tool to required scopes
- `tool-pins.json` and `src/flights/pin.py` — tool description pinning
- Tests proving scope enforcement
- Adversarial client (named below)
- AGENTS.md and skills under `.opencode/skills/` / governance surfaces

## SUBSTRATE

- Repository: https://github.com/WTAMU-CIDM6333/Jeremiah-Jakpa
- Base (E4): commits f523122, d94bfd3
- OpenCode: `1.18.21`
- Model: `opencode/big-pickle`
- Host: Windows 11, PowerShell 5.1, Git, uv, Python 3.13+

## ADVERSARIAL CLIENT

Named: `evolution-05/adversarial_client.py` — attempts to call write tools with insufficient/wrong-scope tokens, inject scope via body/header/argument, and access poisoned resources.

## TEST POINTS

### TP0 — Preparation checks
- [ ] Flight card committed
- [ ] Chase GO obtained and dated before first log entry
- [ ] pin.py runs and exits 0 on committed server

### TP1 — Scope enforcement (token-based)
- Read token gets 403 insufficient_scope on write tool before function runs
- Token with wrong audience gets 401
- Scope claimed in body/header/argument changes nothing
- Each refusal writes log line with sub and tool

### TP2 — Scope table completeness
- Every tool mapped in scopes.py table
- Tool not in table is refused
- Check and scope docs read the table

### TP3 — Tool pinning
- tool-pins.json committed
- pin.py exits 0 on committed server
- Log shows pin.py ran before sortie

### TP4 — Adversarial write attempt blocked
- Adversarial client cannot cause write via poisoned resource or scope escalation
- Server refuses with appropriate error

## INSTRUMENTATION

- All events logged with timestamps
- Refusals logged with sub and tool
- pin.py execution logged
- Adversarial client actions logged
- Evidence paths recorded in flight-log.md

## PRE-REGISTERED FALSIFIERS

1. Write executes despite insufficient scope / wrong audience
2. Scope from body/header/argument is accepted
3. Tool not in table allowed or check bypasses table
4. pin.py not run or fails
5. Refusal not logged with sub and tool

## CHASE GO

> GO — AI reviewer (Big Pickle), not a human — 2026-11-04 11:00 CDT (UTC−05:00)

- Applies to evolution-05 preparation package
- AI-authored, not a human signature
- GO dated before first log entry
