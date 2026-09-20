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
