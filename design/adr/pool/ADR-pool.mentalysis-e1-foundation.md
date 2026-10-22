---
id: ADR-pool.mentalysis-e1-foundation
status: Pool
lane: lite
parent: PRD-MENTALYSIS-1.0.0
---

# ADR-pool.mentalysis-e1-foundation: Historical E1 conversion lineage

## Persona

Main-session: craftsperson, governance-aware, direct; preserve historical evidence without manufacturing completion.

## Intent

Retain the CLI demotion witness and parked historical children of the original foundation package. This is historical lineage, not a second active E1 implementation plan.

## Disposition

On 2026-10-18 the operator approved feature conversion: "go ahead and make the conversion". `gz adr demote` emitted the append-only rename from `ADR-0.0.1-mentalysis-e1-foundation` to this pool ID and parked `OBPI-0.0.1-01-preparation` and `OBPI-0.0.1-02-flight`. GHI 520 in the demotion event refers to upstream gzkit's Foundation Sunset anchor, not a newly filed project issue.

Active replacement: [ADR-0.1.0-mentalysis-e1](../pre-release/ADR-0.1.0-mentalysis-e1/ADR-0.1.0-mentalysis-e1.md), with `OBPI-0.1.0-01-preparation` and `OBPI-0.1.0-02-flight`. All implementation instructions and requirements reside in that package. Original brief prose was preserved and migrated to the replacement IDs.

The CLI's promote command would unpark the old IDs without renumbering them. Therefore replacement creation used `gz plan create` and `gz specify`; old children remain parked. No human-attested supersession, withdrawal, completion, or flight occurred. Pool status deliberately reflects ledger truth rather than falsely claiming an attested retirement. Do not promote this historical record as new work.
