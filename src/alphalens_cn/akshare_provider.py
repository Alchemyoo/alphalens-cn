from __future__ import annotations

from typing import List

from .models import Candidate, MarketSummary
from .mock_data import get_mock_summary
from .scoring import select_top3


class AKShareProvider:
    name = "akshare"

    def get_market_summary(self, date: str) -> MarketSummary:
        try:
            import importlib.util
            if not importlib.util.find_spec("akshare"):
                s = get_mock_summary(date)
                s.provider = "mock"
                s.note = "akshare not installed; fallback to mock"
                return s

            from importlib import import_module
            ds_mod = import_module("data_sources")
            fetcher = ds_mod.DataFetcher(date=date.replace("-", ""))

            market = fetcher._fetch_market()
            sentiment = fetcher.fetch_all(mode="sentiment").get("sentiment", {})
            limitup = fetcher._fetch_limitup(top=10)
            concepts = fetcher._fetch_concepts(top=5)

            indices = market.get("indices") or []
            benchmark_name = "沪指"
            benchmark_change = 0.0
            if indices:
                benchmark_name = str(indices[0].get("name") or "沪指")
                benchmark_change = float(indices[0].get("pct_change") or 0.0)

            turnover_yi = float(market.get("turnover") or 0.0)
            turnover_trillion = round(turnover_yi / 10000, 2) if turnover_yi else 0.0

            hot_concepts: List[str] = []
            if concepts.get("top_concepts"):
                for item in concepts["top_concepts"][:5]:
                    name = str(item.get("name") or "").strip()
                    if name:
                        hot_concepts.append(name)
            elif limitup.get("main_themes"):
                hot_concepts = [str(x) for x in limitup.get("main_themes", [])[:5] if str(x).strip()]

            watchlist = []
            for leader in limitup.get("leaders", [])[:3]:
                name = str(leader.get("name") or "").strip()
                code = str(leader.get("code") or "").strip()
                board = leader.get("board")
                if name and code:
                    label = f"{name}({code})"
                    if board not in (None, "", "nan"):
                        label += f" - {board}板"
                    watchlist.append(label)
            if not watchlist:
                watchlist = ["高辨识度核心股", "分歧转一致首板", "机构关注方向"]

            candidate_rows = []
            try:
                if fetcher.ak:
                    zt_df = fetcher.ak.stock_zt_pool_em(date=date.replace('-', ''))
                    if not zt_df.empty:
                        candidate_rows = zt_df.to_dict(orient='records')
            except Exception:
                candidate_rows = []
            top3 = select_top3(candidate_rows, hot_concepts=hot_concepts)
            candidates = [
                Candidate(
                    name=x['name'],
                    code=x['code'],
                    industry=x.get('industry', ''),
                    board=int(x.get('board', 0)),
                    score=int(x.get('score', 0)),
                    turnover_yi=float(x.get('turnover_yi', 0.0)),
                )
                for x in top3
            ]

            note_parts = [market.get("note"), sentiment.get("note"), limitup.get("note"), concepts.get("note")]
            note = " | ".join([x for x in note_parts if x])

            return MarketSummary(
                date=date,
                benchmark=benchmark_name,
                benchmark_change_pct=benchmark_change,
                turnover_trillion=turnover_trillion,
                advancers=int(market.get("up_count") or 0),
                decliners=int(market.get("down_count") or 0),
                flat=int(market.get("flat_count") or 0),
                limit_up_count=int(sentiment.get("limit_up_count") or 0),
                broken_board_count=int(sentiment.get("exploded_count") or 0),
                limit_down_count=int(sentiment.get("limit_down_count") or 0),
                hot_concepts=hot_concepts,
                watchlist=watchlist,
                candidates=candidates,
                provider="akshare",
                note=note,
            )
        except Exception as e:
            s = get_mock_summary(date)
            s.provider = "mock"
            s.note = f"akshare provider fallback: {e}"
            return s
