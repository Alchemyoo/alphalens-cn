import argparse

from .exporters import write_text
from .providers import get_provider
from .report import render_markdown


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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="alphalens-cn")
    sub = parser.add_subparsers(dest="command", required=True)

    review = sub.add_parser("review", help="Generate end-of-day market review")
    review.add_argument("--date", required=True, help="Trading date, e.g. 2026-03-13")
    review.add_argument("--provider", default="mock", help="Data provider name, default: mock")
    review.add_argument("--output", help="Optional markdown output path")
    review.set_defaults(func=cmd_review)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
