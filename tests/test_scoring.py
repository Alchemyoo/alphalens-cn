from alphalens_cn.scoring import score_candidate, select_top3


def test_score_candidate_returns_score():
    row = {
        '名称': '测试股',
        '代码': '000001',
        '连板数': 2,
        '成交额': 900000000,
        '所属行业': '电力',
        '首次封板时间': '094500',
        '最后封板时间': '145500',
        '开板次数': 0,
        '涨跌幅': 10.0,
    }
    scored = score_candidate(row, hot_concepts=['电力', '化工'])
    assert scored['score'] >= 60
    assert scored['name'] == '测试股'


def test_select_top3_has_fallback():
    rows = [
        {'名称': 'A', '代码': '000001', '连板数': 1, '成交额': 200000000, '所属行业': '电力', '开板次数': 2, '涨跌幅': 10},
        {'名称': 'B', '代码': '000002', '连板数': 1, '成交额': 300000000, '所属行业': '化工', '开板次数': 2, '涨跌幅': 10},
        {'名称': 'C', '代码': '000003', '连板数': 1, '成交额': 400000000, '所属行业': '电力', '开板次数': 3, '涨跌幅': 9},
    ]
    picked = select_top3(rows, hot_concepts=['电力'])
    assert len(picked) == 3
