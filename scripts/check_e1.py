"""Validate E1 preparation, not flight success, before publication."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    ".opencode/agents/mentalysis.md",
    "opencode.json",
    "docs/PRD.md",
    "evolution-01/flight-card.md",
    "evolution-01/flight-log.md",
    "evolution-01/fixtures/review-queue.md",
    "evolution-01/evidence/README.md",
    "design-analyses/E1-react-opencode.md",
    "design-analyses/LEDGER.md",
    "AI_LOG.md",
)
SCOPES = (
    "documents", "ledger", "taxonomy", "decomposition", "brief-structure",
    "req-kind-discipline", "brief-command-shape", "kind-invariance",
    "persona-witness", "line-endings",
)


def preparation_errors(root: Path) -> list[str]:
    """Return structural defects; no structural check awards a sortie verdict."""
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file() or not (root / name).read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty required artifact: {name}")
    if errors:
        return errors

    agent_text = (root / REQUIRED[0]).read_text(encoding="utf-8")
    try:
        sections = agent_text.split("---", 2)
        if sections[0].strip() or len(sections) != 3:
            raise ValueError("missing YAML frontmatter")
        agent = yaml.safe_load(sections[1])
        if not isinstance(agent, dict):
            raise TypeError("frontmatter must be a mapping")
        for key, value in (("mode", "primary"), ("model", "opencode/big-pickle"), ("steps", 5)):
            if agent.get(key) != value or (key == "steps" and type(agent.get(key)) is not int):
                errors.append(f"Agent {key} must equal {value!r}")
        if not agent.get("description") or not sections[2].strip():
            errors.append("Agent needs a description and instructions")
    except (ValueError, TypeError, yaml.YAMLError) as exc:
        errors.append(f"Invalid agent: {exc}")

    try:
        config = json.loads((root / "opencode.json").read_text(encoding="utf-8"))
        if not isinstance(config, dict) or config.get("default_agent") != "mentalysis":
            errors.append("Project must select mentalysis as default_agent")
    except ValueError as exc:
        errors.append(f"Invalid opencode.json: {exc}")

    prd = (root / "docs/PRD.md").read_text(encoding="utf-8")
    attestation = prd.partition("## Attestation")[2]
    if not re.search(r"I have reviewed and approve", attestation) or not re.search(
        r"Jeremiah Jakpa.*\d{4}-\d{2}-\d{2}", attestation
    ):
        errors.append("PRD must retain the owner's dated approval")

    queue = (root / "evolution-01/fixtures/review-queue.md").read_text(encoding="utf-8").splitlines()
    if len(queue) != 20 or any(not line.startswith(f"{i:02d}. ") for i, line in enumerate(queue, 1)):
        errors.append("Review fixture must contain exactly 20 sequential numbered lines")

    card = (root / "evolution-01/flight-card.md").read_text(encoding="utf-8")
    for heading in (
        "ENVELOPE", "DESIGN CLAIM", "SYSTEMS UNDER TEST", "SUBSTRATE", "TEST POINTS",
        "INSTRUMENTATION", "PRE-REGISTERED FALSIFIERS", "ABORT", "CHASE GO",
    ):
        if f"## {heading}" not in card:
            errors.append(f"Flight card missing {heading}")
    normalized_card = " ".join(card.split())
    if "permission was loosened, a tool was removed, or an export was edited" not in normalized_card:
        errors.append("Flight card must retain the mandatory falsifier")
    for expected in ("1428.57", "offset 1", "limit 1", "20 items"):
        if expected not in card:
            errors.append(f"Flight card missing test contract: {expected}")

    log = (root / "evolution-01/flight-log.md").read_text(encoding="utf-8")
    evidence = [p for p in (root / "evolution-01/evidence").rglob("*") if p.is_file() and p.name != "README.md"]
    has_go = bool(re.search(r"^GO\s+—\s+[^\n]+\s+—\s+\d{4}-\d{2}-\d{2}", card, re.MULTILINE))
    if not has_go and ("Status: NOT FLOWN" not in log or evidence):
        errors.append("Flight observations/exports require an actual dated Chase GO")
    for path in evidence:
        if not path.name.endswith(".sanitized.json"):
            errors.append(f"Unexpected evidence file (raw exports forbidden): {path.relative_to(root)}")
        else:
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError):
                errors.append(f"Invalid evidence JSON: {path.relative_to(root)}")
    return errors


def main() -> int:
    errors = preparation_errors(ROOT)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    commands = [
        ["uv", "run", "python", "-m", "unittest", "discover", "-s", "tests", "-v"],
        ["uv", "run", "ruff", "check", "scripts/check_e1.py", "tests/test_e1_preparation.py"],
        ["uv", "run", "gz", "validate", *[f"--{scope}" for scope in SCOPES]],
        ["uv", "run", "gz", "obpi", "validate", "--adr", "ADR-0.1.0", "--authored"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode:
            return result.returncode
    print("PASS: E1 preparation publication checks. Flight success and sanitization provenance require human evidence review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
