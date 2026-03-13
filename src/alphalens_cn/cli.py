import argparse
import json

from .exporters import write_text
from .market_tools import (
    get_board_concept,
    get_board_industry,
    get_historical_kline,
    get_realtime_quotes,
    search_stock,
)
from .providers import get_provider
from .report import render_markdown


def _print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_review(args: argparse.Namespace) -> int:
    provider = get_provider(args.provider)
    summary = provider.get_market_summary(args.date)
    output = render_markdown(summary)
    if args.output:
        out_path = write_text(args.output, output)
        print(f"report written to {out_path}")
    else:
        print(output)
    return 0


def _run_json_command(func, *args, **kwargs) -> int:
    try:
        _print_json(func(*args, **kwargs))
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False, indent=2))
        return 1


def cmd_quote(args: argparse.Namespace) -> int:
    symbols = args.symbols.split(",") if args.symbols else None
    return _run_json_command(get_realtime_quotes, symbols=symbols, limit=args.limit)


def cmd_search(args: argparse.Namespace) -> int:
    return _run_json_command(search_stock, args.keyword, limit=args.limit)


def cmd_kline(args: argparse.Namespace) -> int:
    return _run_json_command(get_historical_kline, args.symbol, period=args.period, days=args.days)


def cmd_industry(args: argparse.Namespace) -> int:
    return _run_json_command(get_board_industry, limit=args.limit)


def cmd_concept(args: argparse.Namespace) -> int:
    return _run_json_command(get_board_concept, limit=args.limit)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="alphalens-cn")
    sub = parser.add_subparsers(dest="command", required=True)

    review = sub.add_parser("review", help="Generate end-of-day market review")
    review.add_argument("--date", required=True, help="Trading date, e.g. 2026-03-13")
    review.add_argument("--provider", default="mock", help="Data provider name, default: mock")
    review.add_argument("--output", help="Optional markdown output path")
    review.set_defaults(func=cmd_review)

    quote = sub.add_parser("quote", help="Get realtime A-share quotes")
    quote.add_argument("--symbols", help="Comma-separated stock codes")
    quote.add_argument("--limit", type=int, default=20)
    quote.set_defaults(func=cmd_quote)

    search = sub.add_parser("search", help="Search stock by code or name")
    search.add_argument("--keyword", required=True)
    search.add_argument("--limit", type=int, default=10)
    search.set_defaults(func=cmd_search)

    kline = sub.add_parser("kline", help="Get historical K-line data")
    kline.add_argument("--symbol", required=True)
    kline.add_argument("--period", default="daily", choices=["daily", "weekly", "monthly"])
    kline.add_argument("--days", type=int, default=30)
    kline.set_defaults(func=cmd_kline)

    industry = sub.add_parser("industry", help="Get industry board snapshot")
    industry.add_argument("--limit", type=int, default=20)
    industry.set_defaults(func=cmd_industry)

    concept = sub.add_parser("concept", help="Get concept board snapshot")
    concept.add_argument("--limit", type=int, default=20)
    concept.set_defaults(func=cmd_concept)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
