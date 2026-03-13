# Contributing

Thanks for your interest in contributing to AlphaLens CN.

## Ways to contribute
- Improve A-share market data adapters
- Enhance report quality and explainability
- Add tests for CLI and report generation
- Improve documentation and examples

## Development setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e . pytest
PYTHONPATH=src python3 -m alphalens_cn.cli review --date 2026-03-13
pytest
```

## Principles
- Keep outputs transparent and auditable
- Avoid opaque magic numbers without explanation
- Preserve reproducibility for daily reports
- Prefer modular provider adapters
