# AlphaLens CN

> An open-source A-share market analysis toolkit for maintainers, traders, and researchers.

AlphaLens CN is a practical A-share analysis tool focused on **daily market review**, **theme tracking**, **limit-up pool analysis**, and **next-day watchlist generation**. It is designed as a maintainable open-source project rather than a one-off script.

## Why this project exists

A-share market participants often rely on fragmented tools, screenshots, and manual note-taking to understand:

- market breadth and sentiment
- limit-up / limit-down structure
- broken-board rate
- active concepts and sector rotation
- dragon-tiger list signals
- next-day observation candidates

AlphaLens CN aims to provide a transparent, scriptable, and extensible workflow for these tasks.

## MVP features

- End-of-day market summary
- Limit-up pool review
- Broken-board review
- Theme/concept aggregation
- Next-day watchlist generation
- Markdown report export

## CLI examples

```bash
PYTHONPATH=src python3 -m alphalens_cn.cli review --date 2026-03-13
PYTHONPATH=src python3 -m alphalens_cn.cli review --date 2026-03-13 --provider mock
PYTHONPATH=src python3 -m alphalens_cn.cli review --date 2026-03-13 --output reports/2026-03-13.md
```

## Project status

Early-stage MVP. Core reporting pipeline is implemented with mock-safe fallback data so contributors can develop locally before wiring in production-grade market data sources.

## Roadmap

See [ROADMAP.md](./ROADMAP.md).

## License

MIT
