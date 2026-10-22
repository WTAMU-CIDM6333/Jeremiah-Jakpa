# GitHub Copilot Instructions

Instructions for GitHub Copilot when working with Jeremiah-Jakpa.

## Project Context

A gzkit-governed project

## Canonical Contract

`AGENTS.md` is the source of truth for governance behavior.

If these instructions drift from `AGENTS.md`, follow `AGENTS.md` and run `gz agent sync control-surfaces`.

## Tech Stack

Python 3.13+ with uv, ruff, ty

## Conventions

Ruff defaults: 4-space indent, 100-char lines, double quotes

## Quality Requirements

Before suggesting code:

1. Follow existing patterns in the codebase
2. Include type annotations for all public functions
3. Write tests for new functionality
4. Follow the invariants defined in governance docs

## Governance

This project uses gzkit for governance. Key commands:

- `gz status` - Check what gates are pending
- `gz validate --documents` - Validate governance artifacts
- `gz check` - Run all quality checks

## OBPI Acceptance

Follow the OBPI Acceptance Protocol defined in `AGENTS.md`. Key rule: use
`uv run gz obpi pipeline <OBPI-ID>` after plan approval; never implement
freeform. Human attestation is required at the brief level whenever the
parent ADR is `heavy`-lane OR `foundation`-kind (either axis alone triggers
it — a `lite`-lane foundation OBPI is NOT self-closeable). `kind` and
`lane` are orthogonal axes (see AGENTS.md § Kinds and § Lane & Kind
Attestation Matrix). A TTY + `ATTEST` confirmation gate prevents agent
subprocesses from synthesizing attestation payloads (GHI #290).

## Skills

Use the canonical skill catalog and keep mirrors synced via `gz agent sync control-surfaces`:

- Canonical skills: `.gzkit/skills`
- Claude skill mirror: `.claude/skills`
- Codex skill mirror: `.agents/skills`
- Copilot skill mirror: `.github/skills`

### Available Skills

See `AGENTS.md` § Available Skills for the complete skill catalog.

## Build Commands

```bash
uv sync                              # Hydrate environment
uv run -m JeremiahJakpa --help            # CLI entry point
uv run gz lint                       # Lint
uv run gz format                     # Format
uv run gz typecheck                  # Type check
uv run gz test                       # Run tests
```

## Key Files

- `AGENTS.md` - Universal agent contract
- `.gzkit/manifest.json` - Governance manifest
- `.gzkit/ledger.jsonl` - Event ledger

---

<!-- BEGIN agents.local.md -->

<!-- END agents.local.md -->
