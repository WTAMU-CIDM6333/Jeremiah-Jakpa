# AI Interaction Log

## 2026-09-20 - Repository Setup

- **Asked:** Requested step-by-step guidance on the eight-part assignment, followed by help creating a public `Evolution-0` repository and inferring its structure from the listed deliverables.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode.
- **Accepted:** The recommendation to create a public personal repository after receiving instructor authorization, clone it locally, and use a minimal structure based on the assignment's named files.
- **Modified:** The original organization-repository requirement was replaced with an instructor-authorized personal repository.
- **Rejected:** Creating a repository before instructor authorization or inventing additional project directories, because neither was supported by the assignment requirements.

## 2026-09-20 - Toolkit Check

- **Asked:** Requested help completing Step 2 by checking and preparing the required development toolkit.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** The existing Python, VS Code, Git, Ollama, and OpenCode installations; installation of `uv` 0.12.17 and `py-gzkit` 0.34.7; and `llama3.2:3b` as a compact local Ollama model suitable for the computer's 8 GB of RAM.
- **Modified:** Added the `uv` tool directory to the user PATH because it was not available to the shell immediately after installation.
- **Rejected:** A larger local model, because the available 8 GB RAM and integrated graphics make a 3B model a more reliable baseline.

## 2026-09-20 - Route, Harness, and Framework Choices

- **Asked:** Requested guidance on Step 3 and selected a model-access route, primary harness, and provisional orchestration framework.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** Route A, OpenCode, and LangGraph as the three choices documented in `choices.md`.
- **Modified:** Kept Ollama as a secondary option for local experiments and fallback access rather than the primary model route.
- **Rejected:** Route B because the computer's 8 GB RAM limits local model capability; alternative harnesses because OpenCode is already installed and in use; and immediate commitment to LangGraph because ADR-1 must compare alternatives in Evolution 2.

## 2026-09-20 - Skills Inventory

- **Asked:** Requested help constructing a skills inventory from beginner-level knowledge of SQL, HTML, Python, ML/AI, and GitHub, plus basic website projects and no API experience.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** A candid beginner-level inventory organized by skill area, with Mentalysis and Evolution-0 as accessible work samples.
- **Modified:** Described the Project 1 website starter without a link because no public URL was available.
- **Rejected:** Unsupported claims of advanced proficiency or API experience, because the inventory should accurately represent current skills and learning needs.
