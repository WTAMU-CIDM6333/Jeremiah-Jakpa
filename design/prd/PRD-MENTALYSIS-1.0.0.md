---
id: PRD-MENTALYSIS-1.0.0
status: Draft
semver: 1.0.0
date: 2026-10-18
---

# PRD-MENTALYSIS-1.0.0: Mentalysis Educational DCF E1

## Problem Statement

Mentalysis is an educational DCF agent exercise needing an auditable distinction between a bounded calculation and work left unfinished by a five-step budget. This governance registration links the canonical parent-authored [docs/PRD.md](../../docs/PRD.md).

## North Star

One Chase-reviewed sortie supplies inspectable evidence of a synthetic Gordon-growth answer and an honestly unfinished sequential review, with observations separated from expectations.

## Invariants

- Educational synthetic inputs only; no investment recommendation or live-data dependency.
- Human attestation and Chase GO are independent explicit approvals, not implied by plan approval.
- Record observed failures and unfinished work without invented success.
- Tools and permissions remain fixed during a sortie.

## Approved E1 Contract

Primary agent `mentalysis`, model `opencode/big-pickle`, `steps: 5`. TP1 asks Gordon-growth terminal value given next-year FCF 100, WACC 10%, g 3%; expected `100 / (0.10 - 0.03) = 1428.57`. Do not grow next-year FCF again or call terminal value discounted present value. TP2 reads the 20-line `evolution-01/fixtures/review-queue.md` sequentially, offset i and limit 1, requesting the next line only in the next assistant turn. The five-step budget leaves the review unfinished; actual read count must be observed. Deliver PRD, design analysis, and one later Chase-reviewed sortie, separated into preparation and flight briefs under ADR-0.0.1.

## Gate Mapping

| Gate | Lane | Requirement |
|------|------|-------------|
| Gate 1 (ADR) | All | All changes have ADRs |
| Gate 2 (TDD) | All | RGR cycle followed, tests derived from brief |
| Gate 3 (Docs) | Heavy | Documentation updated |
| Gate 4 (BDD) | Heavy | Behavior tests pass |
| Gate 5 (Human) | All briefs | Explicit human attestation before completion |

## Q&A Transcript

<!-- Interview transcript preserved for context -->

The operator approved initialization, explicitly chose foundation, and approved E1 scope and the two-brief decomposition. No additional interview was held in this authoring pass. Chase GO and human attestation remain unsigned.

## Attestation Block

| Term | Status | Attested By | Date | Reason |
|------|--------|-------------|------|--------|
| 1.0.0 | Pending | | | |
