from __future__ import annotations

from typing import Any


def _to_float(value: Any, default: float = 0.0) -> float:
    try:
        if value in (None, "", "-", "--"):
            return default
        return float(value)
    except Exception:
        return default


def score_candidate(row: dict, hot_concepts: list[str] | None = None) -> dict:
    hot_concepts = hot_concepts or []
    name = str(row.get('名称') or '')
    code = str(row.get('代码') or '')
    board = int(_to_float(row.get('连板数'), 0))
    turnover = _to_float(row.get('成交额'), 0) / 1e8
    industry = str(row.get('所属行业') or '')
    first_limit_time = str(row.get('首次封板时间') or '')
    last_limit_time = str(row.get('最后封板时间') or '')
    open_count = int(_to_float(row.get('开板次数'), 0))
    pct = _to_float(row.get('涨跌幅'), 0)

    theme_score = 30 if industry and industry in hot_concepts[:1] else 20 if industry and industry in hot_concepts[:2] else 10 if industry else 0
    board_score = 20 if 2 <= board <= 3 else 12 if board == 1 else 8 if board >= 4 else 0
    turnover_score = 15 if 5 <= turnover <= 20 else 10 if 3 <= turnover < 5 or 20 < turnover <= 30 else 5 if 1 <= turnover < 3 else 0

    structure_score = 0
    if open_count == 0 and board >= 1:
        structure_score = 15
    elif open_count <= 1 and pct >= 9:
        structure_score = 10
    elif open_count <= 2:
        structure_score = 5

    tradable_score = 10
    if board >= 4:
        tradable_score = 2
    elif first_limit_time and first_limit_time <= '093500':
        tradable_score = 6
    if last_limit_time and last_limit_time >= '145000' and open_count > 0:
        tradable_score = max(tradable_score, 8)

    flow_score = 10 if turnover >= 8 and open_count <= 1 else 6 if turnover >= 3 else 0

    total = theme_score + board_score + turnover_score + structure_score + tradable_score + flow_score
    return {
        'name': name,
        'code': code,
        'industry': industry,
        'board': board,
        'turnover_yi': round(turnover, 2),
        'score': total,
        'theme_score': theme_score,
        'board_score': board_score,
        'turnover_score': turnover_score,
        'structure_score': structure_score,
        'tradable_score': tradable_score,
        'flow_score': flow_score,
    }


def select_top3(limitup_rows: list[dict], hot_concepts: list[str] | None = None) -> list[dict]:
    scored = [score_candidate(row, hot_concepts=hot_concepts) for row in limitup_rows]
    filtered = [x for x in scored if x['score'] >= 70 and x['theme_score'] >= 10 and x['structure_score'] >= 10]
    filtered.sort(key=lambda x: (x['score'], x['board'], x['turnover_yi']), reverse=True)
    return filtered[:3]
