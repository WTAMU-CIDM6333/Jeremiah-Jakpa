# Mentalysis Agent — Product Requirements

Date: 2026-10-18
Status: Product requirements approved by Jeremiah Jakpa on 2026-10-21; flight acceptance pending
Governance registration: [PRD-MENTALYSIS-1.0.0](../design/prd/PRD-MENTALYSIS-1.0.0.md)

## User and problem

Finance students need to explain and check discounted cash flow assumptions.
Growth, discount-rate, and terminal-value inputs can conflict mathematically,
and fluent model prose can hide missing evidence. Mentalysis helps a student
review assumptions, distinguish calculations from judgment, and identify what
still needs verification. This continues [the Evolution 0 pitch](../evolution-00/pitch.md).

## E1 scope

OpenCode supplies the execution loop, tools, and model connection. The project
supplies `.opencode/agents/mentalysis.md`, a primary educational review agent
using `opencode/big-pickle` with `steps: 5`. Inputs for E1 are synthetic and
contain no account data, credentials, or real investment decisions.

The agent answers a bounded DCF question and reports partial progress when
OpenCode's iteration budget prevents completing a larger review. The five-step
setting is an iteration budget, not a promise of five tool calls or a wall-clock
timeout. E1 does not claim a deterministic valuation engine exists.

## Acceptance criteria

| ID | Criterion | Evidence |
| --- | --- | --- |
| E1-AC1 | Primary agent declares description, mode, model, and steps: 5; OpenCode loads it. | Committed agent and preflight inspection |
| E1-AC2 | TP1 answers TV = 100 / (0.10 - 0.03) = 1428.57 in the same currency units, conditional on constant perpetual growth and WACC > g; fewer than five iterations. | Sanitized TP1 session export |
| E1-AC3 | TP2 leaves review work unfinished, reaches the configured iteration boundary, and ends with text only, with no further tool calls. | Sanitized TP2 session export with counted iteration records |
| E1-AC4 | Chase GO is committed before flight; card/config remain fixed; log names evidence, counts, and verdict. | Git history, card, log, sanitized exports |
| E1-AC5 | E1 design analysis compares ReAct with OpenCode across nine components and includes a judgment loop. | Design analysis and ledger row |

## Product boundaries and later layers

The student retains judgment and approval over adopted assumptions. Generated
explanations are not evidence of successful execution. E2 will define a workflow
pattern and ADR-1; E3 will test local-model permission gates; E4 will add the
project's MCP server and second client. Those layers require their own plans,
briefs, cards, and evidence after E1.

## Attestation

> I have reviewed and approve the Mentalysis PRD’s user, problem, scope, and acceptance criteria, And authorize a commit and push

— Jeremiah Jakpa — 2026-10-21, supplied in the operator conversation.

This attests the product requirements and authorizes publication of preparation.
It does not attest observed flight results or substitute for the Chase's GO.
