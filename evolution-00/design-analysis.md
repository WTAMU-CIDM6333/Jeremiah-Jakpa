# Design Analysis 1

**Subject:** ChatGPT versus OpenCode

**Sources read:** [ChatGPT Capabilities Overview](https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview); OpenCode documentation for [introduction](https://opencode.ai/docs/), [tools](https://opencode.ai/docs/tools/), [agents](https://opencode.ai/docs/agents/), and [permissions](https://opencode.ai/docs/permissions/).

| Component | ChatGPT | OpenCode |
| --- | --- | --- |
| Foundation | Hosted selectable models | Provider-selected models |
| Perception | Prompts and uploads | Prompts, repository, tool results |
| Planning and reasoning | Dialogue and research | Iterative plan-act-check loop |
| Tools and orchestration | Hosted tools | Shell, files, web, MCP |
| Memory and context | Chats, memory, projects | Sessions, instructions, compaction |
| Coordination | User-assistant interaction | Primary agents and subagents |
| Evaluation and feedback | User review | Diffs, tests, user review |
| Governance and human interface | Chat controls | Plan mode and permissions |
| Runtime and operations | Hosted application | Local TUI, IDE, CLI, server |

OpenCode was built because coding requires inspecting artifacts, acting, and checking results, not only advice. This privileges actionability, local context, repeatability, and evidence, but costs setup, permission management, tokens, and side-effect exposure. A plausible but wrong edit is the central failure. Plan mode, approvals, diffs, tests, Git history, and human review preserve control.

**Judgment loop:** **Decision:** use the harness. **Characteristics privileged:** action, evidence, repeatability. **Cost:** complexity and side effects. **Failure mode:** wrong changes. **Preservation:** permissions, tests, Git, human approval.
