# One-Page System Pitch

## Mentalysis Agent

### User and Problem

Mentalysis Agent is an educational DCF-assumption review assistant for finance students. Students often assemble growth, discount-rate, and terminal-value assumptions from spreadsheets, course materials, filings, and web sources, but they may miss mathematical conflicts, use evidence from the wrong period, or struggle to explain why an assumption is reasonable. Existing chat assistants can produce fluent answers without consistently checking calculations or showing reliable evidence. Mentalysis Agent would help a student examine assumptions, identify questions and inconsistencies, connect feedback to cited evidence, and revise the analysis. It would support learning and review rather than calculate a final investment recommendation or replace the student's judgment.

### Fit for the Course Framework

This problem is broad enough to exercise every layer named in the assignment. An **agent loop** can observe the submitted assumptions, decide what needs review, act through tools, and check the result. Different **patterns** can route deterministic calculations, evidence gathering, critique, and human approval. **Tools** can parse documents, run valuation checks, and retrieve approved sources, while **MCP** can provide standardized access to external data and document services. **Context** can hold the rubric, company, valuation date, and current task; **memory** can retain a project's assumptions, sources, revisions, and accepted decisions. A **multi-agent** design can eventually separate researcher, calculator, and reviewer roles when that separation improves reliability. **Evaluation** can measure calculation accuracy, citation support, consistency, helpfulness, and refusal behavior. **Deployment** can place the system behind a small web interface or API with authentication, logs, cost limits, and human checkpoints. These layers are useful rather than decorative because the task combines numerical rules, changing evidence, explanation, and accountable user decisions.

### Biggest Risk

The biggest risk is misleading guidance: the system could hallucinate a fact, rely on weak or outdated evidence, or present an uncertain judgment as authoritative and thereby distort a student's valuation. The design should therefore separate deterministic calculations from model-generated interpretation, attach citations and dates to factual claims, expose uncertainty, preserve an audit trail, and require the student to approve revisions. It should clearly state that it is an educational review tool, not a source of investment advice.

### PEAS Specification

| PEAS element | Mentalysis specification | Nine-component mapping |
| --- | --- | --- |
| **Performance measure** | Correct mathematical checks; claims supported by accessible, dated sources; useful explanations; consistent results; appropriate uncertainty and refusals; low cost and acceptable response time; student approval before changes are adopted. | **Evaluation and feedback**, because these criteria define how outputs are tested, scored, reviewed, and improved. |
| **Environment** | Student-entered assumptions, DCF spreadsheets, assignment rubrics, company filings, approved market sources, changing valuation dates, model and API limits, and a student working through a course project. | **Runtime and operations**, because this component manages the live application, integrations, availability, costs, logs, and operating constraints surrounding the agent. |
| **Actuators** | Ask clarifying questions, retrieve sources, parse documents, run deterministic checks, compare assumptions, produce cited feedback, suggest revisions, and request human approval. | **Tools and orchestration**, because these are the controlled actions and workflows the system uses to affect the task. |
| **Sensors** | Form inputs, spreadsheet values, uploaded text and tables, source metadata and dates, tool results, user corrections, approval decisions, and runtime errors. | **Perception**, because this component converts user, document, tool, and system signals into information the agent can reason about. |

The remaining components support the mapped PEAS elements: the foundation model generates and interprets language; planning and reasoning select review steps; memory and context preserve task state; coordination governs specialist roles; and governance and human interface communicate boundaries and keep the student in control.
