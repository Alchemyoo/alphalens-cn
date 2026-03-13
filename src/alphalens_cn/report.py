from .models import MarketSummary


def render_markdown(summary: MarketSummary) -> str:
    concept_text = "、".join(summary.hot_concepts) if summary.hot_concepts else "无"
    watchlist_text = "\n".join(f"- {item}" for item in summary.watchlist) if summary.watchlist else "- 无"
    breadth_ratio = round(summary.advancers / max(summary.decliners, 1), 2)

    return f"""# AlphaLens CN 日报 - {summary.date}

## 市场概览
- 指数：{summary.benchmark} {summary.benchmark_change_pct:+.2f}%
- 两市成交额：{summary.turnover_trillion:.2f} 万亿
- 上涨家数：{summary.advancers}
- 下跌家数：{summary.decliners}
- 平盘家数：{summary.flat}
- 市场宽度（涨/跌）：{breadth_ratio}

## 情绪指标
- 涨停家数：{summary.limit_up_count}
- 炸板家数：{summary.broken_board_count}
- 跌停家数：{summary.limit_down_count}

## 热门概念
- {concept_text}

## 次日观察
{watchlist_text}

## 数据来源
- provider：{summary.provider}
- note：{summary.note or '无'}
"""
