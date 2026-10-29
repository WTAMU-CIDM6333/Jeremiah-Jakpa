# E2 — Mentalysis orchestrator–workers

Status: CHASE GO RECORDED (AI-authored); NOT FLOWN. E1 Chase review is deferred
because the partner is unavailable. The operator authorized E2 preparation as a
sequencing deviation; E1 completion and instructor approval are not implied.
The preparation substrate was frozen on 2026-10-29 (OpenCode `1.18.21`,
`opencode/big-pickle`, resolved agent/task rules, Windows 11 / PowerShell 5.1).
The GO was returned by an AI reviewer, not a human; the operator's position is
that this satisfies the assignment's Chase requirement.

## What is built

`mentalysis-e2` calls `mentalysis-calculation`, waits, calls
`mentalysis-assumptions` with the result, then synthesizes the answer.
`permission.task` allows only those two names. The registered
`mentalysis-e2-probe` is a denied negative control; it must never execute from
the E2 primary. [ADR-1](../docs/adr/ADR-1.md) compares OpenCode with LangGraph and
Pydantic AI and names the limits of prompt-directed sequencing.

This pattern uses agent files; custom commands are not required for this branch
of the assignment. The project default still selects the E1 `mentalysis` agent.
Select `mentalysis-e2` explicitly for E2, and quit/restart OpenCode after adding
or changing agent files so configuration reloads.

## Preparation and review

1. Review `docs/adr/ADR-1.md`, all four E2 agent files, the analysis, and card.
2. Inspect `opencode debug agent mentalysis-e2` locally: mode, model, five steps,
   and effective Task rules. Inspect each worker/probe to establish it exists.
   Do not publish raw configuration containing inherited credentials.
3. Validate authored briefs under `ADR-0.2.0`. Configuration loading and document
   validation are not demonstrations of model behavior.
4. Commit preparation and record ledger events when publication is authorized.
   The card's version, model-listing, resolved-agent, host, and effective-config
   fields are filled from the 2026-10-29 preflight. The preparation commit SHA is
   recorded in the follow-up card-freeze commit; no SHA is invented here.
5. Obtain a committed dated GO on the completed card before any execution. The
   recorded GO is AI-authored, not a human signature.
6. Run TP1 and TP2 in fresh sessions using the exact prompts on the card;
   export the actual parent and required child sessions with `--sanitize`.
7. Fill the log with actual evidence and PASS/FAIL/ABORT, then obtain CHASE review.

For TP2, do not use direct `@` invocation. OpenCode documents that users may
directly invoke subagents independently of a primary's Task restrictions. It
also documents that a target denied by `permission.task` is removed from the
Task tool description, so a compliant primary may make no attempt at all. TP2
PASS therefore needs three things: the frozen preflight showing the probe is a
real subagent while the primary's task rules deny it; confirmed non-execution
(no probe child session, no successful probe Task record, no
`E2_DENIED_DELEGATE_EXECUTED` marker); and either no attempt or an attempted
call rejected by the runtime. A bare textual refusal without that configuration
and non-execution evidence is inconclusive, not PASS.

## Returning to E1

E1's agent file and `opencode.json` are unchanged, but adding agents changes
discovery. Revisit E1 from its frozen preparation baseline in a separate
checkout/worktree and recheck its effective configuration before GO/flight.
Do not reset this working tree or discard E2 work to recover E1.
