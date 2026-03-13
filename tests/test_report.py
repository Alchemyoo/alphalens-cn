from alphalens_cn.mock_data import get_mock_summary
from alphalens_cn.report import render_markdown


def test_render_markdown_contains_key_sections():
    summary = get_mock_summary("2026-03-13")
    md = render_markdown(summary)
    assert "# AlphaLens CN 日报 - 2026-03-13" in md
    assert "## 市场概览" in md
    assert "## 情绪指标" in md
    assert "## 热门概念" in md
    assert "## 次日观察" in md
