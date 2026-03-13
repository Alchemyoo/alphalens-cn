# AlphaLens CN

> An open-source A-share market analysis toolkit for maintainers, traders, and researchers.

AlphaLens CN is a practical A-share analysis tool focused on **daily market review**, **theme tracking**, **limit-up pool analysis**, **stock search**, **historical K-line query**, and **next-day watchlist generation**.

## MVP features

- End-of-day market summary
- Limit-up pool review
- Broken-board review
- Theme/concept aggregation
- Next-day watchlist generation
- Realtime quote query
- Stock search
- Historical K-line query
- Industry/concept board snapshot
- Markdown report export

## CLI examples

```bash
PYTHONPATH=src python3 -m alphalens_cn.cli review --date 2026-03-13 --provider akshare
PYTHONPATH=src python3 -m alphalens_cn.cli quote --limit 5
PYTHONPATH=src python3 -m alphalens_cn.cli search --keyword 平安
PYTHONPATH=src python3 -m alphalens_cn.cli kline --symbol 000001 --days 10
PYTHONPATH=src python3 -m alphalens_cn.cli industry --limit 10
PYTHONPATH=src python3 -m alphalens_cn.cli concept --limit 10
```

## Project status

Early-stage MVP with real-data support through AKShare and a maintainable CLI-oriented architecture.

## License

MIT
