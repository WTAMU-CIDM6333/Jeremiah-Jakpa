# AI Interaction Log

Entries group consecutive prompts, responses, revisions, and commit confirmations by assignment step. Each entry records the meaningful decisions from that interaction rather than duplicating mechanical Git confirmations.

## 2026-09-20 - Repository Setup

- **Asked:** Requested step-by-step guidance on the eight-part assignment, followed by help creating a public `Evolution-0` repository and inferring its structure from the listed deliverables.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** The recommendation to create a public personal repository after receiving instructor authorization, clone it locally, and use a minimal structure because this satisfied the instructor's exception without inventing unsupported folders.
- **Modified:** The original organization-repository requirement was replaced with an instructor-authorized personal repository.
- **Rejected:** Creating a repository before instructor authorization or inventing additional project directories, because neither was supported by the assignment requirements.

## 2026-09-20 - Toolkit Check

- **Asked:** Requested help completing Step 2 by checking and preparing the required development toolkit.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** The existing Python, VS Code, Git, Ollama, and OpenCode installations; installation of `uv` 0.12.17 and `py-gzkit` 0.34.7; and `llama3.2:3b` because these met the toolkit requirements while fitting the computer's 8 GB of RAM.
- **Modified:** Added the `uv` tool directory to the user PATH because it was not available to the shell immediately after installation.
- **Rejected:** A larger local model, because the available 8 GB RAM and integrated graphics make a 3B model a more reliable baseline.

## 2026-09-20 - Route, Harness, and Framework Choices

- **Asked:** Requested guidance on Step 3 and selected a model-access route, primary harness, and provisional orchestration framework.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** Route A, OpenCode, and LangGraph because hosted models provide stronger primary capability, OpenCode is already operational, and LangGraph is a flexible provisional framework.
- **Modified:** Kept Ollama as a secondary option for local experiments and fallback access rather than the primary model route.
- **Rejected:** Route B because the computer's 8 GB RAM limits local model capability; alternative harnesses because OpenCode is already installed and in use; and immediate commitment to LangGraph because ADR-1 must compare alternatives in Evolution 2.

## 2026-09-20 - Skills Inventory

- **Asked:** Requested help constructing a skills inventory from beginner-level knowledge of SQL, HTML, Python, ML/AI, and GitHub, plus basic website projects and no API experience.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** A candid beginner-level inventory organized by skill area, with Mentalysis and Evolution-0 as accessible work samples, because it is accurate and provides links the instructor can open.
- **Modified:** Removed the final statement about the unlinked Project 1 website starter before committing because it was not needed as a work-sample entry without a public URL.
- **Rejected:** Unsupported claims of advanced proficiency or API experience, because the inventory should accurately represent current skills and learning needs.

## 2026-09-20 - One-Page System Pitch

- **Asked:** Requested guidance on Step 5 and selected Mentalysis Agent for finance students, with misleading guidance as its primary risk.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** An educational DCF-assumption review agent using evidence, deterministic checks, citations, uncertainty, and student approval because it extends prior work while providing enough depth for the course framework.
- **Modified:** Expanded the earlier Mentalysis website concept into an agentic system while preserving its educational scope and avoiding investment recommendations.
- **Rejected:** A general-purpose finance assistant and unsupported claims that the system can replace student judgment, because both would weaken the user focus and increase safety risk.

## 2026-09-20 - Design Analysis 1

- **Asked:** Requested guidance on Step 6, comparing a chat assistant with the selected agent harness across nine components and documenting the judgment loop.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** ChatGPT as the representative chat assistant, OpenCode as the harness, official product documentation as sources, and a compact comparison because they directly match the selected tools and assignment format.
- **Modified:** Used a table for the nine components so every required comparison remains explicit while the surrounding analysis stays near the requested length.
- **Rejected:** Treating tool access alone as evidence of a harness; the judgment instead emphasizes repository action, verification, permissions, and preserved human control.

## 2026-09-20 - Framework Board

- **Asked:** Requested guidance on Step 7 and supplied the course image titled `Agentic AI: A Complete Framework`.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** A Markdown transcription that checks boxes with concrete examples from systems already encountered and leaves unfamiliar topics unchecked because the board is intended to expose rather than conceal knowledge gaps.
- **Modified:** Consolidated the image's repeated Agent Management summary with cross-references to the detailed capability boxes while still representing all four summary items.
- **Rejected:** Filling every box with newly invented or unfamiliar examples, because that would hide the knowledge gaps the assignment intends to expose.

## 2026-09-20 - AI Log Audit

- **Asked:** Requested guidance on Step 8 and a final review of the root-level AI interaction log.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** The existing step-based chronology because it captures each meaningful assignment interaction, the model and harness, and the decisions made.
- **Modified:** Added explicit reasons for accepted decisions, corrected the Step 4 revision record, documented the grouping convention, and added this audit entry so the log matches the rubric.
- **Rejected:** Separate entries for mechanical commit and push confirmations because they introduced no new generated content or substantive decision and are already grouped with their corresponding steps.
