# Route, Harness, and Candidate Framework

## Model-Access Route: A

I will use Route A: a model subscription supported by a small API budget. This route gives me access to stronger hosted models for demanding reasoning and implementation tasks while keeping API spending controlled through deliberate model selection, short experiments, and usage monitoring. It is more practical for my current computer, which has 8 GB of RAM and integrated graphics and therefore runs only relatively small local models comfortably. I will retain Ollama and `llama3.2:3b` for local experiments, fallback access, and comparisons, but local inference will not be my primary route.

## Primary Harness: OpenCode

I selected OpenCode as my primary harness because it provides an agent-oriented workflow around the model rather than only a chat interface. It can inspect the repository, edit files, run terminal commands, use specialized tools, and verify results while keeping the work visible through Git. I have already installed and used OpenCode 1.18.21 to establish this repository and complete the toolkit check, so this choice avoids unnecessary switching costs and gives me a working environment for iterative development, evaluation, and human approval.

## Candidate Orchestration Framework: LangGraph

My provisional orchestration-framework choice is LangGraph. Its graph-based model makes agent state, control flow, branching, retries, tool use, persistence, and human-in-the-loop checkpoints explicit, which should support a system that must eventually address the assignment's loop, context, memory, multi-agent, evaluation, and deployment layers. The tradeoff is additional design complexity compared with a simpler agent library, so I will treat LangGraph as a candidate rather than a final commitment. ADR-1 in Evolution 2 will compare it with credible alternatives before formalizing the framework decision.
