from pathlib import Path
import sys

from .akshare_provider import AKShareProvider
from .mock_data import get_mock_summary
from .models import MarketSummary


class DataProvider:
    name = "base"

    def get_market_summary(self, date: str) -> MarketSummary:
        raise NotImplementedError


class MockProvider(DataProvider):
    name = "mock"

    def get_market_summary(self, date: str) -> MarketSummary:
        return get_mock_summary(date)


def _ensure_skill_path() -> None:
    skill_scripts = Path("/var/minis/skills/a-share-close-review/scripts")
    skill_path = str(skill_scripts)
    if skill_scripts.exists() and skill_path not in sys.path:
        sys.path.insert(0, skill_path)


def get_provider(name: str) -> DataProvider:
    _ensure_skill_path()
    providers = {
        "mock": MockProvider(),
        "akshare": AKShareProvider(),
    }
    if name not in providers:
        raise ValueError(f"unknown provider: {name}")
    return providers[name]
