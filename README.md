# Jeremiah-Jakpa

CIDM 6333 Agentic Systems course repository.

## Layers of truth

- **L1 (Source)**: Files in the repo (source code, configs, documentation) - e.g., `src/`, `opencode.json`, `AGENTS.md`, `pyproject.toml`
- **L2 (Ledger)**: Append-only runtime ledger at `var/ledger.jsonl` - records events like turn_budget, compaction, handoff_written, session_resumed
- **L3 (Derived/Runtime)**: Derived state, caches, and runtime artifacts - e.g., logs, compiled outputs, temporary state

**Precedence:** L2 > L1 > L3

When L3 disagrees with L2, the ledger (L2) is the source of truth and L3 state must be reconciled or discarded.
