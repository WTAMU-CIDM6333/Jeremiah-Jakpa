# E1 design analysis — ReAct and OpenCode's loop

Date: 2026-10-18. System: Mentalysis Agent.

Sources checked: [ReAct project and paper summary](https://react-lm.github.io/)
and [OpenCode agents, especially Max steps](https://opencode.ai/docs/agents/).
ReAct is a reasoning/action method; OpenCode is an execution harness. This
comparison concerns what Mentalysis would need to supply around either choice.

| Component | ReAct-based implementation | OpenCode E1 |
| --- | --- | --- |
| Foundation | Developer selects an LLM and prompts reasoning/action trajectories. | Agent selects `opencode/big-pickle`; harness connects the provider. |
| Perception | Developer integrates observations from APIs or environments. | Prompt plus repository read-tool results enter the session. |
| Planning and reasoning | Interleaved reasoning, actions, and observations revise the approach. | Model chooses actions in the harness loop; steps: 5 bounds iterations. |
| Tools and orchestration | Developer supplies dispatch and result handling. | Harness supplies tool dispatch; E1 defines a single primary agent. |
| Memory and context | Developer chooses trajectory storage and context policy. | Harness maintains sessions; no project long-term memory is implemented. |
| Coordination | ReAct alone does not require a multi-agent topology. | E1 is single-agent; E2 will explicitly choose coordination. |
| Evaluation and feedback | Task/environment outcomes evaluate trajectories. | Synthetic numerical oracle plus exported iterations and Chase review. |
| Governance and human interface | Method itself does not supply this course's approval process. | Chase-signed card and PRD attestation are procedural; step budgeting is a harness setting. |
| Runtime and operations | Developer owns retry, stop, persistence, and model integration code. | OpenCode owns these facilities; pinned version and exports identify the tested substrate. |

## Judgment loop

**Decision:** use OpenCode's loop, with our agent and an explicit iteration budget.
**Privileged characteristics:** observable tool use, bounded execution, and a
repeatable comparison between a small calculation and an unfinished review.
**Cost:** dependence on harness counting, provider behavior, inherited settings,
and export visibility rather than full control over the execution algorithm.
**Failure mode:** an early voluntary answer looks like a successful budget halt,
or batching fits the whole task into fewer iterations than intended.
**Preservation:** pre-register sequential reads, freeze configuration, count actual
export records, distinguish tools from iterations, and fail the claim when the
halt mechanism is not visible. **Feedback:** Chase reviews evidence; a failed
claim drives a revised card and new approval, never edited evidence.

The documentation describes intended `steps` behavior; no E1 export yet verifies
it for this installed version and model. ReAct's published benchmark results do
not establish Mentalysis accuracy.
