- A Python task is not done until verification covers lint, types, and relevant tests without unrelated style churn.
- Preferred verification flow:
  1. run editor/MCP diagnostics on touched files
  2. run focused pytest files first, then broaden to full `pytest` when impact is broad or uncertain
  3. run strict type checking
  4. run lint checks
- CLI equivalents:
  - `pytest tests/test_<touched_module>.py -q`
  - `pytest`
  - `python -m pyright`
  - `ruff check .`
- Do not autoformat unrelated files just to satisfy style; preserve existing manual alignment/formatting.
- When tests are added/edited, verify fixture placement in `tests/conftest.py`, required parametrization, deterministic data, and assertion messages.