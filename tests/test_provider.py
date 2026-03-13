from alphalens_cn.providers import get_provider


def test_get_mock_provider():
    provider = get_provider("mock")
    summary = provider.get_market_summary("2026-03-13")
    assert summary.date == "2026-03-13"
    assert summary.benchmark == "沪指"
