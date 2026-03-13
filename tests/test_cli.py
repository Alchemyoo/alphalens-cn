from alphalens_cn.cli import build_parser


def test_cli_parser_accepts_review_command():
    parser = build_parser()
    args = parser.parse_args(["review", "--date", "2026-03-13"])
    assert args.command == "review"


def test_cli_parser_accepts_search_command():
    parser = build_parser()
    args = parser.parse_args(["search", "--keyword", "平安"])
    assert args.command == "search"
    assert args.keyword == "平安"


def test_cli_parser_accepts_quote_command():
    parser = build_parser()
    args = parser.parse_args(["quote", "--limit", "5"])
    assert args.command == "quote"
    assert args.limit == 5


def test_cli_parser_accepts_financial_command():
    parser = build_parser()
    args = parser.parse_args(["financial", "--symbol", "000001"])
    assert args.command == "financial"
    assert args.symbol == "000001"


def test_cli_parser_accepts_lhb_command():
    parser = build_parser()
    args = parser.parse_args(["lhb", "--date", "2026-03-13"])
    assert args.command == "lhb"
    assert args.date == "2026-03-13"
