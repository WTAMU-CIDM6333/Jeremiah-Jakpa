# E5 design analysis — MCP server hardening with token-based scopes

Date: 2026-11-04. System: Flights MCP Server (hardened).

## Why (paragraph)

E4 connected two friendly clients to an MCP server with read/write tools. E5 hardens the server against adversarial clients by enforcing scope checks based solely on verified tokens, pinning tool descriptions, and requiring that scope claims in body/header/args cannot escalate privileges. The design treats scope as a property of verified tokens (not client-supplied claims), fails closed (tools not in table refused), and logs all refusals with subject and tool for auditability.

## Nine components

| Component | Adversarial threat | E5 hardened design |
|---|---|---|
| Foundation | Untrusted clients can claim arbitrary permissions | Token-based auth with signed tokens, verified by server; audience checked (401 on wrong audience) |
| Perception | Clients inject scope via headers/body/args | Scope comes ONLY from verified token payload; claims in args/headers/body ignored |
| Planning and reasoning | Client tries to discover and exploit tool surface | Every tool mapped in single scope table (scopes.py); tools not in table refused before execution |
| Tools and orchestration | Write tool callable without write scope | Authorization checked BEFORE function runs; read token gets 403 insufficient_scope on write tool |
| Memory and context | No audit trail of attempts | All refusals and calls logged with sub and tool; log entries include timestamps |
| Coordination | Multiple clients (friendly + adversarial) need different treatment | Same server enforces same rules for all clients; adversarial client tested against server |
| Evaluation and feedback | No verification of security properties | Tests prove 401/403 cases, scope injection ignored, table completeness; adversarial client validates all cases |
| Governance and human interface | Tool descriptions can drift/be poisoned | Tool descriptions pinned in tool-pins.json; pin.py verifies on committed server; run before sortie |
| Runtime and operations | Configuration drift or tampered server | pin.py exits 0 on committed server; evidence logged; flight card requires GO before first log entry |

## Judgment loop

**Decision:** Enforce token-based scopes from verified tokens only, fail closed, pin tool descriptions, log all refusals with sub and tool.

**Privileged characteristics:** Single source of truth (scope table), check-before-execution, impossible to escalate via client-supplied scope claims, auditable refusals.

**Cost:** Added complexity (token verification), requires clients to obtain valid tokens, logging overhead.

**Failure mode:** If scope check is bypassed or token verification broken, adversary could write without permission. Scope claims in args could be accepted if not properly ignored.

**Preservation:** Scope table is single source of truth read by check; tests verify 401 (wrong audience), 403 (insufficient scope) before function runs; adversarial client confirms scope injection ignored; tool not in table refused; every refusal logs sub and tool. pin.py verifies pins before sortie.

**Feedback:** Tests and adversarial client provide concrete evidence; any bypass would fail tests/falsifiers recorded in flight log.
