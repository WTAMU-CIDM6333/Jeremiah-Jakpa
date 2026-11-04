# Test Runner Skill

Multi-step procedure for running tests.

## Steps
1. Discover tests: `uv run python -m unittest discover -s tests`
2. Run all tests and check for failures
3. Report results with coverage if needed
4. Enforced by: pre-commit hook `test-discovery`
