from dataclasses import dataclass, field
from typing import List


@dataclass
class Candidate:
    name: str
    code: str
    industry: str = ""
    board: int = 0
    score: int = 0
    turnover_yi: float = 0.0


@dataclass
class MarketSummary:
    date: str
    benchmark: str
    benchmark_change_pct: float
    turnover_trillion: float
    advancers: int
    decliners: int
    flat: int
    limit_up_count: int
    broken_board_count: int
    limit_down_count: int
    hot_concepts: List[str] = field(default_factory=list)
    watchlist: List[str] = field(default_factory=list)
    candidates: List[Candidate] = field(default_factory=list)
    provider: str = "mock"
    note: str = ""
