from alphalens_cn.scoring import score_candidate


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
    assert scored['score'] >= 70
    assert scored['name'] == '测试股'
