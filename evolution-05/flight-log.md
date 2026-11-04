# E5 — Sortie 5 flight log

Pilot: Jeremiah Jakpa | Chase: AI reviewer (Big Pickle), not a human  
Date: 2026-11-04  
Card: [flight-card.md](flight-card.md) — GO recorded 2026-11-04 11:00 CDT (UTC−05:00) before first log entry

## PRE-FLIGHT
- [x] Card committed and signed (GO dated before first log entry)
- [x] Adversarial client named: evolution-05/adversarial_client.py
- [x] pin.py created at src/flights/pin.py
- [x] tool-pins.json generated

## TP0 — Preparation
- Card committed: evolution-05/flight-card.md
- GO: 2026-11-04 11:00 CDT (UTC−05:00) (AI reviewer, not human)
- pin.py executed before sortie: `uv run python -m src.flights.pin` → exit 0, pinned 3 tools
Evidence: tool-pins.json, src/flights/pin.py

## TP1 — Scope enforcement (token-based)
- Read token gets 403 insufficient_scope on write tool before function runs: **PASS**
  - Evidence: tests/test_scope_enforcement.py::test_read_token_insufficient_scope_on_write
- Token with wrong audience gets 401: **PASS**
  - Evidence: tests/test_scope_enforcement.py::test_wrong_audience_gets_401
- Scope claimed in body/header/argument changes nothing: **PASS**
  - Evidence: tests/test_scope_enforcement.py::test_scope_in_args_does_not_change_authorization
- Each refusal writes log line with sub and tool: **PASS**
  - Evidence: src/flights/server.log (refusal entries with sub and tool)

## TP2 — Scope table completeness
- Every tool mapped in scopes.py table: **PASS** (get_flights, list_tools_info, add_flight all mapped)
- Tool not in table is refused: **PASS**
  - Evidence: tests/test_scope_enforcement.py::test_tool_not_in_table_refused
- Check and scope docs read the table: **PASS** (server.py imports from scopes.py, uses TOOL_SCOPES)

Evidence: src/flights/scopes.py

## TP3 — Tool pinning
- tool-pins.json committed: **PASS**
- pin.py exits 0 on committed server: **PASS** (exit code 0)
- Log shows pin.py ran before sortie: **PASS** (executed during preparation)

Evidence: tool-pins.json, src/flights/pin.py

## TP4 — Adversarial write attempt blocked
- Adversarial client cannot cause write via poisoned resource or scope escalation: **PASS**
  - Adversarial client tests all passed (see evolution-05/adversarial_client.py output)

Evidence: evolution-05/adversarial_client.py

## VERDICT
**PASS** — All test points satisfied. Server hardened with token-based scope verification, scope table enforced, tool descriptions pinned, adversarial attacks blocked.
