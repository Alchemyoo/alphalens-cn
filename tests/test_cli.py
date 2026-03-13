from alphalens_cn.cli import build_parser


def test_cli_parser_accepts_review_command():
    parser = build_parser()
    args = parser.parse_args(["review", "--date", "2026-03-13"])
    assert args.command == "review"
    assert args.date == "2026-03-13"
