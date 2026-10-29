# E2 design analysis — LangGraph and OpenCode orchestration

Date: 2026-10-25. System: Mentalysis. Status: design/preparation, not flown.
Decision: [ADR-1](../docs/adr/ADR-1.md).

| Component | LangGraph | Mentalysis on OpenCode |
| --- | --- | --- |
| Foundation | Python graph/state APIs plus chosen model integration. | OpenCode runtime plus named Big Pickle agents. |
| Perception | Nodes consume typed/application-defined state and observations. | Primary receives the bounded question; workers receive explicit task payloads. |
| Planning and reasoning | Edges and routing functions can enforce stage reachability. | Primary is prompted to await calculation before assumptions; order is observed, not guaranteed. |
| Tools and orchestration | Nodes, conditional edges, and Send support worker coordination. | Task invokes two permitted subagents; wildcard deny excludes all other names. |
| Memory and context | State/checkpoint mechanisms can retain workflow progress. | Sessions/child sessions retain run evidence; no product-level long-term memory added. |
| Coordination | Application owns shared state, branching, and joins. | Primary owns a sequential handoff and final synthesis; workers cannot delegate. |
| Evaluation and feedback | Node/unit tests can check transitions and typed state. | Numerical oracle, exported task order, frozen deny rule plus non-execution evidence, and Chase review. |
| Governance and human interface | Application integrates approval policy; graph correctness is distinct from permission policy. | Task permission rules enforce allowed delegates; Chase GO is a separate procedural requirement. |
| Runtime and operations | Developer owns graph deployment, provider setup, and persistence configuration. | Harness owns execution; agent budgets are per agent and version/model IDs identify the substrate. |

## Judgment loop

**Decision:** keep the required OpenCode substrate and use orchestrator–workers.
**Privileged characteristics:** attributable work, explicit handoff, and a named
delegation boundary with low implementation overhead for this educational slice.
**Cost:** prompted order and text field conventions instead of code-enforced
edges and validated typed worker outputs; extra latency and correlated errors.
**Failure mode:** the primary answers correctly without workers, or a probe
omission/refusal is read as enforcement without the frozen deny rule and
confirmed non-execution.
**Preservation:** pre-register two tests; require actual ordered Task records,
child-session linkage, and payload handoff. For the boundary, require the frozen
deny-rule snapshot plus no probe child session and no marker, with either no
attempt or a runtime-rejected attempt. Keep original sanitized exports; a bare
refusal remains insufficient evidence.
**Feedback and revision:** Chase compares observations to the card and falsifiers.
An ordering failure motivates a new approved card or a future code-controlled
workflow; it never authorizes editing a trace or expanding an allowlist midflight.

## Sources and limits

- [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
  describes graph edges, shared state, and orchestrator-worker coordination.
- [OpenCode agents](https://opencode.ai/docs/agents/#task-permissions) describes
  named Task permissions, rule precedence, and denied-target visibility.

Sources checked 2026-10-25. No benchmark, successful flight, or independent-model
agreement is claimed. E1 remains deferred because the Chase is unavailable.
