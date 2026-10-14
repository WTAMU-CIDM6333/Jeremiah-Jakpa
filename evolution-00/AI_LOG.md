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

## 2026-09-29 - AGENTS.md Lab Setup

- **Asked:** Requested a simplified action plan for the `AGENTS.md` budget lab, completed the initial setup checks, and asked that the selected model deviation be recorded.
- **Model and harness:** `openai/gpt-5.6-sol` through OpenCode 1.18.21.
- **Accepted:** Continuing the exercise with GPT Sol because it is the user's chosen working model and can perform the same measurement procedure.
- **Modified:** Replaced the lab-specified `opencode/big-pickle` model with `openai/gpt-5.6-sol` and documented that the resulting token counts may not be directly comparable with the class baseline.
- **Rejected:** Muse Spark after briefly considering it, because the user decided to continue with GPT Sol instead.

## 2026-09-29 - AGENTS.md Lab Model Switch

- **Asked:** Reported that Big Pickle had been activated and asked to rewrite the Step 1 record using it.
- **Model and harness:** `opencode/big-pickle` through OpenCode 1.18.21.
- **Accepted:** Re-recording the measurement setup for `opencode/big-pickle` because it matches the lab specification and keeps the token comparison valid against the class baseline.
- **Modified:** Replaced the GPT Sol model entry in the measurement setup table and removed the documented model deviation.
- **Rejected:** Keeping the GPT Sol measurement baseline, because its token counts would not be comparable with classmates using Big Pickle.

## 2026-09-29 - AGENTS.md Lab Inventory

- **Asked:** Asked to proceed to the inventory step before drafting `AGENTS.md`.
- **Model and harness:** `opencode/big-pickle` through OpenCode 1.18.21.
- **Accepted:** Deriving the inventory only from `AI_LOG.md`, the commit history, and observable corrections in this session, because the lab forbids drafting from assumptions.
- **Modified:** Replaced the lab template's example truth paths with the paths that actually exist, and documented the absent control surfaces after verifying them against the repository.
- **Rejected:** The template commands `uv sync`, `uv run pytest -q`, and `gz status` plus the `docs/prd.md`, `docs/adr/`, and flight-card paths, because this repository is documentation only and contains none of them.

## 2026-09-29 - AGENTS.md Draft and Measurement

- **Asked:** Asked to draft `AGENTS.md`, then to prune it against the three probes and measure what the harness loads.
- **Model and harness:** `opencode/big-pickle` through OpenCode 1.18.21.
- **Accepted:** A 1640-character map built only from verified repository facts, a self-applied probe pass, and JSON token counts taken from `opencode run --format json` rather than read by eye from the TUI.
- **Modified:** Removed the repository description as derivable, deleted the unenforceable no-secrets and no-push rules, replaced the unenforced-rules list with one factual statement that nothing here is mechanically enforced, and moved future-unenforced-rule guidance into conventions.
- **Rejected:** Keeping the unenforceable rules as written intentions, and asking the user to read token counts off the TUI, because the JSON event stream reports the same input-token field directly and wishful rules fail the lab's own second probe.
- **Measured:** 1640 characters; baseline 6042 input tokens; with file 6513; difference 471, which is 29% of the byte count and inside the lab's expected quarter-to-third range. Verbatim recall succeeded, with the model correctly reporting that the file states there is no test suite.

## 2026-09-29 - `/init` Comparison and Session Pause

- **Asked:** Asked how to read the token count from the TUI, then asked to continue to the `/init` comparison, and finally asked to pause until Chase partner details are known.
- **Model and harness:** `opencode/big-pickle` through OpenCode 1.18.21.
- **Accepted:** Measuring tokens through `opencode run --format json` instead of the TUI, running `/init` inside a temporary scratch copy rather than the repository, and recording the full worksheet plus self-review candidates in the measurement file so the session can resume later.
- **Modified:** Corrected the earlier assumption that the verbatim-recall probe would return a command; it instead returned the file's claim that no test suite exists, which is accurate for this repository and still distinguishes a loaded file from an unloaded one. The `/init` specimen measured 2985 characters, 1.82x the hand-written file, and was shown to fail all three probes despite fitting the budget.
- **Rejected:** Running `/init` in the working tree, because it would have overwritten the hand-written file, and leaving the Chase section as a placeholder, because the worksheet and the outstanding issues needed to be captured before stopping.
- **Deferred:** The Chase exchange, final verdict, ledger event, and commit, all pending the partner's details. One candidate addition from the `/init` specimen, the `board.md` unchecked-box convention, is proposed but not yet applied.

## 2026-09-29 - AGENTS.md Chase Review of Partner File

- **Asked:** Provided the partner's `AGENTS.md` along with the three Chase probe instructions, and asked for the review to be run against it.
- **Model and harness:** `opencode/big-pickle` through OpenCode 1.18.21.
- **Accepted:** A FAIL verdict with one quoted line per probe, plus two structural findings, because the second read found all three failure types and the lab allows no judgement call on the count.
- **Modified:** Framed Probe 1 around the fact that every role description in the partner's truth-lives list restates its filename, rather than around the presence of paths themselves, since a required section cannot simply be deleted.
- **Rejected:** Passing the partner's file on the grounds that its enforced rule already uses the correct `Enforced by: nothing yet — GHI #1` wording, because the referenced issue could not be verified as opened and a reference to a nonexistent issue is a placeholder that still fails the probe; and answering with only the review while leaving the worksheet fields unrecorded.

## 2026-09-29 - Chase Findings Applied and File Re-measured

- **Asked:** Provided three probe findings against our own `AGENTS.md` and asked for them to be recorded, since the partner returned no written review.
- **Model and harness:** `opencode/big-pickle` through OpenCode 1.18.21.
- **Accepted:** All three findings, and a PASS verdict after fixing them, because each identified a real defect and the second read then found none of the three problems.
- **Modified:** Cut the derivable half of the opening line, rewrote the commit gate as `Enforced by: nothing automated; approval is manual`, and replaced `Unconfirmed means it does not exist` with the checkable `confirm it exists by reading it`. Re-measured the file after editing rather than reporting a number that no longer matched it, and switched the token figure from bare `tokens.input` to total input because cache-read variation made the bare field unstable.
- **Rejected:** The `board.md` convention from the `/init` specimen, the earlier 471-token figure, and the claim that the file already warned about filling gaps in `board.md`, which it does not and which was corrected before recording.
- **Measured:** Final file 1665 characters; difference 450 to 490 tokens, or 0.27 to 0.30 per character, against a baseline with roughly 50 tokens of run-to-run spread.

## 2026-09-29 - Ledger Event Deviation

- **Asked:** Asked how to satisfy the exit ticket's ledger event, given that `gz` is installed but the repository has no `.gzkit` ledger.
- **Model and harness:** `opencode/big-pickle` through OpenCode 1.18.21.
- **Accepted:** Recording the commit in this log and in the measurement file while stating the deviation plainly, because the repository is documentation-only and the deviation is a finding rather than a defect to hide.
- **Modified:** None.
- **Rejected:** Running `gz init` to scaffold governance, because `gz ledger` only offers a merge driver for an existing ledger and initialising one would also contradict the `AGENTS.md` line stating there are no hooks or permission rules, invalidating the just-recorded measurement.

## 2026-10-14 - Three Probes Against Our AGENTS.md

- **Asked:** Requested three quoted probe results against our own AGENTS.md.
- **Model and harness:** GPT-6-based Codex through the Codex desktop app; exact model route is not exposed in this session.
- **Accepted:** Review findings from the current file: the course-deliverable description repeats repository context; the commit gate has no mechanical enforcement; "Unconfirmed means it does not exist" supplies no concrete verification criterion.
- **Modified:** Applied the three lab probe categories to our file instead of the partner's file. No edits to AGENTS.md were made.
- **Rejected:** Presenting this assistant review as the pending human partner review, or describing any repository rule as mechanically enforced.
