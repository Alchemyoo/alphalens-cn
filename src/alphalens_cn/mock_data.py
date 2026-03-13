from .models import MarketSummary


def get_mock_summary(date: str) -> MarketSummary:
    return MarketSummary(
        date=date,
        benchmark="沪指",
        benchmark_change_pct=0.68,
        turnover_trillion=1.12,
        advancers=3124,
        decliners=1811,
        flat=146,
        limit_up_count=87,
        broken_board_count=21,
        limit_down_count=4,
        hot_concepts=["AI算力", "机器人", "低空经济", "证券"],
        watchlist=["高辨识度龙头", "分歧转一致首板", "机构持续净买入标的"],
        provider="mock",
        note="mock-safe fallback summary",
    )
